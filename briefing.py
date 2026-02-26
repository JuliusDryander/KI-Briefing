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

GEMINI_MODEL = "gemini-2.5-flash"
INPUT_FILE = "latest.txt"
OUTPUT_FILE = "briefing.md"
EMAIL_OUTPUT_FILE = "briefing_email.html"
MAX_OUTPUT_TOKENS = 65536
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
Wähle die 3-5 relevantesten Segmente aus. Die Zielgruppe sind europäische Entscheider und Führungskräfte.

PRIORITÄTSREIHENFOLGE (höchste zuerst):
1. Wirtschaftspolitik: Zölle, Handelsabkommen, Regulierung, Sanktionen – alles mit Auswirkung auf internationale Märkte
2. Infrastruktur & Energie: Rechenzentren, Kernkraft, Energiepolitik, Kapitalallokation für Infrastruktur
3. Technologie-Strategie: KI-Marktveränderungen, SaaS-Disruption, Plattform-Dynamiken, Capital Markets
4. Finanzwesen & Banking: Neue Finanzinstitutionen, Regulierung, Krypto-Integration
5. Geopolitik & Industriepolitik: US-China, Verteidigung, Industrieförderung

NIEDRIGE PRIORITÄT (nur in "Weitere Segmente"):
- Prominenten-Skandale, Klatsch, persönliche Kontroversen (z.B. Epstein-Diskussionen)
- VR/Gaming/Konsumententechnologie (es sei denn mit klarer Marktrelevanz)
- Lifestyle, Smalltalk, Werbung, Memes, Real Estate

### Schritt 3: Extraktion mit Quelltreue
Für jedes gewählte Segment, extrahiere:
- **Zentrale These** – in einem Satz, eng am Wortlaut des Sprechers
- **Belege/Details** – die wichtigsten konkreten Zahlen, Beispiele, Unternehmen (MAXIMAL 6 Punkte, nur die stärksten)
- **Fehlende Sprecher** – wurden im selben Themenblock weitere Personen interviewt?

WICHTIG: Erstelle KEINEN separaten Abschnitt "Einschränkungen" oder "Offene Fragen". Wenn ein Sprecher relevante Einschränkungen nennt, fließen diese in die "Zum Drüber Nachdenken"-Impulse ein.

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

**Konkrete Details aus dem Gespräch:** (MAXIMAL 6 Punkte)
- [Fakt/Zahl/Beispiel 1]
- [Fakt/Zahl/Beispiel 2]
- ...

**🇪🇺 Europa-Relevanz:** (NUR wenn EU-Kontext bereitgestellt wurde UND ein konkreter Bezug besteht. Wenn kein Bezug → komplett weglassen.)
- [Stichpunkt mit KONKRETEM Policy-Detail: Paragraphen, Fristen, Bußgelder, Zahlen aus dem EU-Kontext]
- [Stichpunkt mit konkretem Akteur/Initiative: Wer in Brüssel/Berlin handelt, welches Instrument greift]
- [Optional: Asymmetrie oder Widerspruch zwischen US- und EU-Ansatz benennen]

QUALITÄTSSTANDARD für Europa-Relevanz (STRIKT EINHALTEN):
- NIEMALS generische Sätze wie "Der EU AI Act reguliert KI umfassend" oder "Die EU fördert KI-Investitionen". Das ist wertlos.
- IMMER spezifisch: Welcher Artikel? Welche Frist? Welches Bußgeld? Welcher Akteur? Welches konkrete Instrument?
- Denke wie ein Policy-Berater, der einem Minister in 30 Sekunden erklärt, warum dieses US-Thema für seine nächste Entscheidung relevant ist.
- Nutze ZAHLEN aus dem EU-Kontext: €-Beträge, Prozentsätze, Deadlines, Chip-Zahlen.
- Benenne PERSONEN und ihre Positionen: Virkkunen, Šefčovič, Merz, Höttges, Schumann – nicht "die EU" oder "Deutschland".
- Zeige SPANNUNGSFELDER: Wo kollidiert das US-Thema mit einer EU-Deadline, einer deutschen Initiative, einem laufenden Gesetzgebungsverfahren?

BEISPIEL für SCHLECHTE Europa-Relevanz:
"Die EU reguliert KI mit dem AI Act und fördert Investitionen durch InvestAI."

BEISPIEL für GUTE Europa-Relevanz:
- Ab Aug 2026 müssen High-Risk-KI-Systeme in der EU vollständig compliant sein – Anthropics Lockerung der Sicherheitsstandards könnte den Wettbewerbsdruck auf EU-konforme Anbieter erhöhen.
- Tim Höttges (Telekom) warnt: Europa nutzt nur 5% der KI-Hochleistungschips vs. 70% in den USA. Das €11-Mrd.-Rechenzentrum Lübbenau (Schwarz Digits) und das Telekom/Nvidia-Projekt München sollen gegensteuern.
- EVP Virkkunen verhandelt den Digital Omnibus, der die High-Risk-Deadline um bis zu 16 Monate verschieben könnte (Backstop: Dez 2027) – ein Zugeständnis an die Industrie bei gleichzeitigem Festhalten an Standards.

## 📌 Weitere bemerkenswerte Segmente

[Kurze Erwähnung von 2-3 Themen, die es nicht in den Deep-Dive geschafft haben – jeweils 1-2 Sätze]

# 💭 Zum Drüber Nachdenken

