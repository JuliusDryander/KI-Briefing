# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| KI-Modell-Wettbewerb & Investitionen | Die Veröffentlichung von Open-Weight-Modellen wie TMLs "Inkling" und die zunehmende Skepsis gegenüber der reinen "Distillation" chinesischer Modelle signalisieren einen Wandel im KI-Modell-Wettbewerb, während Venture-Investoren in einem "disorientierenden" Markt mit "House Money" agieren und sich auf große KI- und Frontier-Tech-IPOs konzentrieren. | Miramirati, Everett Randle (Benchmark), Jack Morris (Engram Labs), Taran Chabra (Anthropic) | TBPN |
| KI-Ausgabenmanagement | Unternehmen erleben einen explosionsartigen Anstieg der KI-Ausgaben (bis zu 21x in Monaten), was die Notwendigkeit robuster Management-Tools wie Ramps Token-Spend-Management unterstreicht, um Kosten zu kontrollieren und die Effizienz durch dynamisches Routing und den Einsatz spezialisierter kleiner Modelle zu optimieren. | Eric Glyman (Ramp) | TBPN |
| Industrielle Automatisierung & Verteidigung | Senra Systems hat $65 Mio. in einer Serie B Runde erhalten, um die Präzisionsfertigung von Kabelbäumen für Luft- und Raumfahrt sowie Verteidigung zu modernisieren, indem es vertikale Integration, hohe Qualität und Geschwindigkeit durch Automatisierung und KI-gestützte Prozesse nutzt. | Jordan Black (Senra Systems) | TBPN |
| Halbleiter-Investitionen | TSMC hat seine Investitionen in den USA um weitere $100 Mrd. erhöht, was seine führende Position in der globalen Halbleiterlieferkette festigt, obwohl der Markt Bedenken hinsichtlich potenzieller Überinvestitionen äußert. | Host | TBPN |

# 🎙 Deep-Dive: Die Kern-Analysen

## 🧠 KI-Modell-Wettbewerb & Investitionen

Miramirati (ehemalige OpenAI Technologiechefin) und Everett Randle (General Partner bei Benchmark) diskutieren die Dynamik im KI-Modell-Markt. Miramirati's Unternehmen Thinking Machines Lab (TML) hat "Inkling" veröffentlicht, ein Open-Weight-Modell, das auf Anpassbarkeit für Fine-Tuning ausgelegt ist und als "bestes Open-Weight-AI-Modell außerhalb Chinas" gilt. Dies geschieht in einem Kontext, in dem Anthropic chinesische Modelle der "Distillation" beschuldigt und Millionen von Accounts schließt. Randle beschreibt das aktuelle Investitionsklima als "disorientierend" und von einem "Gefühl der Unvermeidbarkeit" geprägt, ähnlich dem Jahr 2021, jedoch diesmal durch große IPOs von KI- und Frontier-Tech-Unternehmen wie SpaceX, OpenAI und Anthropic angetrieben.

**Konkrete Details aus dem Gespräch:**
- TMLs "Inkling" ist ein Open-Weight-Modell mit 975 Milliarden Parametern (41 Milliarden aktiv), das auf Anpassbarkeit für Fine-Tuning ausgelegt ist.
- "Inkling" schlägt Nemotron 3 Ultra in Benchmarks und wird zwischen Kimi K2.5 und 2.7 eingeordnet.
- TML nutzte synthetische Daten von Open-Weight-Modellen (Kimi K2.5) für das Post-Training, was als "leichtester Touch" der Distillation beschrieben wird.
- Anthropic beschuldigt chinesische Modelle (Zipu, Deepseek, Alibaba, Moonshot, Minimax) der Distillation und schließt Millionen von Distillation-Accounts pro Woche.
- Everett Randle (Benchmark) beschreibt das Investitionsklima als "disorientierend" mit einem "Gefühl der Unvermeidbarkeit" ähnlich 2021, aber diesmal angetrieben durch große IPOs (SpaceX, OpenAI, Anthropic).
- Firmen mit großen Gewinnen aus wenigen Unternehmen ("Playing with house money") nehmen mehr Risiko, da Anthropic beispielsweise in acht ihrer Fonds enthalten ist.
- Randle kritisiert das Fehlen guter westlicher Open-Source-Modelle, sieht aber Fortschritte bei Nvidia (Nemotron) und TML (Inkling).

