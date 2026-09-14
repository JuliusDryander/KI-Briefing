# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| KI-Regulierung | Die US-Regierung und Think Tanks schlagen weitreichende Maßnahmen zur Verlangsamung und Kontrolle der KI-Entwicklung vor, mit Fokus auf Compute-Kontrollen und physischer Sicherheit von Rechenzentren, um existenzielle Risiken zu mindern. | Host, Thijs Simonian | TBPN |
| KI-Chips & Infrastruktur | Positron AI entwickelt neue Chips für die KI-Ära, wobei die Halbleiterentwicklung durch KI beschleunigt wird und der Fokus auf der Bewältigung von Skalierungs- und Lieferkettenherausforderungen liegt, um die enorme Nachfrage der Hyperscaler und Frontier Labs zu bedienen. | Mitesh Agarwal (Positron AI) | TBPN |
| Robotik & KI-Anwendungen | Aktuelle KI-Modelle können physische Roboter für komplexe Aufgaben steuern, was ein großes Potenzial für kostengünstige, quelloffene Robotik im DIY-Bereich und für alltägliche Anwendungen eröffnet. | Thijs Simonian (OpenAI intern) | TBPN |

# 🎙 Deep-Dive: Die Kern-Analysen

## 🚨 KI-Regulierung: US-Vorschläge für Compute-Kontrollen und physische Sicherheit

Die Diskussion bei TBPN beleuchtet, wie US-Think Tanks wie "AI 2040" und politische Akteure wie Bernie Sanders konkrete und weitreichende Vorschläge zur Regulierung der KI-Entwicklung vorlegen. Der Fokus liegt auf einer Verlangsamung des Fortschritts durch Compute-Kontrollen und erhöhte physische Sicherheit von Rechenzentren, um existenzielle Risiken zu adressieren. Diese Ansätze zielen darauf ab, die Entwicklung von Superintelligenz zu kontrollieren und zu verzögern, anstatt sie vollständig zu stoppen.

**Konkrete Details aus dem Gespräch:**
- Der "AI 2040"-Plan fordert eine "AI Pause", die das Training neuer "Frontier"-Modelle stoppen soll.
- Rechenzentren mit über 10.000 H-100-Äquivalenten (ca. 100 Mio. $ Equipment) sollen einer "Inference-only"-Verifizierung unterliegen.
- Es wird die Offenlegung von KI-Compute-Inventaren durch große Länder und von Verkaufsprotokollen von Chipherstellern gefordert.
- Physische High-Bandwidth-Netzwerke sollen in Rechenzentren entfernt werden, um große verteilte Trainingsläufe zu verhindern.
- Neue KI-F&E-Rechenzentren sollen mit "Nation-State-Level"-Sicherheit, Faraday-Käfigen und Air-Gap-Kommunikation gebaut werden, mit einer Bandbreitenbegrenzung von 1 Megabit pro Sekunde für externe Kommunikation.
- Frontier-Modellgewichte sollen bewusst größer als compute-optimal gemacht (z.B. 100 TB statt 1 TB) und nur verschlüsselt, von den USA und China gemeinsam signiert und physisch eskortiert transportiert werden.
- Bernie Sanders schlägt ein Verbot von künstlicher Superintelligenz vor, definiert als Systeme, die menschliche kognitive Leistung übertreffen oder die Entmachtung der Menschheit planen können, sowie eine neue Bundesbehörde zur Überwachung und Zerstörung solcher Systeme.

**🇪🇺 Europa-Relevanz:**
- Der EU AI Act (High-Risk-Deadline Aug 2026) reguliert bereits umfassend, während die US-Vorschläge (AI 2040, Sanders) auf Compute-Kontrollen und physische Sicherheit abzielen – eine regulatorische Asymmetrie, die EU-Anbieter benachteiligen könnte.
- Die Forderung nach Offenlegung von Compute-Inventaren und Chip-Verkaufsprotokollen könnte mit dem EU-Anti-Coercion Instrument (ACI) kollidieren, falls die USA einseitig handeln und die EU als Druckmittel reagieren müsste.
- EVP Henna Virkkunen (Tech-Souveränität) könnte die US-Vorschläge im Rahmen des Digital Fitness Checks (Konsultation bis 11. März 2026) prüfen, um die Auswirkungen auf die europäische KI-Industrie zu bewerten.

