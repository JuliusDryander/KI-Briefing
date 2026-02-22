import datetime
import re
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

BASE_URL = "https://podscripts.co/podcasts/tbpn-live/"
DOMAIN = "https://podscripts.co"

# ============================================================
# 1. TRANSCRIPT CLEANING – Der Staubsauger (v2.0)
# ============================================================
# Ziel: Gemini bekommt NUR den Dialog – kein Website-Chrome,
# keine Werbung, kein Footer. Das reduziert Rauschen und
# verhindert, dass Gemini Token für Müll verschwendet.
# ============================================================

# Werbe-Keywords: Wenn ein Absatz mit einem davon beginnt,
# ist es ein Ad-Read und wird entfernt.
AD_PATTERNS = [
    r"Let me (?:also )?tell you about\b",
    r"And let me (?:also )?tell you about\b",
    r"While .{0,30} let me tell you about\b",
    r"I'm (?:also )?going to tell you about\b",
    r"And I'm (?:also )?going to tell you about\b",
    r"is made possible by\b",
    r"is brought to you by\b",
    r"is sponsored by\b",
]
AD_REGEX = re.compile("|".join(AD_PATTERNS), re.IGNORECASE)

# Sponsor-Einzeiler: "Ramp - https://Ramp.com" etc.
SPONSOR_LINK_REGEX = re.compile(
    r"^.{1,60}\s*[-–—]\s*https?://\S+$", re.MULTILINE
)

# Footer/Boilerplate, die nach dem Transkript kommt
FOOTER_MARKERS = [
    "There aren't comments yet",
    "Report Ad",
    "What is this?",
    "Click on any sentence in the transcript to leave a comment",
]

# Website-Header, die vor dem Transkript stehen
HEADER_END_MARKERS = [
    "Transcript",       # podscripts.co zeigt "Transcript" als Tab
    "Discussion",       # ... und "Discussion" direkt danach
]

# Transkript-Start-Marker (erster echter Dialog)
TRANSCRIPT_START_MARKERS = [
    "You're watching TBPN",
    "you're watching TBPN",
    "We are live from",
    "we are live from",
    "Sign up for TBPN",
]