**🇪🇺 Europa-Relevanz:**
- Ab Aug 2025 müssen GPAI-Anbieter in der EU Transparenzpflichten erfüllen und den Code of Practice unterzeichnen; Metas Verweigerung und Anthropic's Kampf gegen Distillation zeigen die Herausforderungen bei der Durchsetzung dieser Standards.
- EVP Henna Virkkunen treibt die "Tech-Souveränität" voran; die US-Diskussion über ein "trusted telecom"-Modell für KI könnte die EU unter Druck setzen, sich zwischen chinesischen und westlichen Open-Source-Modellen zu entscheiden.
- Der Digital Omnibus (Nov 2025) könnte die High-Risk-Deadline des AI Act bis Dez 2027 verschieben, um der Industrie mehr Zeit für die Anpassung an Standards zu geben, was im Kontrast zur schnellen Entwicklung von Open-Weight-Modellen steht.

## 💰 Managing AI Spend & Efficiency

Eric Glyman (Co-CEO von Ramp) beleuchtet die explosionsartigen Kosten für KI-Modelle und die Notwendigkeit, diese Ausgaben zu managen. Ramp hat ein neues Produkt namens Token-Spend.fm eingeführt, um Unternehmen dabei zu helfen, ihre KI-Ausgaben zu überwachen und zu optimieren. Die Ausgaben für Token sind bei Ramp-Kunden in den letzten Monaten um das 21-fache gestiegen, und Ramps eigene KI-Ausgaben erreichten in einer Woche $1,5 Mio. Glyman betont, dass Unternehmen Strategien wie Caching, dynamisches Routing und den Einsatz kleiner, spezialisierter Modelle nutzen müssen, um die Effizienz zu steigern und die Kosten zu kontrollieren.

**Konkrete Details aus dem Gespräch:**
- Ramp-Kunden verzeichneten in den letzten Monaten einen 21-fachen Anstieg der Token-Ausgaben.
- Ramps eigene KI-Ausgaben erreichten $1,5 Mio. in einer einzigen Woche, was fast 10% der Gehaltsausgaben entspricht.
- Das neue Produkt Token-Spend.fm ermöglicht Unternehmen, API-Keys zu verknüpfen, Ausgaben zu überwachen, ungewöhnliche Spitzen zu erkennen und Kosten zu senken.
- Optimierungsstrategien umfassen Caching, Vermeidung von "Fast Mode" und dynamisches Routing von Aufgaben zu kleineren, spezialisierten Modellen.
- 59% der Token-Ausgaben durchschnittlicher Unternehmen entfallen auf Frontier-Modelle.
- Frontier-Modelle können für komplexe Aufgaben effizienter sein (z.B. "Scott Wu" pro Sekunde kann günstiger sein als ein "Team von Drittklässlern").
- Generative Interfaces können B2B-SaaS-Produkte intuitiver und relevanter machen, indem sie nutzerspezifische Ansichten bieten.
- Die Ramp Econ Lab-Forschung hilft, die wirtschaftlichen Auswirkungen von KI besser zu verstehen, da Ramp etwa 1% der gesamten Unternehmensausgaben in den USA verfolgt.

**🇪🇺 Europa-Relevanz:**
- Tim Höttges (Telekom) betont, dass Europa nur 5% der KI-Hochleistungschips nutzt, verglichen mit 70% in den USA, was die Notwendigkeit von Kostenoptimierung und effizienter Modellnutzung in der EU verstärkt.
- Die EU mobilisiert €200 Mrd. über InvestAI, um 4-5 KI-Gigafactories mit je ~100.000 Next-Gen-AI-Chips zu finanzieren, was die Infrastruktur für effizientere KI-Nutzung schaffen soll.
- Schwarz Digits investiert €11 Mrd. in ein Rechenzentrum in Lübbenau (Brandenburg) mit bis zu 100.000 GPUs, um die Rechenkapazität zu erhöhen und die Kosten für KI-Anwendungen zu senken.

## ⚙️ Industrielle Automatisierung & Verteidigung