## ⚡ KI-Chips & Infrastruktur: Positron AI und die Gigawatt-Nachfrage

Mitesh Agarwal von Positron AI erörtert die rasante Entwicklung im Halbleiterbereich, die durch KI selbst beschleunigt wird. Sein Unternehmen konzentriert sich auf die Entwicklung neuer Chips für die KI-Inferenz, wobei die größten Herausforderungen in der Skalierung der Produktion und der Sicherstellung der Lieferketten liegen. Die Nachfrage von Hyperscalern und Frontier Labs bewegt sich im Gigawatt-Bereich, was enorme Investitionen und eine robuste Infrastruktur erfordert.

**Konkrete Details aus dem Gespräch:**
- Positron AI wurde 2023 gegründet und lieferte in 15 Monaten ein erstes Produkt auf FPGA-Basis aus.
- Das Unternehmen nutzt KI-Tools, insbesondere für die Verifikation, um mit einem vergleichsweise kleinen Team (kürzlich 100 Mitarbeiter) schnell neue Chips zu entwickeln.
- Nvidia setzt einen 12-Monats-Zyklus für neue Chips, was den Wettbewerb in der Halbleiterindustrie beschleunigt.
- Die Nachfrage von Hyperscalern und Frontier Labs nach Chips wird im Gigawatt-Bereich gemessen, was einem Umsatz von 35-40 Mrd. $ für Nvidia entsprechen würde.
- Kunden fragen nach Fabrikationskapazität und einfacher Bereitstellung, z.B. ohne Flüssigkeitskühlung.
- Positron umgeht Engpässe bei HPM (High Bandwidth Memory) und COOS (Chip-on-Wafer-on-Substrate) durch die Verwendung von Commodity Memory (LPDR5X), was technische Innovation zur Kompensation der geringeren Geschwindigkeit erfordert.
- Die Software-Strategie basiert auf PyTorch und VLM/SG Lang, mit Co-Design-Ansätzen für große Kunden zur Optimierung.
- KI-Agenten können die Bereitstellung neuer Modelle von Tagen/Wochen auf Stunden reduzieren.

**🇪🇺 Europa-Relevanz:**
- Tim Höttges (Telekom) warnte, dass Europa nur 5% der KI-Hochleistungschips nutzt, während die USA 70% nutzen – Positron AI's Fokus auf Skalierbarkeit und Commodity Memory könnte eine Alternative zu den HPM/COOS-Engpässen der Nvidia-Chips bieten.
- Die EU AI Champions Initiative mobilisiert €200 Mrd. für KI-Gigafactories, die bis zu 100.000 Next-Gen-AI-Chips beherbergen sollen – die Fähigkeit von Positron, Chips in Gigawatt-Mengen zu liefern, wäre entscheidend für das Erreichen dieser Ziele.
- Rolf Schumann (Co-CEO Schwarz Digits) treibt die €11 Mrd.-Investition in das Rechenzentrum Lübbenau voran, das bis zu 100.000 GPUs aufnehmen soll – die Verfügbarkeit alternativer Chip-Architekturen wie die von Positron könnte die Abhängigkeit von einzelnen Anbietern reduzieren.

## 🤖 Robotik & KI-Anwendungen: Vom virtuellen Pinsel zum IRL-Spamfilter

Thijs Simonian, ein Praktikant bei OpenAI, demonstriert die Fähigkeit aktueller KI-Modelle, physische Roboter für komplexe Aufgaben wie das Malen zu steuern. Er sieht ein enormes Potenzial für kostengünstige, quelloffene Robotik, die den DIY-Markt revolutionieren und alltägliche Aufgaben automatisieren könnte, ähnlich dem Boom der 3D-Drucker.

