# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| Compute-Effizienz & Infrastruktur | Die AI-Skalierungsära ist von erheblicher Ineffizienz bei der Compute-Nutzung geprägt, was eine "nationale Sicherheitskrise" darstellt und "Output Maxing" statt bloßem Skalieren erfordert, um mit globalen Wettbewerbern mithalten zu können. | Anjney Midha (AMP) | TBPN |
| AMDs KI-Strategie & Ökosystem | AMD verfolgt eine Strategie der offenen Ökosysteme und Partnerschaften, um die schnelle Adaption von KI voranzutreiben, wobei sie auf ein heterogenes Portfolio aus CPUs, GPUs und FPGAs setzen, da es keine "One-size-fits-all"-Lösung gibt. | Lisa Su (AMD CEO) | TBPN |
| Kernenergie & KI-Infrastruktur | Die narrative Wahrnehmung von Kernenergie als "Haftung" muss zu einem "echten Vermögenswert" verschoben werden, um die Energieengpässe für die KI-Infrastruktur zu lösen und die Wettbewerbsfähigkeit der USA zu sichern. | Seth Cohen (Mavera, Inc.) | TBPN |
| Hyperscaler KI-Investitionen & Marktdynamik | Große Technologieunternehmen wie Alphabet und OpenAI investieren massiv in KI-Infrastruktur, was zu enormen Ausgaben und neuen Projekten führt, während gleichzeitig Debatten über die Monetarisierung von KI und deren Auswirkungen auf den Arbeitsmarkt geführt werden. | Hosts, Max Anderson, Eric Sufert, Sundar Pachai, Sam Altman, Leong When Fung, Mark Zuckerberg | TBPN |

# 🎙 Deep-Dive: Die Kern-Analysen

## ⚡ Compute-Effizienz & Infrastruktur: Die "nationale Sicherheitskrise" der KI-Skalierung

Anjney Midha (AMP) kritisiert die massive Ineffizienz in der aktuellen KI-Skalierungsära, die er als "nationale Sicherheitskrise" bezeichnet. Er fordert ein Umdenken hin zum "Output Maxing", um die Compute-Ressourcen maximal zu nutzen und mit globalen Wettbewerbern mithalten zu können.

**Konkrete Details aus dem Gespräch:**
- Nur 15% der Flops in US-Rechenzentren werden genutzt; die Netflops-Auslastung liegt unter 20%.
- 30-40% Flop-Verlust entstehen durch schlechte Zeitplanung bei Langzeitmieten von Rechenzentren.
- Innerhalb eines Chips werden nur 15% der Flops genutzt (Model Flop Utilization, MFU), da der Chip auf andere Prozesse wartet.
- AMP beschafft neue Energiekapazität für 2030, da die Lieferkette für zwei Jahre blockiert ist und es nicht genug Standorte gibt.
- Kernkraft wird als notwendig erachtet, um den steigenden Energiebedarf zu decken.
- Private Kreditmärkte sehen Startups nicht als "investment-grade" für die Beschaffung von Compute-Kapazität.
- Reinforcement Learning (RL) wird als der "Geschenkgeber" bezeichnet, der die nächste Welle des Konsums antreibt, insbesondere dort, wo formale Verifikation möglich ist (z.B. Coding, Materialwissenschaft).

**🇪🇺 Europa-Relevanz:**
- EU-Strompreise sind 2-3x höher als in den USA, und Deutschland hat die höchsten Industriestrompreise in Europa – die 15%ige Compute-Auslastung in den USA wäre in der EU wirtschaftlich untragbar.
- Das €11 Mrd. Rechenzentrum Lübbenau von Schwarz Digits (200 MW) und das €1 Mrd. Telekom/Nvidia-Projekt in München müssen von Anfang an auf maximale Effizienz ausgelegt sein, um im europäischen Energiemarkt bestehen zu können.
- Kanzler Merz' Regierung senkt Netzentgelte und Stromsteuer für das produzierende Gewerbe, um die Wettbewerbsfähigkeit zu verbessern, was auch für energieintensive KI-Infrastruktur relevant ist.
- EVP Henna Virkkunen betont die Notwendigkeit, "doing business in Europe easier" zu machen, was die Vereinfachung von Genehmigungsverfahren für Rechenzentren und die Sicherstellung einer stabilen Energieversorgung einschließt.