Jordan Black (CEO und Mitgründer von Senra Systems) berichtet über die erfolgreiche Serie B Finanzierungsrunde von $65 Mio. für sein Unternehmen. Senra Systems konzentriert sich auf die Modernisierung der Präzisionsfertigung von Kabelbäumen für die Luft- und Raumfahrt sowie die Verteidigungsindustrie in den USA. Das Unternehmen setzt auf vertikale Integration, um die Qualität und Geschwindigkeit der Produktion zu verbessern, da Kabelbäume traditionell manuell und mit veralteten Methoden entworfen und gefertigt werden. Senra agiert als Engineering-Partner von der Prototypenentwicklung bis zur Serienproduktion und identifiziert Wachstumsmärkte wie Rechenzentren und neue Energie (z.B. Mikroreaktoren).

**Konkrete Details aus dem Gespräch:**
- Senra Systems hat $65 Mio. in einer Serie B Runde erhalten, mit Founders Fund als Investor.
- Das Unternehmen löst das $165 Mrd. Problem der Kabelbaumfertigung in den USA für Luft- und Raumfahrt und Verteidigung.
- Kabelbäume werden traditionell in Excel-Tabellen und PowerPoint-Folien entworfen und von Hand gefertigt, was zu Komplexität und Qualitätsmängeln führt.
- Senra bietet vertikale Integration, da Kunden das physische Produkt schnell und in hoher Qualität wünschen.
- Qualität ist der wichtigste Faktor: Senra erreicht über 99% "first-pass yield".
- Geschwindigkeit: Reduzierung der Lieferzeiten von Monaten auf Wochen.
- Forward-deployed engineering: Partnerschaft mit Kunden von Prototyp bis Produktion, um Design und Fertigung zu optimieren.
- Wachstumsmärkte: Rechenzentren (inkl. umgebende Infrastruktur wie Generatoren, HVAC), kommerzielle Luft- und Raumfahrt (Satelliten), neue Energie (Mikroreaktoren, Kernkraft).
- Automatisierungspfad: Von manueller Fertigung zu geschulten Arbeitskräften (90% der Belegschaft in 4 Wochen geschult) hin zu Semi-Automatisierung und zukünftiger Integration von KI und Robotik.
- Eigene KI-Software zur Optimierung der Materialkosten (Bill of Material, BOM) und zur Vorschlag von kosteneffizienten Komponenten.

**🇪🇺 Europa-Relevanz:**
- Kanzler Merz betont die Notwendigkeit einer F&E-Quote von 3,5% des BIP und sieht KI als "Grundlage für Souveränität und Sicherheit", was die Investitionen in Unternehmen wie Senra Systems unterstützt.
- Der Deutschlandfonds (Dez 2025) mit €30 Mrd. Garantien und €3,2 Mrd. Eigenmitteln zielt darauf ab, bis zu €130 Mrd. private Investitionen in DeepTech, KI und Verteidigung zu mobilisieren, was Senras Finanzierungsumfeld stärkt.
- Die Mainzer Erklärung (Jan 2026) der Merz-Regierung fordert eine Senkung der Körperschaftsteuer und verbesserte Abschreibungen, um die Industrieproduktion und Investitionen in Deutschland zu fördern.

## 📈 Halbleiter-Investitionen

TSMC hat seine Investitionspläne deutlich erhöht und plant, weitere $100 Mrd. in Fabs in den USA zu investieren. Dies unterstreicht die führende Rolle des Unternehmens in der globalen Halbleiterlieferkette. Trotz starker Geschäftsergebnisse reagierte der NASDAQ mit einem Rückgang von 1% auf die erhöhten CAPEX-Pläne, was auf Bedenken des Marktes hinsichtlich potenzieller Überinvestitionen hindeutet.

**Konkrete Details aus dem Gespräch:**
- TSMC übertraf die Gewinnerwartungen und erhöhte seine Investitionsausgaben (CAPEX).
- Das Unternehmen plant, weitere $100 Mrd. in Fabs in Arizona zu investieren.
- Diese Investitionen festigen TSMCs Position an der Spitze der globalen Halbleiterlieferkette.
- Der NASDAQ fiel um 1% aufgrund der TSMC-Ausgabenpläne, was auf Skepsis des Marktes gegenüber Überinvestitionen hindeutet.

