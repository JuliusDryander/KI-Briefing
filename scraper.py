import datetime
import json
import os
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET

import requests
from google import genai
from google.genai import types

PROCESSED_FILE = "processed.json"
GEMINI_MODEL = "gemini-2.5-flash-preview-05-20"

# ============================================================
# PODCAST-QUELLEN KONFIGURATION (RSS-basiert)
# ============================================================

SOURCES = [
    {
        "name": "TBPN",
        "rss_url": "https://feeds.transistor.fm/technology-brother",
        "min_duration_minutes": 45,  # Mindestlänge um Diet-Episoden zu filtern
        "exclude_title": ["diet"],   # Titel-Filter (case-insensitive)
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
        "rss_url": "https://allinchamathjason.libsyn.com/rss",
        "min_duration_minutes": 30,
        "exclude_title": [],
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
    #     "rss_url": "https://feeds.megaphone.fm/...",
    #     "min_duration_minutes": 15,
    #     "exclude_title": [],
    #     "corrections": {},
    # },
    # -------------------------------------------------------
]


# ============================================================
# DUPLIKAT-ERKENNUNG
# ============================================================

def load_processed():
    """Lädt die Liste bereits verarbeiteter Episode-GUIDs pro Quelle."""
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_processed(processed):
    """Speichert die Liste verarbeiteter Episode-GUIDs."""
    with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=2, ensure_ascii=False)


# ============================================================
# RSS FEED PARSING
# ============================================================

def parse_duration(duration_str):
    """Parst verschiedene Dauer-Formate und gibt Minuten zurück."""
    if not duration_str:
        return 0
    # Format: HH:MM:SS oder MM:SS
    parts = duration_str.strip().split(":")
    try:
        if len(parts) == 3:
            return int(parts[0]) * 60 + int(parts[1]) + int(parts[2]) / 60
        elif len(parts) == 2:
            return int(parts[0]) + int(parts[1]) / 60
        else:
            return int(parts[0]) / 60  # Sekunden
    except ValueError:
        return 0


def get_latest_episode(source):
    """
    Holt den RSS-Feed und gibt die neueste passende Episode zurück.
    Returns: dict mit {guid, title, audio_url, duration_min, pub_date} oder None
    """
    name = source["name"]
    rss_url = source["rss_url"]
    exclude_title = source.get("exclude_title", [])
    min_duration = source.get("min_duration_minutes", 0)

    print(f"  [{name}] Lade RSS-Feed: {rss_url}")

    try:
        resp = requests.get(rss_url, timeout=30, headers={
            "User-Agent": "KI-Briefing-Bot/1.0"
        })
        resp.raise_for_status()
    except Exception as e:
        print(f"  [{name}] FEHLER beim Laden des RSS-Feeds: {e}")
        return None

    # XML parsen
    try:
        root = ET.fromstring(resp.content)
    except ET.ParseError as e:
        print(f"  [{name}] FEHLER beim Parsen des RSS-Feeds: {e}")
        return None

    # Namespaces für iTunes-Tags
    ns = {
        "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        "content": "http://purl.org/rss/1.0/modules/content/",
    }

    channel = root.find("channel")
    if channel is None:
        print(f"  [{name}] Kein <channel> im Feed gefunden.")
        return None

    for item in channel.findall("item"):
        title_el = item.find("title")
        title = title_el.text.strip() if title_el is not None and title_el.text else ""

        # Titel-Filter: Diet-Episoden etc. ausschließen
        skip = False
        for ex in exclude_title:
            if ex.lower() in title.lower():
                print(f"  [{name}] Überspringe (Titel-Filter '{ex}'): {title[:60]}")
                skip = True
                break
        if skip:
            continue

        # Audio-URL aus <enclosure>
        enclosure = item.find("enclosure")
        if enclosure is None:
            continue
        audio_url = enclosure.get("url", "")
        if not audio_url:
            continue

        # Dauer prüfen
        duration_el = item.find("itunes:duration", ns)
        duration_str = duration_el.text if duration_el is not None else ""
        duration_min = parse_duration(duration_str)

        if min_duration > 0 and duration_min < min_duration:
            print(f"  [{name}] Überspringe (zu kurz: {duration_min:.0f} Min): {title[:60]}")
            continue

        # GUID für Duplikat-Check
        guid_el = item.find("guid")
        guid = guid_el.text.strip() if guid_el is not None and guid_el.text else audio_url

        # Datum
        pub_date_el = item.find("pubDate")
        pub_date = pub_date_el.text.strip() if pub_date_el is not None and pub_date_el.text else ""

        print(f"  [{name}] Neueste Episode: {title[:80]}")
        print(f"  [{name}] Dauer: {duration_min:.0f} Min | Datum: {pub_date[:25]}")

        return {
            "guid": guid,
            "title": title,
            "audio_url": audio_url,
            "duration_min": duration_min,
            "pub_date": pub_date,
        }

    print(f"  [{name}] Keine passende Episode im Feed gefunden.")
    return None


