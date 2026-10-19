# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| KI-Markt & Erwartungen | Trotz explosiven Wachstums von 45% QoQ und einem annualisierten Umsatz von 67,2 Mrd. USD, verfehlte Anthropic die überzogenen Markterwartungen, was zu einem breiten Rückgang im KI-Sektor führte. | John, Tyler | TBPN |
| On-Prem Cloud Infrastruktur | Oxide Computer Company entwickelt Rack-Scale-Maschinen mit Hardware-Software-Co-Design, um Cloud-Computing auch On-Premise anzubieten, eine konträre Strategie in einem SaaS-dominierten Markt. | Bryan Cantrill | TBPN |
| Unterirdische Infrastruktur | Die Advanced Spade Company spezialisiert sich auf unterirdische Infrastruktur, insbesondere das Verlegen von Versorgungsleitungen, indem sie technische Probleme löst und effizientere Werkzeuge entwickelt, um die Kosten zu senken und die Sicherheit zu erhöhen. | Daniel Kimminau | TBPN |
| KI-Interpretierbarkeit & Alignment | Neue Forschungsergebnisse deuten darauf hin, dass neuronale Netze, selbst mit Billionen von Parametern, möglicherweise leichter interpretierbar sind als bisher angenommen, was die Entwicklung von AI-Alignment-Lösungen beschleunigen könnte. | Nick Camerata, Rune, Tyler | TBPN |
| Open Source KI-Debatte | Die Debatte um Open-Source-KI-Modelle ist intensiv, wobei Hyperscaler wie Microsoft eine ambivalente Haltung einnehmen, während die breite Wirtschaftslobby (25 Billionen USD Marktkapitalisierung) Open Source unterstützt. | Reed Albergotti, John, Tyler | TBPN |

# 🎙 Deep-Dive: Die Kern-Analysen

## 📉 KI-Markt: Anthropic verfehlt Erwartungen trotz massivem Wachstum

Laut der Diskussion verfehlte Anthropic die überzogenen Markterwartungen, obwohl das Unternehmen ein explosives Wachstum von 45% Quartal zu Quartal verzeichnete und einen annualisierten Umsatz von 67,2 Mrd. USD erreichte. Dies führte zu einem breiten Rückgang im KI-Sektor, wobei Coreweave im letzten Monat um etwa 50% fiel. Der Markt reagiert mit einer Rotation von Tech-Aktien hin zu traditionelleren Werten und Staatsanleihen.

**Konkrete Details aus dem Gespräch:**
- Anthropic's Q3-Umsatz betrug 16,8 Mrd. USD, was einem annualisierten Umsatz von 67,2 Mrd. USD entspricht.
- Die Markterwartungen für Anthropic lagen bei 90-150 Mrd. USD annualisiert.
- Meta hat sich von Anthropic abgewendet und nutzt nun eigene Modelle.
- "Distillation" (Modell-Diebstahl) macht 5-7% des Umsatzes aus, was Milliarden von Dollar an potenziellen Einnahmen entspricht und das Wachstum bremst.
- Der NASDAQ ist um 0,3-0,4% gefallen, während der Dow um fast 1% gestiegen ist, was eine Markt-Rotation signalisiert.
- Brad Gersner hat seine Coreweave-Positionen verkauft und 10% seines Kapitals in Meta und Tesla umgeschichtet, da er den KI-Markt als "überschossen" ansieht.

**🇪🇺 Europa-Relevanz:**
- Anthropic ist einer der 26 Anbieter, die den GPAI Code of Practice unterzeichnet haben, dessen Transparenzpflichten in der EU ab August 2025 in Kraft treten.
- Die EU AI Act-Vorschriften für High-Risk-KI-Systeme treten ab August 2026 in Kraft; die Enttäuschung über Anthropic könnte den Wettbewerbsdruck auf EU-Anbieter erhöhen, die strengere Compliance-Anforderungen erfüllen müssen.
- Die Diskussion um "Distillation" unterstreicht die Notwendigkeit robuster IP-Schutzmechanismen, die durch den EU AI Act und den Digital Fitness Check (Konsultation bis 11. März 2026) adressiert werden.

## ☁️ Oxide Computer Company: Cloud-Infrastruktur On-Premise neu gedacht