**🇪🇺 Europa-Relevanz:**
- Tim Höttges (Telekom) warnt, dass Europa nur 5% der KI-Hochleistungschips nutzt, während die USA 70% nutzen; TSMCs US-Investitionen verschärfen diese Asymmetrie.
- Die EU mobilisiert €200 Mrd. über InvestAI, um 4-5 KI-Gigafactories mit je ~100.000 Next-Gen-AI-Chips zu finanzieren, um die Abhängigkeit von außereuropäischen Halbleiterinvestitionen zu reduzieren.
- EVP Henna Virkkunen betont, dass die Mehrheit der Eigentümer von EU-finanzierten Gigafactories aus Europa kommen sollte, um die Tech-Souveränität zu gewährleisten, was im Kontrast zu TSMCs US-Fokus steht.

## 📌 Weitere bemerkenswerte Segmente

- **California Forever:** Das Projekt verlor einen $3.2 Mrd. schweren Schiffbauauftrag von Defense Startup Seronic an den Hafen von Brownsville, Texas. Der Verlust wird auf Kaliforniens langwierige Genehmigungsprozesse zurückgeführt, was ein "mächtiges Signal" über die Wettbewerbsfähigkeit des Staates für große Industrieinvestitionen aussendet. (TBPN)
- **Roblox Build & AI-Infrastruktur:** Roblox kündigt "Build" an, eine KI-gestützte Plattform zur Spieleerstellung, die auf der eigenen Infrastruktur läuft, um Kosten zu senken und die Performance zu steigern. Das Unternehmen setzt auf KI für fotorealistisches Multiplayer-Gaming (AI upreszing), NPCs und dynamische Welterstellung, sowie für Sicherheit und IP-Management. (TBPN)

# 💭 Zum Drüber Nachdenken

**Trumps "Trusted Telecom"-Strategie für KI entlarvt Europas Souveränitäts-Illusion**
Kontext: US-Firmen wie TML und Nvidia versuchen, eine westliche Open-Source-KI-Alternative zu chinesischen Modellen zu etablieren, während Anthropic Millionen von "Distillation"-Accounts schließt. Die EU hat mit dem AI Act strenge Transparenzpflichten für GPAI-Anbieter ab Aug 2025 und fordert von EVP Virkkunen "Tech-Souveränität". Wenn die USA ihre "trusted telecom"-Strategie auf KI ausweiten, könnte dies die EU vor die Wahl stellen, ob sie chinesische Modelle (die oft auf US-Closed-Source basieren) oder die noch jungen westlichen Open-Source-Alternativen bevorzugt.
Die Frage dahinter: Wie kann Europa seine eigene KI-Souveränität sichern, wenn die globalen Open-Source-Modelle entweder aus China stammen oder auf US-Technologie basieren, und gleichzeitig die Gefahr der "Distillation" die Entwicklung bremst?

**Europas KI-Gigafactory-Träume kollidieren mit der Kostenrealität**
Kontext: Die "3-Dollar-Uber-Ära" der KI ist vorbei; Unternehmen wie Ramp sehen 21-fache Kostensteigerungen und müssen KI-Ausgaben aktiv managen, während die Investitionen in Rechenzentren und Halbleiter explodieren. Tim Höttges (Telekom) warnt, dass Europa nur 5% der KI-Hochleistungschips nutzt. Die EU mobilisiert €200 Mrd. über InvestAI, inklusive €20 Mrd. für 4-5 KI-Gigafactories, und Schwarz Digits investiert €11 Mrd. in ein Rechenzentrum in Lübbenau. Gleichzeitig sind EU-Strompreise 2-3x höher als in den USA, und es gibt Moratorien für Rechenzentren in Städten wie Frankfurt.
Die Frage dahinter: Kann Europa seine ambitionierten KI-Infrastrukturziele erreichen und gleichzeitig die explodierenden Betriebskosten für KI-Modelle in den Griff bekommen, wenn es mit deutlich höheren Energiepreisen und Genehmigungshürden als die USA zu kämpfen hat?