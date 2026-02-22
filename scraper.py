import datetime
import re
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

DOMAIN = "https://podscripts.co"

# ============================================================
# PODCAST-QUELLEN KONFIGURATION
# ============================================================
# Hier fügst du neue Podcasts hinzu. Der Scraper verarbeitet
# alle Quellen automatisch. Jeder Eintrag braucht:
#   - name:        Kürzel für Dateinamen
#   - url:         Übersichtsseite auf podscripts.co
#   - min_chars:   Mindestlänge (filtert Bonus-/Kurzepisoden)
#   - exclude:     Begriffe im URL-Pfad, die übersprungen werden
#   - corrections: Podcast-spezifische Transkriptionsfehler
# ============================================================

SOURCES = [
    {
        "name": "TBPN",
        "url": "https://podscripts.co/podcasts/tbpn-live/",
        "min_chars": 50000,
        "exclude": ["diet"],
        "corrections": {
            "TVPN": "TBPN",
            "Grogopedia": "Grokopedia",
            "Quen-3": "Qwen-3",
            "Aerobor": "Arabor",
            "Aribor": "Arabor",
        },
    },
    {
        "name": "All-In",
        "url": "https://podscripts.co/podcasts/all-in-with-chamath-jason-sacks-friedberg/",
        "min_chars": 30000,
        "exclude": [],
        "corrections": {
            "Jamath": "Chamath",
            "Chamat ": "Chamath ",
            "Freedberg": "Friedberg",
            "Sax ": "Sacks ",
        },
    },
    # -------------------------------------------------------
    # Weitere Quellen einfach hier einfügen, z.B.:
    #
    # {
    #     "name": "BG2",
    #     "url": "https://podscripts.co/podcasts/bg2pod/",
    #     "min_chars": 15000,
    #     "exclude": [],
    #     "corrections": {},
    # },
    # -------------------------------------------------------
]


# ============================================================
# GEMEINSAME CLEANING-PATTERNS
# ============================================================

AD_PATTERNS = [
    r"Let me (?:also )?tell you about\b",
    r"And let me (?:also )?tell you about\b",
    r"While .{0,30} let me tell you about\b",
    r"I'm (?:also )?going to tell you about\b",
    r"And I'm (?:also )?going to tell you about\b",
    r"is made possible by\b",
    r"is brought to you by\b",
    r"is sponsored by\b",
    r"Our presenting sponsor\b",
    r"Today's episode is powered by\b",
]
AD_REGEX = re.compile("|".join(AD_PATTERNS), re.IGNORECASE)

SPONSOR_LINK_REGEX = re.compile(
    r"^.{1,60}\s*[-–—]\s*https?://\S+$", re.MULTILINE
)

FOOTER_MARKERS = [
    "There aren't comments yet",
    "Report Ad",
    "What is this?",
    "Click on any sentence in the transcript",
]

TRANSCRIPT_START_MARKERS = {
    "TBPN": [
        "You're watching TBPN",
        "you're watching TBPN",
        "We are live from",
        "we are live from",
        "Sign up for TBPN",
    ],
    "All-In": [
        "welcome back to the",
        "Welcome back to the",
        "I'm going all in",
        "going all in",
        "All right, everybody",
        "besties",
    ],
    "_default": [
        "Transcript",
    ],
}

GUEST_PATTERNS = [
    r"[Ll]et'?s bring (?:him|her|them) in",
    r"[Ww]e have .{2,40} (?:joining|in the .{0,20}waiting room)",
    r"[Ll]et'?s bring in .{2,40}",
]
GUEST_REGEX = re.compile("|".join(GUEST_PATTERNS))


# ============================================================
# CLEANING FUNCTIONS
# ============================================================