Bryan Cantrill, Co-Founder und CTO von Oxide Computer Company, beschreibt das Unternehmen als Hersteller von Rack-Scale-Maschinen mit Hardware-Software-Co-Design. Ihre Vision ist es, Cloud-Computing auch On-Premise verfügbar zu machen, eine konträre Strategie in einem Markt, der 2019 stark auf SaaS fokussiert war. Sie beobachteten, dass Hyperscaler ihre eigenen Maschinen bauen, während andere Unternehmen bei Skalierungsproblemen mit Commodity-Hardware konfrontiert sind.

**Konkrete Details aus dem Gespräch:**
- Oxide wurde 2019 gegründet, um Rack-Scale-Maschinen mit Hardware-Software-Co-Design für On-Premise-Cloud-Lösungen anzubieten.
- Das Unternehmen entwickelte eigene Compute-Slides, Switches, eliminierte UEFI-Bias und schrieb die gesamte Software von der Firmware bis zur Control Plane selbst.
- Die Seed-Finanzierung von 20 Mio. USD erfolgte durch Eclipse, die an das Hardware-Software-Co-Design glaubten.
- Oxide fokussiert sich auf große Kunden und langfristige Beziehungen, da Enterprise-Kunden Racks über lange Zeiträume testen, bevor sie größere Investitionen tätigen.
- Ein Ziel ist es, mehr Racks als Mitarbeiter zu versenden, um ein effizientes Geschäft mit hohem Umsatz pro Mitarbeiter zu führen.
- Das Unternehmen lernte aus dem Scheitern von Nebula, einer ähnlichen Vision, die an technischer Umsetzung, Fertigung, Lieferkette und Markteinführung scheiterte.

**🇪🇺 Europa-Relevanz:**
- Die EU fördert mit InvestAI (€200 Mrd. mobilisiert) den Aufbau von 4-5 KI-Gigafactories, die jeweils ~100.000 Next-Gen-AI-Chips beherbergen sollen – Oxide's Ansatz könnte für diese Infrastruktur relevant sein.
- Schwarz Digits investiert €11 Mrd. in das Rechenzentrum Lübbenau (Brandenburg) mit bis zu 100.000 GPUs; die Notwendigkeit von effizienter, souveräner Hardware-Infrastruktur ist in Europa hoch.
- Tim Höttges (Telekom) kritisiert, dass Europa nur 5% der KI-Hochleistungschips nutzt, während die USA 70% nutzen – Oxide könnte eine Alternative für den Aufbau europäischer Rechenkapazitäten bieten.

## ⛏️ Advanced Spade Company: Innovation in unterirdischer Infrastruktur

Daniel Kimminau, Gründer und CEO der Advanced Spade Company, konzentriert sich auf die Lösung technischer Probleme im unterirdischen Bauwesen, insbesondere beim Verlegen von Versorgungsleitungen. Das Unternehmen begann mit unbeliebten, schwierigen Arbeiten und entwickelte eigene, effizientere Werkzeuge und Datenintegrationen, um die Kosten zu senken und die Sicherheit zu erhöhen.

**Konkrete Details aus dem Gespräch:**
- Daniel Kimminau war zuvor an der Hyperloop- und Boring Company beteiligt und erkannte die technischen Herausforderungen im unterirdischen Bau.
- Das Unternehmen begann mit der privaten Leitungslokalisierung und entwickelte sich weiter zum Bohren, um schließlich eigene, bewährte Werkzeuge an kleinere Unternehmen zu verkaufen ("Golden Shovels").
- Die oberirdische Verlegung von Versorgungsleitungen führt zu Ausfällen (z.B. Waldbrände in LA), was die Notwendigkeit unterirdischer Lösungen unterstreicht.
- Die Herausforderung liegt im Mangel an geeigneten Technologien und Prozessen für sicheres, grabenloses Arbeiten in Städten.
- Das Team der Advanced Spade Company umfasst etwa 50-55 Mitarbeiter.
- Die Technologie ermöglicht es, die normale Wachstumsphase im Bauwesen zu beschleunigen.

