"""
scraper.py – Hybrid-Scraper für Podcast-Transkripte

PRIMÄR:   Podscripts.co → fertiges Transkript scrapen
FALLBACK: RSS-Feed → MP3 downloaden → Gemini erstellt Briefing direkt aus Audio

Wenn Podscripts ein Transkript hat, wird es wie bisher verwendet (bewährte Qualität).
Wenn Podscripts ausfällt, wird die Episode via RSS als Audio geholt und Gemini
erstellt das Briefing direkt aus dem Audio (kein Zwischen-Transkript).
"""

import datetime
import json
import os
import re
import tempfile
import time
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

DOMAIN = "https://podscripts.co"
PROCESSED_FILE = "processed.json"
GEMINI_MODEL = "gemini-2.5-flash"

# Flag-Datei: Signalisiert briefing.py, dass das Briefing schon fertig ist
BRIEFING_FROM_AUDIO_FLAG = "briefing_from_audio.flag"

# ============================================================
# PODCAST-QUELLEN KONFIGURATION
# ============================================================

SOURCES = [
    {
        "name": "TBPN",
        # Podscripts (primär)
        "podscripts_url": "https://podscripts.co/podcasts/tbpn-live/",
        "min_chars": 50000,
        "exclude": ["diet"],
        # RSS (Fallback)
        "rss_url": "https://feeds.transistor.fm/technology-brother",
        "min_duration_minutes": 45,
        "exclude_title": ["diet"],
        # Gemeinsam
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
        # Podscripts (primär)
        "podscripts_url": "https://podscripts.co/podcasts/all-in-with-chamath-jason-sacks-friedberg/",
        "min_chars": 30000,
        "exclude": [],
        # RSS (Fallback)
        "rss_url": "https://allinchamathjason.libsyn.com/rss",
        "min_duration_minutes": 30,
        "exclude_title": [],
        # Gemeinsam
        "corrections": {
            "Jamath": "Chamath",
            "Chamat ": "Chamath ",
            "Freedberg": "Friedberg",
            "Sax ": "Sacks ",
        },
    },
]


# ============================================================
# DUPLIKAT-ERKENNUNG
# ============================================================

def load_processed():
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_processed(processed):
    with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=2, ensure_ascii=False)


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
    r"^.{1,60}\s*[-\u2013\u2014]\s*https?://\S+$", re.MULTILINE
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
# CLEANING FUNCTIONS (für Podscripts-Transkripte)
# ============================================================