## 🚀 AMDs KI-Strategie & Ökosystem: Heterogene Compute für eine schnelle KI-Adoption

Lisa Su, CEO von AMD, beschreibt die aktuelle KI-Ära als eine Zeit extrem schneller Veränderungen, die AMD dazu zwingt, noch schneller zu agieren. Sie betont AMDs Kultur der Partnerschaft und offener Ökosysteme, um die KI-Adaption voranzutreiben, und setzt dabei auf ein breites, heterogenes Portfolio aus CPUs, GPUs und FPGAs, da es keine "One-size-fits-all"-Lösung für die vielfältigen Workloads gibt.

**Konkrete Details aus dem Gespräch:**
- Die Rate und das Tempo der KI-Adoptionskurve und Technologieentwicklung sind "viel, viel schneller" als in der Vergangenheit.
- AMD muss Entscheidungen für Technologie-Roadmaps drei bis fünf Jahre im Voraus treffen, aber der Markt verlangt noch höhere Geschwindigkeit.
- Partnerschaft ist die Grundlage der AMD-Kultur, mit dem Ziel, "eins plus eins ist größer als drei" zu erreichen.
- Anthropic nutzt AMD MI355-Beschleuniger, wobei Claude ihnen hilft, neue Hardware ohne AMDs direkte Hilfe zu adaptieren.
- AMD glaubt an eine "heterogene Welt" und bietet ein Portfolio aus CPUs, GPUs (nach Xilinx-Akquisition), FPGAs und einem PC-Ökosystem.
- Investitionen in "Local AI" durch AI PCs (Ryzen AI Max Portfolio) und kleine Robotik-Formfaktoren zur Senkung der Einstiegshürden.
- R&D-Fokus auf Chiplets, Networking und Optimierung von CPU/GPU-Integration (Helios).

**🇪🇺 Europa-Relevanz:**
- Tim Höttges (Telekom) warnt, dass Europa nur 5% der KI-Hochleistungschips nutzt, während die USA 70% nutzen – AMDs Fokus auf heterogene Systeme und lokale KI könnte Europas Abhängigkeit von einzelnen Chip-Architekturen reduzieren.
- Die EU AI Champions Initiative mobilisiert €200 Mrd. für KI-Investitionen, darunter €20 Mrd. für 4-5 KI-Gigafactories, die von AMDs Technologie-Roadmap und Partnerschaftsansatz profitieren könnten.
- Die Förderung von "Local AI" durch AMDs AI PCs und Robotik-Formfaktoren könnte die Entwicklung von KI-Anwendungen im europäischen Mittelstand und in Startups erleichtern, die nicht sofort auf große Cloud-Instanzen zugreifen können.
- EVP Henna Virkkunen betont die Notwendigkeit, die Tech-Souveränität Europas zu stärken, wozu auch die Diversifizierung der Chip-Lieferanten und die Förderung offener Ökosysteme gehören.

## ☢️ Kernenergie & KI-Infrastruktur: Vom Abfall zum nationalen Vermögenswert

Seth Cohen, Mitgründer von Mavera, Inc., argumentiert, dass die öffentliche Wahrnehmung von Kernenergie von einer "Haftung" zu einem "echten Vermögenswert" verschoben werden muss, um die Energieengpässe für die KI-Infrastruktur zu lösen und die Wettbewerbsfähigkeit der USA zu sichern. Er hebt hervor, dass die Kernenergie ein enormes ungenutztes Potenzial birgt.