**🇪🇺 Europa-Relevanz:**
- Die EU-Strompreise sind 2-3x höher als in den USA, und Deutschland hat die höchsten Industriestrompreise in Europa; unterirdische Leitungen können die Netzinfrastruktur stabilisieren und Ausfälle reduzieren.
- Der Berlin-Anschlag auf das Stromnetz (Jan 2026) hat die Debatte über kritische Infrastruktur (Kritis-Dachgesetz) und hybride Bedrohungen neu entfacht, was die Bedeutung robuster und sicherer Versorgungsnetze unterstreicht.
- Kanzler Merz' Regierung senkt Netzentgelte und Stromsteuer, um die Energiepreise zu senken, was Investitionen in effiziente Infrastruktur wie unterirdische Leitungen attraktiver macht.

## 🧠 KI-Alignment: Neuronale Netze leichter interpretierbar als gedacht

Nick Camerata, ehemals bei OpenAI und jetzt bei Goodfire, und Rune sind begeistert von neuen Forschungsergebnissen, die darauf hindeuten, dass neuronale Netze, selbst mit Billionen von Parametern, möglicherweise leichter interpretierbar sind als bisher angenommen. Camerata, der ursprünglich pessimistisch war, fand mit modernen "agentic tools" heraus, dass die meisten Neuronen in großen Modellen "lesbar" sind und ihre Schaltkreise "schön" erscheinen.

**Konkrete Details aus dem Gespräch:**
- Nick Camerata, der bei OpenAI an der mechanistischen Interpretierbarkeit arbeitete, war zunächst pessimistisch, da neuronale Netze "willkürlich verwickelte Knoten" bildeten.
- Mit modernen "agentic tools" und genauerer Betrachtung sind die meisten Neuronen in Modellen mit Billionen von Parametern "lesbar" und ihre Schaltkreise "schön".
- Viele zuvor als "verwickelt" angesehene Neuronen wurden missverstanden.
- Die erwarteten Hindernisse für die Interpretierbarkeit sind größtenteils nicht vorhanden.
- Camerata glaubt, dass die Interpretierbarkeit "recht bald" gelöst sein wird, da automatisierte Wissenschaftler sich verbessern.
- Diese Fortschritte sind sowohl für die Sicherheit (Alignment) als auch für die Fähigkeiten (Optimierung von Modellfunktionen) von KI-Systemen nützlich.

**🇪🇺 Europa-Relevanz:**
- EVP Henna Virkkunen betont die Notwendigkeit, hohe Standards zu wahren, während der Digital Omnibus die Umsetzung des AI Act vereinfachen soll; Fortschritte in der Interpretierbarkeit könnten die Einhaltung dieser Standards erleichtern.
- Der EU AI Act sieht Bußgelder bis zu €35 Mio. / 7% Umsatz für verbotene KI-Praktiken vor (ab Feb 2025) und verlangt ab Aug 2026 vollständige Compliance für High-Risk-Systeme – Interpretierbarkeit ist entscheidend für die Nachweisbarkeit der Compliance.
- Die Möglichkeit, Bias in KI-Systemen besser zu erkennen und zu verstehen (Bias-Erkennung mit sensiblen Daten unter Auflagen im Digital Omnibus erlaubt), wird durch verbesserte Interpretierbarkeit gestärkt.

## ⚖️ Microsoft & die Open Source KI-Allianz: Ein Kampf der Giganten

Reed Albergotti diskutiert die intensive Debatte um Open-Source-KI-Modelle, wobei Hyperscaler wie Microsoft eine ambivalente Haltung einnehmen. Während Microsofts CEO Satya Nadella als "kandidat" und "nicht performativ" beschrieben wird, würden die Hyperscaler Open Source am liebsten verbieten. Die breite Wirtschaftslobby, die Open Source unterstützt, repräsentiert jedoch eine Marktkapitalisierung von etwa 25 Billionen USD.

**Konkrete Details aus dem Gespräch:**
- Microsofts CEO Satya Nadella wird für seine offene und nicht-performative Kommunikationsweise gelobt.
- Xbox Labs experimentiert mit KI-generierten Mashup-Spielen und Cloud-Gaming, was die Notwendigkeit der Selbst-Disruption unterstreicht.
- Hyperscaler würden Open Source am liebsten verbieten, aber es ist "massiv" und "nimmt Fahrt auf".
- Ein Verbot von Open Source KI wird als technisch machbar, aber rechtlich schwer durchsetzbar angesehen, da ein neuer Rechtsrahmen erforderlich wäre.
- Die "Open Source Alliance" wird von Unternehmen mit einer Marktkapitalisierung von etwa 25 Billionen USD unterstützt.
- Es wird vorgeschlagen, Sicherheitslösungen (Sandboxes) durch Crowdsourcing zu entwickeln, anstatt sie auf wenige Labs zu zentralisieren.

