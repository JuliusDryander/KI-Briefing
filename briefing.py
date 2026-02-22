"""
briefing.py – Erstellt ein Executive Briefing aus Podcast-Transkripten.

Liest latest.txt (vom Scraper), schickt es an die Gemini API,
und speichert das Ergebnis als briefing.md (sauberes Markdown).

Verwendung:
    python briefing.py

Benötigt:
    - GEMINI_API_KEY als Umgebungsvariable
    - latest.txt im selben Verzeichnis
"""

import os
import json
import urllib.request
import urllib.error
import sys

# ============================================================
# KONFIGURATION
# ============================================================

GEMINI_MODEL = "gemini-2.0-flash"
INPUT_FILE = "latest.txt"
OUTPUT_FILE = "briefing.md"
MAX_OUTPUT_TOKENS = 8192
TEMPERATURE = 0.2

# ============================================================
# SYSTEM-PROMPT
# ============================================================

SYSTEM_PROMPT = """Du bist ein Analyst, der aus Podcast-Transkripten Executive Briefings erstellt.

## KRITISCHE REGELN

1. **NUR Informationen aus dem Transkript verwenden.** Du darfst KEIN Hintergrundwissen einbringen, das nicht explizit im Text steht. Wenn etwas im Transkript nicht gesagt wurde, gehört es nicht ins Briefing.
2. **Aussagen korrekt zuordnen.** Wenn unklar ist, wer genau eine These vertritt, schreibe "laut der Diskussion" statt einer falschen Zuordnung.
3. **Nuancen und Einschränkungen bewahren.** Wenn ein Sprecher sagt "vielleicht" oder "ich bin nicht sicher", muss das Briefing diese Unsicherheit widerspiegeln.
4. **Rollen korrekt wiedergeben.** Beschreibe Personen nur mit den Rollen, die im Transkript genannt werden. Erfinde keine Titel oder Gründer-Zuschreibungen.
5. **Quellenangabe bei mehreren Transkripten.** Wenn mehrere Podcast-Quellen vorhanden sind, gib bei jeder These an, aus welcher Quelle sie stammt.

STRENG VERBOTEN: Erwähne KEINE Technologien, Produkte, Kooperationen oder Strategien, die nicht WÖRTLICH im Transkript vorkommen. Insbesondere: Erfinde keine Finanzprodukte (z.B. Stablecoins, Krypto-Settlement), keine Behörden-Kooperationen und keine Gründer-Zuschreibungen, die nicht explizit im Transkript stehen.

## ANALYSE-PROZESS

### Schritt 1: Segmentierung
Identifiziere alle inhaltlichen Segmente der Episode(n). Liste sie intern auf mit:
- Sprecher
- Kernthema
- Geschätzte Relevanz (hoch/mittel/niedrig)

### Schritt 2: Auswahl
Wähle die 3-5 relevantesten Segmente aus. Kriterien:
- Strategische/wirtschaftliche Tragweite
- Neuigkeitswert (neue Ankündigungen, Regulierungen, Marktbewegungen)
- Handlungsrelevanz für Entscheider
- Ignoriere: Smalltalk, Werbung, Memes, Real Estate, Lifestyle-Segmente

### Schritt 3: Extraktion mit Quelltreue
Für jedes gewählte Segment, extrahiere:
- **Zentrale These** – in einem Satz, eng am Wortlaut des Sprechers
- **Belege/Details** – konkrete Zahlen, Beispiele, Unternehmen, die genannt wurden
- **Einschränkungen** – was der Sprecher NICHT behauptet oder wo er unsicher war
- **Fehlende Sprecher** – wurden im selben Themenblock weitere Personen interviewt?

## OUTPUT-FORMAT

Antworte ausschließlich in reinem Markdown. Kein JSON. Kein Wrapper. Beginne direkt mit dem ersten Heading.

---

# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| [Thema 1] | [1 Satz, eng am Transkript] | [Name, Rolle wie im Transkript] | [Podcast-Name] |
| [Thema 2] | ... | ... | ... |

# 🎙 Deep-Dive: Die Kern-Analysen

## [Emoji] [Thema 1]: [Überschrift]

[Name] ([Rolle/Firma wie im Transkript]) [Zusammenfassung der Position, 3-5 Sätze].

**Konkrete Details aus dem Gespräch:**
- [Fakt/Zahl/Beispiel 1]
- [Fakt/Zahl/Beispiel 2]
- [Fakt/Zahl/Beispiel 3]

**Einschränkungen/Offene Fragen:**
- [Was der Sprecher nicht behauptet hat oder wo Unsicherheit besteht]

## 📌 Weitere bemerkenswerte Segmente

[Kurze Erwähnung von 2-3 Themen, die es nicht in den Deep-Dive geschafft haben – jeweils 1-2 Sätze]

# 💡 LinkedIn-Potenzial

**Hook 1:** [Aufmerksamkeitsstarker Einstieg]
- Inhalt: [2-3 Sätze]
- Call-to-Action: [Frage an die Community]

**Hook 2:** [Aufmerksamkeitsstarker Einstieg]
- Inhalt: [2-3 Sätze]
- Call-to-Action: [Frage an die Community]

---

## QUALITÄTS-CHECKLISTE (intern durchgehen vor Output)

Bevor du antwortest, prüfe:
- [ ] Steht JEDE Behauptung so im Transkript? Wenn nein → streichen
- [ ] Sind alle Personen mit der richtigen Rolle/Firma beschrieben?
- [ ] Habe ich pro Thema auch erwähnt, was der Sprecher NICHT gesagt hat?
- [ ] Sind wichtige Gesprächspartner berücksichtigt?
- [ ] Enthält der Output KEINE Informationen aus meinem Vorwissen?
- [ ] Bei mehreren Quellen: Ist jede These einer Quelle zugeordnet?
"""