def clean_transcript(raw_text, source):
    name = source["name"]
    corrections = source.get("corrections", {})
    print(f"  [{name}] Starte Text-Reinigung...")
    cleaned = raw_text

    markers = TRANSCRIPT_START_MARKERS.get(name, TRANSCRIPT_START_MARKERS["_default"])
    for marker in markers:
        idx = cleaned.find(marker)
        if idx != -1:
            cleaned = cleaned[idx:]
            print(f"  [{name}] Header entfernt (bei: '{marker[:30]}...')")
            break

    for marker in FOOTER_MARKERS:
        idx = cleaned.find(marker)
        if idx != -1:
            cleaned = cleaned[:idx]
            print(f"  [{name}] Footer entfernt")
            break

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

    cleaned = SPONSOR_LINK_REGEX.sub("", cleaned)
    cleaned = re.sub(r'Starting point is \d{2}:\d{2}:\d{2}', '', cleaned)
    cleaned = re.sub(r'\(\d{2}:\d{2}:\d{2}\)', '', cleaned)

    for wrong, right in corrections.items():
        if wrong in cleaned:
            count = cleaned.count(wrong)
            cleaned = cleaned.replace(wrong, right)
            print(f"  [{name}] Korrektur: '{wrong}' → '{right}' ({count}x)")

    cleaned = re.sub(r'(?<!\n)\n(?!\n)', ' ', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    cleaned = re.sub(r' +', ' ', cleaned)
    cleaned = cleaned.strip()

    print(f"  [{name}] Fertig: {len(cleaned)} Zeichen")
    return cleaned


def add_segment_markers(text):
    lines = text.split("\n\n")
    result = []
    for i, para in enumerate(lines):
        if GUEST_REGEX.search(para) and i > 0:
            result.append("\n---\n")
        result.append(para)
    return "\n\n".join(result)


def build_header(title, url, name, date_str, char_count, method="Podscripts"):
    return (
        f"=== PODCAST-TRANSKRIPT: {name} ===\n"
        f"Titel: {title}\n"
        f"Quelle: {url}\n"
        f"Datum: {date_str}\n"
        f"Länge: ~{char_count // 1000}k Zeichen\n"
        f"Hinweis: Werbeblöcke entfernt. '---' markiert Gast-Wechsel.\n"
        f"Methode: {method}\n"
        f"{'=' * 40}\n\n"
    )


# ============================================================
# PODSCRIPTS SCRAPER (PRIMÄR)
# ============================================================

def find_latest_episode_url(page, source):
    base_url = source["podscripts_url"]
    exclude = source.get("exclude", [])

    page.goto(base_url)
    page.wait_for_load_state('networkidle')

    soup = BeautifulSoup(page.content(), 'html.parser')
    all_links = soup.find_all('a', href=True)

    base_path = base_url.replace(DOMAIN, "")
    for link in all_links:
        href = link.get('href', '')
        link_text = link.get_text(strip=True).lower()
        if (href.startswith(base_path)
                and len(href) > len(base_path)
                and "page=" not in href):
            if not any(ex.lower() in href.lower() or ex.lower() in link_text
                       for ex in exclude):
                return DOMAIN + href if href.startswith('/') else href
    return None


def scrape_episode(page, source, ep_url):
    name = source["name"]
    min_chars = source["min_chars"]

    print(f"  [{name}] Scrape Podscripts: {ep_url}")

    page.goto(ep_url)
    page.wait_for_load_state('networkidle')

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
    clean_text = clean_transcript(raw_text, source)
    clean_text = add_segment_markers(clean_text)

    if len(clean_text) > min_chars:
        title = (ep_soup.find('h1').get_text(strip=True)
                 if ep_soup.find('h1') else "Unbekannter Titel")
        print(f"  [{name}] ✅ Podscripts-Transkript gefunden! ({len(clean_text)} Zeichen)")
        return title, clean_text
    else:
        print(f"  [{name}] ⚠️  Podscripts zu kurz ({len(clean_text)} Zeichen)")
        return None


# ============================================================
# RSS FEED PARSING (für Fallback)
# ============================================================

def parse_duration(duration_str):
    if not duration_str:
        return 0
    parts = duration_str.strip().split(":")
    try:
        if len(parts) == 3:
            return int(parts[0]) * 60 + int(parts[1]) + int(parts[2]) / 60
        elif len(parts) == 2:
            return int(parts[0]) + int(parts[1]) / 60
        else:
            return int(parts[0]) / 60
    except ValueError:
        return 0


def get_latest_rss_episode(source):
    name = source["name"]
    rss_url = source.get("rss_url")
    if not rss_url:
        return None

    exclude_title = source.get("exclude_title", [])
    min_duration = source.get("min_duration_minutes", 0)

    print(f"  [{name}] 🔄 Fallback: Lade RSS-Feed...")

    try:
        resp = requests.get(rss_url, timeout=30, headers={
            "User-Agent": "KI-Briefing-Bot/1.0"
        })
        resp.raise_for_status()
    except Exception as e:
        print(f"  [{name}] FEHLER beim RSS-Feed: {e}")
        return None

    try:
        root = ET.fromstring(resp.content)
    except ET.ParseError as e:
        print(f"  [{name}] FEHLER beim Parsen: {e}")
        return None

    ns = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}
    channel = root.find("channel")
    if channel is None:
        return None

    for item in channel.findall("item"):
        title_el = item.find("title")
        title = title_el.text.strip() if title_el is not None and title_el.text else ""

        skip = False
        for ex in exclude_title:
            if ex.lower() in title.lower():
                skip = True
                break
        if skip:
            continue

        enclosure = item.find("enclosure")
        if enclosure is None:
            continue
        audio_url = enclosure.get("url", "")
        if not audio_url:
            continue

        duration_el = item.find("itunes:duration", ns)
        duration_str = duration_el.text if duration_el is not None else ""
        duration_min = parse_duration(duration_str)

        if min_duration > 0 and duration_min < min_duration:
            continue

        guid_el = item.find("guid")
        guid = guid_el.text.strip() if guid_el is not None and guid_el.text else audio_url

        print(f"  [{name}] RSS-Episode: {title[:70]}")
        print(f"  [{name}] Dauer: {duration_min:.0f} Min")

        return {
            "guid": guid,
            "title": title,
            "audio_url": audio_url,
            "duration_min": duration_min,
        }

    return None