def clean_transcript(raw_text):
    """
    Bereinigt das rohe Transkript in mehreren Stufen:
    1. Website-Header entfernen
    2. Footer entfernen
    3. Werbeblöcke entfernen
    4. Sponsor-Links entfernen
    5. Timestamps bereinigen
    6. Tippfehler korrigieren
    7. Leerzeilen normalisieren
    """
    print("Starte Text-Reinigung (Staubsauger v2.0)...")
    cleaned = raw_text

    # ----------------------------------------------------------
    # STUFE 1: Website-Header abschneiden
    # Alles vor dem eigentlichen Transkript ist Navigation,
    # Metadaten, Podcast-Beschreibungen etc.
    # ----------------------------------------------------------

    # Versuche zuerst, den Transkript-Start-Marker zu finden
    for marker in TRANSCRIPT_START_MARKERS:
        idx = cleaned.find(marker)
        if idx != -1:
            cleaned = cleaned[idx:]
            print(f"  Header entfernt (Start bei: '{marker[:40]}...')")
            break
    else:
        # Fallback: Suche nach "Transcript" oder "Discussion" Header
        for marker in HEADER_END_MARKERS:
            # Suche das letzte Vorkommen vor dem Haupttext
            pattern = re.compile(re.escape(marker) + r"\s*\n", re.IGNORECASE)
            matches = list(pattern.finditer(cleaned))
            if matches:
                last_match = matches[-1]
                cleaned = cleaned[last_match.end():]
                print(f"  Header entfernt (Fallback bei: '{marker}')")
                break

    # ----------------------------------------------------------
    # STUFE 2: Footer abschneiden
    # Alles nach dem letzten Dialog ist Boilerplate
    # ----------------------------------------------------------
    for marker in FOOTER_MARKERS:
        idx = cleaned.find(marker)
        if idx != -1:
            cleaned = cleaned[:idx]
            print(f"  Footer entfernt (bei: '{marker[:40]}...')")
            break

    # ----------------------------------------------------------
    # STUFE 3: Werbeblöcke entfernen
    # Ad-Reads sind typischerweise 1-3 Sätze, die mit
    # "Let me tell you about..." beginnen.
    # Wir entfernen den gesamten Absatz.
    # ----------------------------------------------------------
    paragraphs = cleaned.split("\n\n")
    filtered_paragraphs = []
    ads_removed = 0

    for para in paragraphs:
        para_stripped = para.strip()
        if not para_stripped:
            continue
        if AD_REGEX.search(para_stripped):
            ads_removed += 1
            continue
        filtered_paragraphs.append(para_stripped)

    cleaned = "\n\n".join(filtered_paragraphs)
    print(f"  {ads_removed} Werbeblöcke entfernt")

    # ----------------------------------------------------------
    # STUFE 4: Sponsor-Link-Zeilen entfernen
    # "Ramp - https://Ramp.com" etc.
    # ----------------------------------------------------------
    sponsor_count = len(SPONSOR_LINK_REGEX.findall(cleaned))
    cleaned = SPONSOR_LINK_REGEX.sub("", cleaned)
    if sponsor_count:
        print(f"  {sponsor_count} Sponsor-Links entfernt")

    # ----------------------------------------------------------
    # STUFE 5: Timestamps entfernen
    # ----------------------------------------------------------
    cleaned = re.sub(r'Starting point is \d{2}:\d{2}:\d{2}', '', cleaned)
    cleaned = re.sub(r'\(\d{2}:\d{2}:\d{2}\)', '', cleaned)

    # ----------------------------------------------------------
    # STUFE 6: Bekannte Transkriptions-Fehler korrigieren
    # (erweitere diese Liste, wenn dir neue auffallen)
    # ----------------------------------------------------------
    replacements = {
        "TVPN": "TBPN",
        "Grogopedia": "Grokopedia",
        "Quen-3": "Qwen-3",
        "Aerobor": "Arabor",
        "Aribor": "Arabor",
        "Air Force": "Arabor",      # Häufiger Transkriptionsfehler
        "Airborne": "Arabor",        # Häufiger Transkriptionsfehler
        "Paul Murlocki": "Palmer Luckey",
        "terrorists": "tariffs",     # Häufiger Speech-to-Text-Fehler
        "Jennifer Duden": "Jennifer Doudna",
    }
    for wrong, right in replacements.items():
        if wrong in cleaned:
            count = cleaned.count(wrong)
            cleaned = cleaned.replace(wrong, right)
            print(f"  Korrektur: '{wrong}' → '{right}' ({count}x)")

    # ----------------------------------------------------------
    # STUFE 7: Leerzeichen und Zeilenumbrüche normalisieren
    # ----------------------------------------------------------
    # Sinnlose einzelne Zeilenumbrüche zu Leerzeichen
    cleaned = re.sub(r'(?<!\n)\n(?!\n)', ' ', cleaned)
    # Mehr als 2 Leerzeilen auf 2 reduzieren
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    # Mehrfache Leerzeichen
    cleaned = re.sub(r' +', ' ', cleaned)

    cleaned = cleaned.strip()
    print(f"  Fertiger Text: {len(cleaned)} Zeichen")
    return cleaned


# ============================================================
# 2. SEGMENT-MARKER (optional, aber hilfreich für Gemini)
# ============================================================
# Fügt Trennlinien ein, wenn ein neuer Gast begrüßt wird.
# Das hilft Gemini, Segmente besser zu erkennen.
# ============================================================

GUEST_PATTERNS = [
    r"[Ll]et'?s bring (?:him|her|them) in",
    r"[Ww]e have .{2,40} (?:joining|in the .{0,20}waiting room)",
    r"[Ll]et'?s bring in .{2,40}",
    r"[Hh]ow are you doing\?",  # Typische Gast-Begrüßung
]
GUEST_REGEX = re.compile("|".join(GUEST_PATTERNS))