USER_PROMPT_TEMPLATE = """Erstelle ein Executive Briefing aus dem folgenden Podcast-Transkript:

{transcript}"""


# ============================================================
# GEMINI API CALL
# ============================================================

def call_gemini(transcript_text):
    """Ruft die Gemini API auf und gibt den Antwort-Text zurück."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("FEHLER: GEMINI_API_KEY nicht gesetzt!")
        sys.exit(1)

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?key={api_key}"
    )

    user_message = USER_PROMPT_TEMPLATE.format(transcript=transcript_text)

    payload = {
        "systemInstruction": {
            "parts": [{"text": SYSTEM_PROMPT}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_message}]
            }
        ],
        "generationConfig": {
            "temperature": TEMPERATURE,
            "maxOutputTokens": MAX_OUTPUT_TOKENS,
        },
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    print(f"Sende {len(transcript_text)} Zeichen an Gemini ({GEMINI_MODEL})...")

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"FEHLER: Gemini API HTTP {e.code}")
        print(error_body)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"FEHLER: Gemini API nicht erreichbar: {e.reason}")
        sys.exit(1)

    # Text aus der Antwort extrahieren
    try:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError) as e:
        print(f"FEHLER: Unerwartetes Antwortformat: {e}")
        print(json.dumps(result, indent=2)[:500])
        sys.exit(1)

    print(f"Antwort erhalten: {len(text)} Zeichen")
    return text


# ============================================================
# MAIN
# ============================================================

def main():
    # 1. Transkript lesen
    if not os.path.exists(INPUT_FILE):
        print(f"FEHLER: {INPUT_FILE} nicht gefunden!")
        sys.exit(1)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        transcript = f.read()

    print(f"Transkript geladen: {len(transcript)} Zeichen")

    # 2. Gemini aufrufen
    briefing = call_gemini(transcript)

    # 3. Sauberes Markdown speichern (kein JSON, keine \n-Literale)
    # Falls Gemini trotzdem JSON-Wrapper liefert, entfernen:
    if briefing.startswith('{"data":"'):
        briefing = briefing[len('{"data":"'):]
        if briefing.endswith('"}'):
            briefing = briefing[:-2]
        # \n-Literale durch echte Zeilenumbrüche ersetzen
        briefing = briefing.replace("\\n", "\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(briefing)

    print(f"Briefing gespeichert: {OUTPUT_FILE} ({len(briefing)} Zeichen)")


if __name__ == "__main__":
    main()