# ============================================================
# AUDIO DOWNLOAD
# ============================================================

def download_audio(audio_url, name):
    """Lädt die MP3-Datei herunter. Gibt den Dateipfad zurück."""
    print(f"  [{name}] Lade Audio herunter: {audio_url[:80]}...")

    suffix = ".mp3"
    if ".m4a" in audio_url:
        suffix = ".m4a"
    elif ".wav" in audio_url:
        suffix = ".wav"

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


# ============================================================
# GEMINI TRANSKRIPTION
# ============================================================

def transcribe_with_gemini(audio_path, source):
    """
    Sendet die Audio-Datei an Gemini und bekommt ein Transkript zurück.
    Gibt den transkribierten Text zurück.
    """
    name = source["name"]
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(f"  [{name}] FEHLER: GEMINI_API_KEY nicht gesetzt!")
        return None

    client = genai.Client(api_key=api_key)

    print(f"  [{name}] Lade Audio zu Gemini hoch...")

    # Datei hochladen via Files API (für große Dateien)
    try:
        uploaded_file = client.files.upload(file=audio_path)
        print(f"  [{name}] Upload erfolgreich: {uploaded_file.name}")
    except Exception as e:
        print(f"  [{name}] FEHLER beim Upload: {e}")
        return None

    # Warten bis Datei verarbeitet ist
    import time
    max_wait = 300  # 5 Minuten max warten
    waited = 0
    while waited < max_wait:
        file_info = client.files.get(name=uploaded_file.name)
        if file_info.state.name == "ACTIVE":
            break
        print(f"  [{name}] Warte auf Verarbeitung... ({waited}s)")
        time.sleep(10)
        waited += 10

    if file_info.state.name != "ACTIVE":
        print(f"  [{name}] FEHLER: Datei nicht rechtzeitig verarbeitet (Status: {file_info.state.name})")
        return None

    # Transkription anfordern
    print(f"  [{name}] Starte Transkription...")

    prompt = """Transcribe this podcast episode completely and accurately.

Requirements:
- Transcribe ALL speech content from start to finish
- Identify speakers where possible (e.g., "Speaker 1:", "John:", etc.)
- Include timestamps every 5-10 minutes in format [MM:SS]
- Transcribe in the original language (English)
- Preserve all proper nouns, company names, and technical terms accurately
- Do NOT summarize - provide the full verbatim transcript
- Skip ad reads and sponsor segments if clearly identifiable
"""

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
                        types.Part.from_text(text=prompt),
                    ]
                )
            ],
            config=types.GenerateContentConfig(
                max_output_tokens=65536,
                temperature=0.1,
            ),
        )

        transcript = response.text
        print(f"  [{name}] Transkription erhalten: {len(transcript)} Zeichen")

        # Cleanup: Datei bei Gemini löschen
        try:
            client.files.delete(name=uploaded_file.name)
        except Exception:
            pass

        return transcript

    except Exception as e:
        print(f"  [{name}] FEHLER bei Transkription: {e}")
        return None


# ============================================================
# TEXT-BEREINIGUNG
# ============================================================

AD_PATTERNS = [
    r"Let me (?:also )?tell you about\b",
    r"And let me (?:also )?tell you about\b",
    r"While .{0,30} let me tell you about\b",
    r"I'm (?:also )?going to tell you about\b",
    r"is made possible by\b",
    r"is brought to you by\b",
    r"is sponsored by\b",
    r"Our presenting sponsor\b",
    r"Today's episode is powered by\b",
]
AD_REGEX = re.compile("|".join(AD_PATTERNS), re.IGNORECASE)