def clean_transcript(raw_text, source):
    """Bereinigt ein Transkript basierend auf der Quellen-Konfiguration."""
    name = source["name"]
    corrections = source.get("corrections", {})
    print(f"  [{name}] Starte Text-Reinigung...")
    cleaned = raw_text

    # --- STUFE 1: Header abschneiden ---
    markers = TRANSCRIPT_START_MARKERS.get(name, TRANSCRIPT_START_MARKERS["_default"])
    for marker in markers:
        idx = cleaned.find(marker)
        if idx != -1:
            cleaned = cleaned[idx:]
            print(f"  [{name}] Header entfernt (bei: '{marker[:30]}...')")
            break

    # --- STUFE 2: Footer abschneiden ---
    for marker in FOOTER_MARKERS:
        idx = cleaned.find(marker)
        if idx != -1:
            cleaned = cleaned[:idx]
            print(f"  [{name}] Footer entfernt")
            break

    # --- STUFE 3: Werbeblöcke entfernen ---
    paragraphs = cleaned.split("\n\n")
    filtered = []
    ads_removed = 0
    for para in paragraphs:
        para_stripped = para.strip()
        if not para_stripped:
            continue
        if AD_REGEX.search(para_stripped):
            ads_removed += 1
            continue
        filtered.append(para_stripped)
    cleaned = "\n\n".join(filtered)
    if ads_removed:
        print(f"  [{name}] {ads_removed} Werbeblöcke entfernt")

    # --- STUFE 4: Sponsor-Links entfernen ---
    cleaned = SPONSOR_LINK_REGEX.sub("", cleaned)

    # --- STUFE 5: Timestamps entfernen ---
    cleaned = re.sub(r'Starting point is \d{2}:\d{2}:\d{2}', '', cleaned)
    cleaned = re.sub(r'\(\d{2}:\d{2}:\d{2}\)', '', cleaned)

    # --- STUFE 6: Podcast-spezifische Korrekturen ---
    for wrong, right in corrections.items():
        if wrong in cleaned:
            count = cleaned.count(wrong)
            cleaned = cleaned.replace(wrong, right)
            print(f"  [{name}] Korrektur: '{wrong}' → '{right}' ({count}x)")

    # --- STUFE 7: Normalisierung ---
    cleaned = re.sub(r'(?<!\n)\n(?!\n)', ' ', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    cleaned = re.sub(r' +', ' ', cleaned)
    cleaned = cleaned.strip()

    print(f"  [{name}] Fertig: {len(cleaned)} Zeichen")
    return cleaned


def add_segment_markers(text):
    """Fügt '---' vor Gast-Wechseln ein."""
    lines = text.split("\n\n")
    result = []
    for i, para in enumerate(lines):
        if GUEST_REGEX.search(para) and i > 0:
            result.append("\n---\n")
        result.append(para)
    return "\n\n".join(result)


def build_header(title, url, name, date_str, char_count):
    """Metadaten-Header für ein Transkript."""
    return (
        f"=== PODCAST-TRANSKRIPT: {name} ===\n"
        f"Titel: {title}\n"
        f"Quelle: {url}\n"
        f"Datum: {date_str}\n"
        f"Länge: ~{char_count // 1000}k Zeichen\n"
        f"Hinweis: Werbeblöcke entfernt. '---' markiert Gast-Wechsel.\n"
        f"{'=' * 40}\n\n"
    )


# ============================================================
# SCRAPER
# ============================================================

def scrape_source(page, source):
    """
    Scraped die neueste lange Episode eines einzelnen Podcasts.
    Gibt (title, url, cleaned_text) zurück, oder None.
    """
    name = source["name"]
    base_url = source["url"]
    min_chars = source["min_chars"]
    exclude = source.get("exclude", [])

    print(f"\n{'='*50}")
    print(f"Scrape: {name}")
    print(f"{'='*50}")

    page.goto(base_url)
    page.wait_for_load_state('networkidle')

    soup = BeautifulSoup(page.content(), 'html.parser')
    all_links = soup.find_all('a', href=True)

    # Episode-Links sammeln
    base_path = base_url.replace(DOMAIN, "")
    episode_links = []
    for link in all_links:
        href = link.get('href', '')
        if (href.startswith(base_path)
                and len(href) > len(base_path)
                and "page=" not in href):
            if not any(ex.lower() in href.lower() for ex in exclude):
                episode_links.append(href)

    print(f"  {len(episode_links)} Episode-Links gefunden")

    for link in episode_links:
        ep_url = DOMAIN + link if link.startswith('/') else link
        print(f"  Prüfe: {ep_url}")

        page.goto(ep_url)
        page.wait_for_load_state('networkidle')

        # "Read More" Buttons klicken
        try:
            buttons = page.locator('button')
            for i in range(buttons.count()):
                text = buttons.nth(i).inner_text().lower()
                if "read more" in text or "load" in text or "show" in text:
                    buttons.nth(i).click(timeout=3000)
                    page.wait_for_timeout(2000)
        except Exception:
            pass

        ep_html = page.content()
        ep_soup = BeautifulSoup(ep_html, 'html.parser')

        for element in ep_soup(["nav", "footer", "header", "script", "style"]):
            element.decompose()

        raw_text = ep_soup.get_text(separator='\n\n', strip=True)

        # Cleaning
        clean_text = clean_transcript(raw_text, source)
        clean_text = add_segment_markers(clean_text)

        if len(clean_text) > min_chars:
            title = (ep_soup.find('h1').get_text(strip=True)
                     if ep_soup.find('h1') else "Unbekannter Titel")
            print(f"  GEFUNDEN! ({len(clean_text)} Zeichen)")
            return title, ep_url, clean_text
        else:
            print(f"  Zu kurz ({len(clean_text)} Zeichen), weiter...")

    print(f"  [{name}] Keine passende Episode gefunden.")
    return None


def scrape_all():
    """Scraped alle konfigurierten Quellen und speichert die Ergebnisse."""
    date_str = datetime.date.today().strftime("%Y-%m-%d")

    print("Starte Browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        results = []

        for source in SOURCES:
            result = scrape_source(page, source)
            if result:
                title, url, text = result
                header = build_header(title, url, source["name"], date_str, len(text))
                results.append({
                    "name": source["name"],
                    "title": title,
                    "url": url,
                    "content": header + text,
                })

        browser.close()

    if not results:
        print("\nFehler: Keine Episoden gefunden.")
        return

    # ---------------------------------------------------------
    # EINZELNE DATEIEN pro Quelle (für Archiv)
    # ---------------------------------------------------------
    for r in results:
        fname = f"Transcript_{r['name']}_{date_str}.txt"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(r["content"])
        print(f"Gespeichert: {fname}")

    # ---------------------------------------------------------
    # KOMBINIERTE DATEI für Gemini/Claude (latest.txt)
    # ---------------------------------------------------------
    combined_header = (
        f"=== KOMBINIERTES BRIEFING-MATERIAL | {date_str} ===\n"
        f"Quellen: {', '.join(r['name'] for r in results)}\n"
        f"Anzahl Transkripte: {len(results)}\n"
        f"Gesamtlänge: ~{sum(len(r['content']) for r in results) // 1000}k Zeichen\n"
        f"{'=' * 50}\n\n"
        f"WICHTIG FÜR DIE ANALYSE:\n"
        f"- Jedes Transkript ist durch '=== PODCAST-TRANSKRIPT: ...' getrennt\n"
        f"- Verknüpfe Themen ÜBER Quellen hinweg, wenn sie verwandt sind\n"
        f"- Gib bei jeder These an, aus welcher Quelle sie stammt\n\n"
    )

    combined = combined_header + "\n\n".join(r["content"] for r in results)

    with open("latest.txt", "w", encoding="utf-8") as f:
        f.write(combined)
    print(f"\nlatest.txt aktualisiert ({len(combined)} Zeichen, {len(results)} Quellen)")

    # Zusammenfassung
    print(f"\n{'='*50}")
    print("ZUSAMMENFASSUNG")
    print(f"{'='*50}")
    for r in results:
        print(f"  ✅ {r['name']}: {r['title'][:60]}... ({len(r['content'])//1000}k)")


if __name__ == "__main__":
    scrape_all()