**🇪🇺 Europa-Relevanz:**
- Die EU AI Champions Initiative (€150 Mrd. private Investitionen) und InvestAI (€200 Mrd. gesamt) zielen darauf ab, ein "CERN für KI" zu schaffen, das offene, kooperative Entwicklung fördert – im Gegensatz zu den US-Hyperscalern.
- EVP Henna Virkkunen fordert, dass Mehrheitseigentümer von EU-finanzierten KI-Projekten aus Europa kommen sollen und High-Risk-Anbieter ausgeschlossen werden, was die strategische Bedeutung von Open Source für die EU-Souveränität unterstreicht.
- Die EFI-Kommission empfiehlt 2026, "europäisch zu denken statt nationaler Kleinstaaterei" bei der KI-Entwicklung, was die Förderung von Open Source und Kooperation gegenüber einem Verbot unterstützt.

## 📌 Weitere bemerkenswerte Segmente

- **Inflation für die 1%:** Eine Analyse der "CPI Reserve" zeigt, dass Luxusgüter wie Chanel-Taschen (+139%), Met Gala Tickets (+233%) und Hamptons-Häuser (+160%) in den letzten 10 Jahren deutlich stärker gestiegen sind als die durchschnittliche Inflation, was auf eine "E-förmige" Wirtschaft hindeutet, in der sich verschiedene Einkommensklassen unterschiedlich entwickeln.
- **KI im Arbeitsmarkt:** KI verändert den Bewerbungsmarkt schneller als den Arbeitsmarkt selbst, mit KI-amplifizierten Bewerbungen, die auf KI-gestützte Filter und Interview-Avatare treffen; McKinsey nutzt bereits KI-Avatare für Interviews, die von Partnern beobachtet werden.
- **VC-Streit um Pro Rata Rechte:** Ein Streit zwischen Valar Atomics (Isaiah Taylor) und Day One Ventures über Pro Rata Rechte verdeutlicht die "Ehe" zwischen Gründern und VCs und die Schwierigkeit, Investoren zu diluieren, selbst bei kontroversen Hintergründen.

# 💭 Zum Drüber Nachdenken

**Anthropic's "Enttäuschung" entlarvt Europas KI-Ambitionen als Wunschdenken**
Kontext: Wenn selbst ein US-Frontier-Lab wie Anthropic mit 67 Mrd. USD annualisiertem Umsatz die überzogenen Erwartungen nicht erfüllen kann und mit "Distillation" kämpft, wie realistisch sind dann Europas €200 Mrd. InvestAI-Ziele für 4-5 Gigafactories? Während die EU ab Aug 2026 High-Risk-KI-Systeme reguliert, könnten US-Anbieter durch den Wettbewerbsdruck ihre Sicherheitsstandards lockern, was die Asymmetrie verschärft.
Die Frage dahinter: Ist Europas Fokus auf Regulierung und "CERN für KI" zu langsam und zu idealistisch, um mit der brutalen Realität des US-KI-Marktes mitzuhalten?

**Trumps Kraftwerks-Zwang entlarvt Europas Rechenzentrum-Illusion**
Kontext: Die Advanced Spade Company zeigt, wie grundlegende Infrastrukturprobleme (unterirdische Leitungen) gelöst werden müssen, während Bryan Cantrill (Oxide) die Notwendigkeit souveräner On-Prem-Cloud-Lösungen betont. In Europa, wo Strompreise 2-3x höher sind und Projekte wie das €11 Mrd. Rechenzentrum Lübbenau (Schwarz Digits) entstehen, ist die Energie- und Infrastrukturfrage noch kritischer. Die Debatte um Rechenzentrums-Moratorien in Frankfurt und Dublin zeigt, dass die EU vor ähnlichen, aber verschärften Herausforderungen steht.
Die Frage dahinter: Kann Europa seine KI-Ambitionen überhaupt realisieren, wenn es die fundamentalen Infrastrukturprobleme – von der Stromleitung bis zum Rechenzentrum – nicht mit der gleichen Dringlichkeit und Innovationskraft wie die USA angeht?