GUEST_PATTERNS = [
    r"[Ll]et'?s bring (?:him|her|them) in",
    r"[Ww]e have .{2,40} (?:joining|in the .{0,20}waiting room)",
    r"[Ll]et'?s bring in .{2,40}",
]
GUEST_REGEX = re.compile("|".join(GUEST_PATTERNS))


def clean_transcript(text, source):
    """Bereinigt ein Transkript basierend auf der Quellen-Konfiguration."""
    name = source["name"]
    corrections = source.get("corrections", {})
    print(f"  [{name}] Starte Text-Reinigung...")
    cleaned = text

    # Werbeblöcke entfernen
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

    # Podcast-spezifische Korrekturen
    for wrong, right in corrections.items():
        if wrong in cleaned:
            count = cleaned.count(wrong)
            cleaned = cleaned.replace(wrong, right)
            print(f"  [{name}] Korrektur: '{wrong}' → '{right}' ({count}x)")

    # Normalisierung
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


def build_header(title, audio_url, name, date_str, char_count):
    """Metadaten-Header für ein Transkript."""
    return (
        f"=== PODCAST-TRANSKRIPT: {name} ===\n"
        f"Titel: {title}\n"
        f"Quelle: {audio_url[:80]}...\n"
        f"Datum: {date_str}\n"
        f"Länge: ~{char_count // 1000}k Zeichen\n"
        f"Hinweis: Werbung entfernt. '---' markiert Gast-Wechsel.\n"
        f"Transkription: Gemini AI (automatisch)\n"
        f"{'=' * 40}\n\n"
    )


# ============================================================
# HAUPTLOGIK
# ============================================================

def scrape_all():
    """Verarbeitet alle konfigurierten Quellen via RSS + Gemini."""
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    processed = load_processed()

    results = []

    for source in SOURCES:
        name = source["name"]
        print(f"\n{'='*50}")
        print(f"Prüfe: {name}")
        print(f"{'='*50}")

        # 1. Neueste Episode aus RSS-Feed
        episode = get_latest_episode(source)
        if not episode:
            print(f"  [{name}] Keine Episode gefunden.")
            continue

        # 2. Duplikat-Check
        if processed.get(name) == episode["guid"]:
            print(f"  [{name}] ⏭️  Bereits verarbeitet: {episode['title'][:50]}...")
            print(f"  [{name}] Keine neue Episode seit letztem Lauf.")
            continue

        print(f"  [{name}] 🆕 Neue Episode: {episode['title'][:60]}")

        # 3. Audio herunterladen
        audio_path = download_audio(episode["audio_url"], name)
        if not audio_path:
            continue

        try:
            # 4. Mit Gemini transkribieren
            transcript = transcribe_with_gemini(audio_path, source)
            if not transcript:
                continue

            # 5. Transkript bereinigen
            clean_text = clean_transcript(transcript, source)
            clean_text = add_segment_markers(clean_text)

            if len(clean_text) > 5000:  # Mindestlänge für gültiges Transkript
                header = build_header(
                    episode["title"], episode["audio_url"],
                    name, date_str, len(clean_text)
                )
                results.append({
                    "name": name,
                    "title": episode["title"],
                    "guid": episode["guid"],
                    "content": header + clean_text,
                })
                # Als verarbeitet markieren
                processed[name] = episode["guid"]
            else:
                print(f"  [{name}] Transkript zu kurz ({len(clean_text)} Zeichen)")

        finally:
            # Temp-Datei aufräumen
            if os.path.exists(audio_path):
                os.unlink(audio_path)

    # Processed-Datei aktualisieren
    save_processed(processed)

    if not results:
        print("\nKeine neuen Episoden gefunden. Briefing wird nicht aktualisiert.")
        return False

    # ---------------------------------------------------------
    # EINZELNE DATEIEN pro Quelle (für Archiv)
    # ---------------------------------------------------------
    for r in results:
        fname = f"Transcript_{r['name']}_{date_str}.txt"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(r["content"])
        print(f"Gespeichert: {fname}")

    # ---------------------------------------------------------
    # KOMBINIERTE DATEI für Gemini (latest.txt)
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

    return True


if __name__ == "__main__":
    scrape_all()