**Konkrete Details aus dem Gespräch:**
- Simonian arbeitet im Robotik-Team von OpenAI an explorativen Projekten, die KI-Modelle (Codex) mit physischen Robotern verbinden.
- Der Roboter nimmt ein Bild auf, schreibt einen Plan in Code, führt diesen aus und überwacht den Fortschritt mit weiteren Bildern.
- Herausforderungen sind die Verarbeitungszeit von Bildern (viele Tokens) und die Geschwindigkeit der Aktions-Feedback-Schleife.
- Er verwendet einen quelloffenen, 3D-druckbaren Hugging Face S.O100 Roboterarm, dessen Aktuatoren etwa 200 $ kosten.
- Simonian sieht Potenzial für "IRL Spamfilter"-Roboter, die Post sortieren, Werbung schreddern und auf Rechnungen reagieren.
- Die Modelle (z.B. Astra) können bereits heute Hunderte von Unkrautarten identifizieren, was den Weg für Gartenroboter ebnet.
- Er vergleicht die Entwicklung mit dem 3D-Druck-Boom, bei dem günstige Geräte den DIY-Markt explodieren ließen.

**🇪🇺 Europa-Relevanz:**
- Die Förderung von "Regulatory Sandboxes" im EU Digital Omnibus könnte die Entwicklung von Open-Source-Robotik-Projekten wie dem Hugging Face S.O100 Arm in Europa erleichtern, indem sie einen geschützten Raum für Experimente bietet.
- Die EU AI Champions Initiative und der Deutschlandfonds (mit Modul für DeepTech-Startups) könnten gezielt Startups fördern, die kostengünstige Robotik-Lösungen für den Alltag entwickeln, um die "IRL Spamfilter"-Vision zu realisieren.
- Das 1.000-Köpfe-Plus-Programm und die EFI-Empfehlung "Europäisch denken statt nationaler Kleinstaaterei" sind entscheidend, um KI-Talente wie Thijs Simonian in Europa zu halten und die Entwicklung von Open-Source-Robotik voranzutreiben.

## 📌 Weitere bemerkenswerte Segmente

**Investitionen in KI und der Wandel im VC-Markt:** Guy O'Siri und Alex Heath von Sound Ventures, Investoren in OpenAI, Anthropic und Hugging Face, beschreiben den aktuellen KI-Markt als unübersichtlich, aber weiterhin spannend. Sie betonen die Notwendigkeit, Visionäre und Talente frühzeitig zu erkennen, ähnlich wie in der Musikindustrie. Alex Heath, ehemals Journalist, wechselt ins VC-Geschäft und plant, seinen Podcast und Newsletter fortzusetzen, um tiefere Einblicke zu teilen, ohne traditionellen Enthüllungsjournalismus zu betreiben. (TBPN)

# 💭 Zum Drüber Nachdenken

**US-Regulierungs-Hammer droht Europas KI-Ambitionen zu zerschlagen, bevor sie richtig starten**
Kontext: Während die EU mit dem AI Act (High-Risk-Deadline Aug 2026) bereits umfassende KI-Regulierung implementiert, diskutieren die USA (AI 2040, Bernie Sanders) drastische Maßnahmen wie Compute-Kontrollen und physische Überwachung von Rechenzentren. Diese regulatorische Asymmetrie könnte europäische Unternehmen, die bereits unter hohen Compliance-Kosten leiden, zusätzlich belasten und den Brain Drain von KI-Talenten in die USA verstärken.
Die Frage dahinter: Kann Europa seine "AI Continent"-Vision (von der Leyen) verwirklichen, wenn die USA den globalen KI-Wettbewerb mit einem "Manhattan Project"-Ansatz neu definieren?

**Europas €200 Mrd. KI-Gigafactory-Traum kollidiert mit der Chip-Realität**
Kontext: Die EU plant mit InvestAI €200 Mrd. für KI-Gigafactories, um bis zu 100.000 Next-Gen-AI-Chips zu sichern. Doch Chiphersteller wie Positron AI betonen, dass Hyperscaler Gigawatt-Mengen an Chips fordern und die Lieferketten (HPM, COOS) extrem angespannt sind. Tim Höttges (Telekom) kritisiert, dass Europa nur 5% der Hochleistungschips nutzt. Ohne eine massive und unabhängige Chip-Beschaffungsstrategie droht Europa, trotz Milliardeninvestitionen, im globalen KI-Rennen abgehängt zu werden.
Die Frage dahinter: Wie kann Europa die benötigten Chip-Mengen sichern, wenn selbst neue Player wie Positron AI vor Gigawatt-Anforderungen stehen und die Lieferketten von wenigen Akteuren dominiert werden?