**Konkrete Details aus dem Gespräch:**
- Seth Cohen war Chief Counsel of Nuclear Policy im Department of Energy (DOE) und war für die Umsetzung nuklearer Executive Orders des Präsidenten verantwortlich.
- Er war maßgeblich an einer erfolgreichen narrativen Verschiebung bei Nuklearabfällen beteiligt: Von Yucca Mountain als einziger Option zu 27 Gouverneuren, die sich für das "Nuclear Life Cycle Innovation Campus"-Programm bewerben.
- Drei Standorte werden voraussichtlich für die vollständige Brennstoffkreislauf-Verarbeitung ausgewählt, die zu wettbewerbsfähigen Metropolregionen re-industrialisiert werden könnten.
- 97% der potenziellen Energie verbleiben in einem Brennstab, nachdem er aus einem Reaktor entnommen wurde.
- 100.000 Tonnen "verbrauchten" Brennstoffs aus 60 Jahren kommerzieller Flotte passen auf ein Fußballfeld und enthalten viermal mehr Energie als Saudi-Arabiens nachgewiesene Ölreserven.
- Datenzentren stehen in den USA vor enormen Problemen, auch aufgrund der öffentlichen Wahrnehmung, obwohl sie "kritische nationale Vermögenswerte" sind.

**🇪🇺 Europa-Relevanz:**
- Während Deutschland am Atomausstieg festhält, plant Frankreich den Bau von 6-14 EPR2-Reaktoren und setzt Atomkraft als Industriestrategie ein, was eine Asymmetrie in der europäischen Energiepolitik darstellt.
- Schweden und andere EU-Staaten diskutieren Small Modular Reactors (SMRs) als potenzielle Lösung für den steigenden Energiebedarf, auch im Kontext von Rechenzentren.
- Das €11 Mrd. Rechenzentrum Lübbenau von Schwarz Digits, das auf erneuerbare Energien und Fernwärme setzt, steht im Spannungsfeld zwischen dem deutschen Atomausstieg und dem enormen Energiebedarf der KI-Infrastruktur.
- Die Debatte über kritische Infrastruktur (Kritis-Dachgesetz) in Deutschland nach dem Berliner Anschlag auf das Stromnetz (Jan 2026) unterstreicht die Notwendigkeit einer stabilen und sicheren Energieversorgung für KI-Rechenzentren.

## 💰 Hyperscaler KI-Investitionen & Marktdynamik: Das Wettrennen um die Compute-Dominanz

Große Technologieunternehmen wie Alphabet und OpenAI investieren massiv in KI-Infrastruktur, was zu enormen Ausgaben und neuen Projekten führt. Gleichzeitig werden Debatten über die Monetarisierung von KI und deren Auswirkungen auf den Arbeitsmarkt geführt, während neue Akteure wie DeepSeek mit beeindruckenden Finanzkennzahlen aufwarten.

**Konkrete Details aus dem Gespräch:**
- Alphabet verzeichnete im Q2 24% Umsatzwachstum (Cloud 82%), aber hohe Ausgaben für KI-Infrastruktur führten zu negativem Cashflow.
- Google Cloud generiert Produktumsätze "primär aus dem Verkauf von TPU-Systemen".
- Google's Gemini-APIs verarbeiten 22 Milliarden Tokens pro Minute, angetrieben vom effizienten Flash-Modell.
- OpenAI erhöht seine prognostizierten Ausgaben für Rechenleistung bis 2030 auf 750 Milliarden US-Dollar (von 600 Milliarden US-Dollar).
- OpenAI investiert 20 Milliarden US-Dollar in ein Rechenzentrum namens "Project Camilla" in Effingham County, Georgia.
- DeepSeek (China) meldet 85% Inferenzmargen, 1 Milliarde US-Dollar API-Umsatz (cashflow-positiv) und eine GPU-Amortisationszeit von 10 Monaten.
- DeepSeek konzentriert sich ausschließlich auf den Weg zur AGI, nicht auf Weltmodelle, Bild-/Video-Generierung oder Chat-Apps.
- Eine Google-Studie besagt, dass KI Arbeitnehmern hilft und sie nicht ersetzt, wobei die Nutzung in den meisten Berufen noch "oberflächlich" ist.
- Mark Zuckerberg (Meta) startet eine Kampagne für KI-Optimismus, im Gegensatz zu "Angst und einer dystopischen Vision der Zukunft".