# ============================================================
# AUDIO DOWNLOAD + GEMINI BRIEFING (Fallback)
# ============================================================

def download_audio(audio_url, name):
    print(f"  [{name}] Lade Audio herunter...")

    suffix = ".mp3"
    if ".m4a" in audio_url:
        suffix = ".m4a"

    tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    tmp_path = tmp.name
    tmp.close()

    try:
        resp = requests.get(audio_url, timeout=600, stream=True, headers={
            "User-Agent": "KI-Briefing-Bot/1.0"
        })
        resp.raise_for_status()

        total = 0
        with open(tmp_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=1024 * 1024):
                f.write(chunk)
                total += len(chunk)

        size_mb = total / (1024 * 1024)
        print(f"  [{name}] Download fertig: {size_mb:.1f} MB")
        return tmp_path

    except Exception as e:
        print(f"  [{name}] FEHLER beim Download: {e}")
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        return None


def briefing_from_audio(audio_path, source):
    """
    Erstellt ein Briefing DIREKT aus dem Audio.
    Kein Transkript als Zwischenschritt – Gemini analysiert das Audio
    und gibt direkt das fertige Briefing zurück.
    """
    from google import genai
    from google.genai import types

    name = source["name"]
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(f"  [{name}] FEHLER: GEMINI_API_KEY nicht gesetzt!")
        return None

    client = genai.Client(api_key=api_key)

    print(f"  [{name}] Lade Audio zu Gemini hoch...")
    try:
        uploaded_file = client.files.upload(file=audio_path)
        print(f"  [{name}] Upload erfolgreich: {uploaded_file.name}")
    except Exception as e:
        print(f"  [{name}] FEHLER beim Upload: {e}")
        return None

    max_wait = 300
    waited = 0
    while waited < max_wait:
        file_info = client.files.get(name=uploaded_file.name)
        if file_info.state.name == "ACTIVE":
            break
        print(f"  [{name}] Warte auf Verarbeitung... ({waited}s)")
        time.sleep(10)
        waited += 10

    if file_info.state.name != "ACTIVE":
        print(f"  [{name}] FEHLER: Datei nicht verarbeitet")
        return None

    eu_context = ""
    if os.path.exists("eu_context.md"):
        with open("eu_context.md", "r", encoding="utf-8") as f:
            eu_context = f.read()
        print(f"  [{name}] EU-Kontext geladen: {len(eu_context)} Zeichen")

    system_prompt = """Du bist ein Analyst, der aus Podcast-Audio Executive Briefings erstellt.

## KRITISCHE REGELN

1. **NUR Informationen aus dem Audio verwenden.** Kein Hintergrundwissen einbringen.
2. **Aussagen korrekt zuordnen.** Bei Unsicherheit: "laut der Diskussion".
3. **Nuancen bewahren.** Unsicherheiten der Sprecher im Briefing abbilden.
4. **Rollen korrekt wiedergeben.** Nur im Audio genannte Rollen verwenden.
5. **Werbung und Sponsor-Segmente ignorieren.**

PRIORITÄTSREIHENFOLGE:
1. Wirtschaftspolitik: Zölle, Handelsabkommen, Regulierung
2. Infrastruktur & Energie: Rechenzentren, Kernkraft, Energiepolitik
3. Technologie-Strategie: KI, SaaS-Disruption, Plattform-Dynamiken
4. Finanzwesen & Banking
5. Geopolitik & Industriepolitik

NIEDRIGE PRIORITÄT: Skandale, Klatsch, VR/Gaming, Lifestyle, Smalltalk

## OUTPUT-FORMAT (reines Markdown)

# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| ... | ... | ... | ... |

# 🎙 Deep-Dive: Die Kern-Analysen

## [Emoji] [Thema]: [Überschrift]
[3-5 Sätze Zusammenfassung]

**Konkrete Details aus dem Gespräch:**
- [Fakt/Zahl/Beispiel]

**Einschränkungen/Offene Fragen:**
- [Was nicht behauptet wurde]

**🇪🇺 Europa-Relevanz:** (NUR bei konkretem Bezug)
[1-3 Sätze]

## 📌 Weitere bemerkenswerte Segmente
[2-3 Themen, je 1-2 Sätze]

# 💭 Zum Drüber Nachdenken

**Impuls 1:** [These mit Europa-Bezug]
- Kontext: [2-3 Sätze]
- Die Frage dahinter: [1 Satz]

**Impuls 2:** [These mit Europa-Bezug]
- Kontext: [2-3 Sätze]
- Die Frage dahinter: [1 Satz]
"""

    if eu_context:
        user_prompt = f"""Erstelle ein Executive Briefing aus diesem Podcast-Audio.

Nutze den EU-Kontext für "🇪🇺 Europa-Relevanz" – aber NUR wo ein konkreter Bezug besteht.

=== EU-KONTEXT ===
{eu_context}
=== ENDE EU-KONTEXT ===

Analysiere das Audio und erstelle das Briefing."""
    else:
        user_prompt = "Erstelle ein Executive Briefing aus diesem Podcast-Audio."

    print(f"  [{name}] Erstelle Briefing aus Audio... (kann 5-15 Min dauern)")

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=[
                types.Content(
                    parts=[
                        types.Part.from_uri(
                            file_uri=uploaded_file.uri,
                            mime_type=uploaded_file.mime_type,
                        ),
                        types.Part.from_text(text=user_prompt),
                    ]
                )
            ],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                max_output_tokens=16384,
                temperature=0.2,
            ),
        )

        briefing_text = response.text
        print(f"  [{name}] ✅ Audio-Briefing erhalten: {len(briefing_text)} Zeichen")

        try:
            client.files.delete(name=uploaded_file.name)
        except Exception:
            pass

        return briefing_text

    except Exception as e:
        print(f"  [{name}] FEHLER bei Audio-Briefing: {e}")
        return None