def add_segment_markers(text):
    """
    Fügt '---' Trennlinien vor Gast-Wechseln ein.
    Das gibt Gemini visuelle Hinweise auf Segmentgrenzen.
    """
    lines = text.split("\n\n")
    result = []
    markers_added = 0

    for i, para in enumerate(lines):
        if GUEST_REGEX.search(para) and i > 0:
            result.append("\n---\n")
            markers_added += 1
        result.append(para)

    if markers_added:
        print(f"  {markers_added} Segment-Marker eingefügt")
    return "\n\n".join(result)


# ============================================================
# 3. METADATEN-HEADER
# ============================================================
# Gibt Gemini Kontext über die Episode direkt am Anfang.
# ============================================================

def build_header(title, url, date_str, char_count):
    """Erstellt einen strukturierten Header für das Transkript."""
    return (
        f"=== PODCAST-TRANSKRIPT ===\n"
        f"Titel: {title}\n"
        f"Quelle: {url}\n"
        f"Datum: {date_str}\n"
        f"Länge: ~{char_count // 1000}k Zeichen\n"
        f"Hinweis: Werbeblöcke wurden entfernt. '---' markiert Gast-Wechsel.\n"
        f"===========================\n\n"
    )


# ============================================================
# 4. HAUPT-SCRAPER
# ============================================================

def scrape_latest():
    print("Starte unsichtbaren Browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)
        page.wait_for_load_state('networkidle')

        soup = BeautifulSoup(page.content(), 'html.parser')
        all_links = soup.find_all('a', href=True)

        # Alle potenziellen Links sammeln
        episode_links = []
        for link in all_links:
            href = link.get('href', '')
            if (href.startswith("/podcasts/tbpn-live/")
                    and len(href) > len("/podcasts/tbpn-live/")
                    and "page=" not in href):
                if "diet" not in href.lower():
                    episode_links.append(href)

        final_text = None
        final_title = None
        final_url = None

        # Links nacheinander prüfen, bis eine lange Folge gefunden wird
        for link in episode_links:
            ep_url = DOMAIN + link if link.startswith('/') else link
            print(f"Prüfe Folge: {ep_url}")

            page.goto(ep_url)
            page.wait_for_load_state('networkidle')

            # Klicke auf alle "Read More" Buttons
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

            # Navigationselemente entfernen
            for element in ep_soup(["nav", "footer", "header", "script", "style"]):
                element.decompose()

            raw_text = ep_soup.get_text(separator='\n\n', strip=True)

            # === NEU: Erweiterte Reinigung ===
            clean_text = clean_transcript(raw_text)
            clean_text = add_segment_markers(clean_text)

            # Nur Voll-Episoden (> 50.000 Zeichen)
            if len(clean_text) > 50000:
                print(f"BINGO! Lange Voll-Episode gefunden ({len(clean_text)} Zeichen).")
                final_text = clean_text
                final_title = (ep_soup.find('h1').get_text(strip=True)
                               if ep_soup.find('h1') else "Unbekannter Titel")
                final_url = ep_url
                break
            else:
                print(f"Zu kurz ({len(clean_text)} Zeichen). Bonusfolge? Suche weiter...")

        browser.close()

    # Datei speichern
    if final_text:
        date_str = datetime.date.today().strftime("%Y-%m-%d")

        # Header mit Metadaten voranstellen
        header = build_header(final_title, final_url, date_str, len(final_text))
        output = header + final_text

        for fname in [f"Transcript_{date_str}.txt", "latest.txt"]:
            with open(fname, "w", encoding="utf-8") as f:
                f.write(output)
        print(f"Erfolg! latest.txt aktualisiert ({len(output)} Zeichen).")
    else:
        print("Fehler: Keine ausreichend lange Episode gefunden.")


if __name__ == "__main__":
    scrape_latest()