**🇪🇺 Europa-Relevanz:**
- Die massiven Investitionen von OpenAI ($750 Mrd. bis 2030) und Alphabet in KI-Infrastruktur stellen eine Herausforderung für die EU dar, die mit InvestAI €200 Mrd. mobilisieren will, um den "AI Infrastructure Gap" zu schließen.
- Tim Höttges (Telekom) warnt, dass Europa nur 5% der KI-Hochleistungschips nutzt, während die USA 70% nutzen – die EU muss ihre Investitionen in Rechenzentren und Chip-Produktion (z.B. durch die EU AI Champions Initiative) beschleunigen.
- Die Mainzer Erklärung der Merz-Regierung fordert eine F&E-Quote von 3,5% des BIP und eine "KI-Offensive" mit €17,1 Mrd. für Forschung und Entwicklung im Bundeshaushalt 2026, um mit den globalen Investitionen Schritt zu halten.
- Die Google-Studie, die besagt, dass KI Arbeitsplätze nicht ersetzt, sondern hilft, könnte die Debatte um den EU AI Act beeinflussen, der ab August 2026 hohe Bußgelder für nicht-konforme High-Risk-Systeme vorsieht.

## 📌 Weitere bemerkenswerte Segmente

- **Odyssey und Weltmodelle:** Oliver Cameron von Odyssey entwickelt "foundational world models", die als Basisintelligenz für virtuelle (Gaming, Bildung) und physische (autonome Fahrzeuge, Robotik, Drohnen) Systeme dienen sollen. Er glaubt, dass diese Modelle handgesteuerte Systeme ersetzen können, indem sie ein tiefes Verständnis von Physik, Ursache-Wirkung und menschlichem Verhalten lernen und dann leicht auf spezifische Aufgaben abgestimmt werden.
- **Ideogram und Unternehmensdesign-KI:** Mohammad Norouzi von Ideogram konzentriert sich auf die KI-Grundlage für die Unternehmensadoption in den Bereichen Content und Design, insbesondere bei der Generierung von Bildern und Designs für Marketing und Produktentwicklung. Sie arbeiten an der Lösung von Konsistenzproblemen und bieten kompakte, offene Modelle an, die Unternehmen On-Premise hosten können, um Datensouveränität und IP-Schutz zu gewährleisten.

# 💭 Zum Drüber Nachdenken

**Amerikas Compute-Verschwendung ist Europas Energie-Albtraum – und die EU schläft noch.**
Kontext: Während US-Firmen wie AMP die 15%ige Auslastung ihrer Rechenzentren als nationale Sicherheitskrise beklagen, kämpft Europa mit Strompreisen, die 2-3x höher sind als in den USA. Projekte wie das €11 Mrd. Rechenzentrum von Schwarz Digits in Lübbenau oder das €1 Mrd. Telekom/Nvidia-Projekt in München müssen unter diesen Bedingungen eine Effizienz erreichen, die in den USA offenbar noch ignoriert wird.
Die Frage dahinter: Kann Europa seine KI-Ambitionen (InvestAI: €200 Mrd., 4-5 Gigafactories) überhaupt realisieren, wenn es die US-Ineffizienzen importiert, anstatt eigene, energieeffiziente "Output Maxing"-Standards zu etablieren?

**Während die USA mit 750 Milliarden Dollar die AGI-Rennstrecke pflastern, bremst Europa mit dem AI Act die eigene Innovations-PS aus.**
Kontext: OpenAI plant bis 2030 $750 Mrd. für Rechenleistung, während DeepSeek sich kompromisslos auf AGI konzentriert. In Europa hingegen müssen High-Risk-KI-Systeme ab August 2026 compliant sein (Bußgelder bis €35 Mio.), und selbst eine mögliche Verschiebung der Deadline durch den Digital Omnibus bis Dez 2027 ändert nichts an der grundsätzlichen regulatorischen Last.
Die Frage dahinter: Kann die EU ihre "Tech-Souveränität" und das Ziel, "doing business in Europe easier" zu machen (EVP Virkkunen), erreichen, wenn sie mit strengen Vorschriften und einem Anteil von nur 5% an KI-Hochleistungschips (Tim Höttges) dem globalen KI-Wettlauf hinterherhinkt?