**[Überspitzte, provokante These als Überschrift – kein neutraler Titel]**
Kontext: [2-3 Sätze, die das US-Thema mit einer KONKRETEN europäischen Implikation verknüpfen. Nenne Akteure, Fristen, Zahlen aus dem EU-Kontext. Hier dürfen auch Einschränkungen und offene Fragen aus dem Podcast einfließen.]
Die Frage dahinter: [1 Satz, zugespitzt – soll beim Leser hängenbleiben]

**[Zweite überspitzte These]**
Kontext: [2-3 Sätze]
Die Frage dahinter: [1 Satz]

WICHTIG für die Impulse:
- GENAU 2 Impulse. Nicht mehr, nicht weniger.
- Keine Skandal- oder Klatsch-Themen
- Fokus auf Wirtschaft, Technologie, Infrastruktur, Regulierung
- Die Impulse sollen zeigen, was die US-Diskussion für Europa bedeutet
- ÜBERSPITZT und meinungsstark formuliert – wie eine scharfe Kolumne, nicht wie ein akademisches Paper
- Darf polarisieren, muss aber auf Fakten aus dem Transkript basieren
- Einschränkungen und Gegenargumente aus dem Podcast gehören HIER rein, nicht in die Deep-Dives
- NUTZE den EU-Kontext auch hier: Nenne konkrete Initiativen, Personen, Deadlines
- BEISPIEL gute These: "Trumps Kraftwerks-Zwang entlarvt Europas Rechenzentrum-Illusion"
- BEISPIEL schlechte These: "Energiefragen sind auch in Europa relevant"

---

## QUALITÄTS-CHECKLISTE (intern durchgehen vor Output)

Bevor du antwortest, prüfe:
- [ ] Steht JEDE Behauptung so im Transkript? Wenn nein → streichen
- [ ] Sind alle Personen mit der richtigen Rolle/Firma beschrieben?
- [ ] Sind wichtige Gesprächspartner berücksichtigt?
- [ ] Enthält der Output KEINE Informationen aus meinem Vorwissen?
- [ ] Bei mehreren Quellen: Ist jede These einer Quelle zugeordnet?
- [ ] Hat KEIN Deep-Dive mehr als 6 konkrete Detail-Punkte?
- [ ] Gibt es KEINEN Abschnitt "Einschränkungen/Offene Fragen" in den Deep-Dives?
- [ ] Ist die Europa-Relevanz in Stichpunkten (nicht Fließtext)?
- [ ] Sind die "Zum Drüber Nachdenken"-Impulse wirklich überspitzt und meinungsstark?
- [ ] Enthält JEDER Europa-Relevanz-Stichpunkt mindestens EINE konkrete Zahl, Frist, Person oder Institution aus dem EU-Kontext?
- [ ] Könnte der Europa-Relevanz-Stichpunkt auch OHNE EU-Kontext geschrieben werden? Wenn ja → zu generisch, umschreiben!
- [ ] Nennen die "Zum Drüber Nachdenken"-Impulse konkrete EU-Akteure, Initiativen oder Deadlines?
"""

USER_PROMPT_TEMPLATE = """Erstelle ein Executive Briefing aus dem folgenden Podcast-Transkript:

{transcript}"""

USER_PROMPT_WITH_EU_TEMPLATE = """Erstelle ein Executive Briefing aus dem folgenden Podcast-Transkript.

Nutze den EU-Kontext (unten) für zwei Zwecke:

1. **Europa-Relevanz pro Deep-Dive:** Ergänze Stichpunkte mit KONKRETEN Policy-Details (Paragraphen, Fristen, Bußgelder, Akteure, Institutionen). KEINE generischen Sätze. Denke wie ein Policy-Berater, der einem Minister erklärt, warum dieses Thema morgen auf seinem Schreibtisch landet.

2. **"Zum Drüber Nachdenken"-Impulse:** Verknüpfe US-Themen mit EU-Realitäten. Nenne Namen (Virkkunen, Höttges, Merz), Zahlen (€200 Mrd., 5% Chip-Anteil), Deadlines (Aug 2026 High-Risk). Formuliere überspitzt – wie eine Kolumne, nicht wie eine Studie.

QUALITÄTSTEST: Wenn ein Stichpunkt auch ohne den EU-Kontext geschrieben werden könnte (z.B. "Die EU reguliert KI"), ist er zu generisch. Lösche ihn und schreibe einen, der NUR mit dem EU-Kontext-Wissen möglich ist.

=== EU-KONTEXT ===
{eu_context}
=== ENDE EU-KONTEXT ===

=== PODCAST-TRANSKRIPT ===
{transcript}"""

EU_CONTEXT_FILE = "eu_context.md"


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

    # EU-Kontext laden falls vorhanden
    if os.path.exists(EU_CONTEXT_FILE):
        with open(EU_CONTEXT_FILE, "r", encoding="utf-8") as f:
            eu_context = f.read()
        user_message = USER_PROMPT_WITH_EU_TEMPLATE.format(
            eu_context=eu_context, transcript=transcript_text
        )
        print(f"EU-Kontext geladen: {len(eu_context)} Zeichen")
    else:
        print("Kein EU-Kontext gefunden, fahre ohne fort.")

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

    # 4. Gestyltes Email-HTML erzeugen
    try:
        from email_template import convert_md_to_email
        email_html = convert_md_to_email(briefing)
        with open(EMAIL_OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(email_html)
        print(f"Email-HTML gespeichert: {EMAIL_OUTPUT_FILE} ({len(email_html)} Zeichen)")
    except ImportError:
        print("email_template.py nicht gefunden – überspringe HTML-Generierung")
    except Exception as e:
        print(f"WARNUNG: Email-HTML Generierung fehlgeschlagen: {e}")
        print("Briefing.md wurde trotzdem gespeichert.")


if __name__ == "__main__":
    main()