# ============================================================
# HAUPTLOGIK
# ============================================================

def scrape_all():
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    processed = load_processed()

    transcript_results = []
    audio_briefings = []

    # =========================================================
    # PHASE 1: Podscripts versuchen
    # =========================================================
    print("=" * 50)
    print("PHASE 1: Podscripts prüfen")
    print("=" * 50)

    sources_without_transcript = []

    print("\nStarte Browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for source in SOURCES:
            name = source["name"]
            print(f"\n{'='*50}")
            print(f"Prüfe: {name}")
            print(f"{'='*50}")

            latest_url = find_latest_episode_url(page, source)
            if not latest_url:
                print(f"  [{name}] Keine Episode auf Podscripts gefunden.")
                sources_without_transcript.append(source)
                continue

            processed_key = f"{name}_podscripts"
            if processed.get(processed_key) == latest_url:
                print(f"  [{name}] ⏭️  Bereits verarbeitet: {latest_url}")
                continue

            print(f"  [{name}] 🆕 Neue Episode: {latest_url}")

            result = scrape_episode(page, source, latest_url)
            if result:
                title, text = result
                header = build_header(title, latest_url, name, date_str, len(text), "Podscripts")
                transcript_results.append({
                    "name": name,
                    "title": title,
                    "url": latest_url,
                    "content": header + text,
                })
                processed[processed_key] = latest_url
            else:
                print(f"  [{name}] Podscripts-Transkript nicht brauchbar.")
                sources_without_transcript.append(source)

        browser.close()

    # =========================================================
    # PHASE 2: RSS-Fallback
    # =========================================================
    if sources_without_transcript:
        print(f"\n{'='*50}")
        print(f"PHASE 2: RSS-Fallback für {len(sources_without_transcript)} Quelle(n)")
        print(f"{'='*50}")

        for source in sources_without_transcript:
            name = source["name"]
            print(f"\n  [{name}] Versuche RSS-Fallback...")

            episode = get_latest_rss_episode(source)
            if not episode:
                print(f"  [{name}] Auch kein RSS-Ergebnis.")
                continue

            processed_key = f"{name}_rss"
            if processed.get(processed_key) == episode["guid"]:
                print(f"  [{name}] ⏭️  RSS-Episode bereits verarbeitet.")
                continue

            audio_path = download_audio(episode["audio_url"], name)
            if not audio_path:
                continue

            try:
                briefing = briefing_from_audio(audio_path, source)
                if briefing:
                    audio_briefings.append({
                        "name": name,
                        "title": episode["title"],
                        "briefing": briefing,
                    })
                    processed[processed_key] = episode["guid"]
            finally:
                if os.path.exists(audio_path):
                    os.unlink(audio_path)

    # =========================================================
    # ERGEBNISSE SPEICHERN
    # =========================================================
    save_processed(processed)

    has_transcripts = len(transcript_results) > 0
    has_audio_briefings = len(audio_briefings) > 0

    if not has_transcripts and not has_audio_briefings:
        print("\nKeine neuen Episoden gefunden. Briefing wird nicht aktualisiert.")
        return False

    # Podscripts-Transkripte → latest.txt (für briefing.py)
    if has_transcripts:
        for r in transcript_results:
            fname = f"Transcript_{r['name']}_{date_str}.txt"
            with open(fname, "w", encoding="utf-8") as f:
                f.write(r["content"])
            print(f"Gespeichert: {fname}")

        combined_header = (
            f"=== KOMBINIERTES BRIEFING-MATERIAL | {date_str} ===\n"
            f"Quellen: {', '.join(r['name'] for r in transcript_results)}\n"
            f"Anzahl Transkripte: {len(transcript_results)}\n"
            f"Gesamtlänge: ~{sum(len(r['content']) for r in transcript_results) // 1000}k Zeichen\n"
            f"{'=' * 50}\n\n"
            f"WICHTIG FÜR DIE ANALYSE:\n"
            f"- Jedes Transkript ist durch '=== PODCAST-TRANSKRIPT: ...' getrennt\n"
            f"- Verknüpfe Themen ÜBER Quellen hinweg, wenn sie verwandt sind\n"
            f"- Gib bei jeder These an, aus welcher Quelle sie stammt\n\n"
        )
        combined = combined_header + "\n\n".join(r["content"] for r in transcript_results)

        with open("latest.txt", "w", encoding="utf-8") as f:
            f.write(combined)
        print(f"\nlatest.txt aktualisiert ({len(combined)} Zeichen)")

    # Audio-Briefings → direkt als briefing.md
    if has_audio_briefings:
        all_briefings = "\n\n---\n\n".join(b["briefing"] for b in audio_briefings)

        if has_transcripts:
            with open("audio_briefing_supplement.md", "w", encoding="utf-8") as f:
                f.write(all_briefings)
            print(f"Audio-Briefing-Supplement gespeichert")
        else:
            with open("briefing.md", "w", encoding="utf-8") as f:
                f.write(all_briefings)
            print(f"briefing.md direkt aus Audio erstellt")
            with open(BRIEFING_FROM_AUDIO_FLAG, "w") as f:
                f.write("true")

    # Zusammenfassung
    print(f"\n{'='*50}")
    print("ZUSAMMENFASSUNG")
    print(f"{'='*50}")
    for r in transcript_results:
        print(f"  ✅ {r['name']}: {r['title'][:60]}... (Podscripts)")
    for b in audio_briefings:
        print(f"  🎵 {b['name']}: {b['title'][:60]}... (Audio-Briefing)")

    return True


if __name__ == "__main__":
    scrape_all()
