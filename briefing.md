# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| KI-Infrastruktur & Rohstoffe | Der Wert im KI-Zeitalter konzentriert sich auf die Infrastrukturschicht (Chips, Verpackung, Energie), was zu enormer Nachfrage nach Rohstoffen wie Kupfer und Engpässen bei Komponenten wie Leistungstransformatoren führt. | Daniel Gross (via Text), John, Jordy | TBPN |
| Geopolitische Implikationen der KI-Dominanz | Die USA sind der dominante Gewinner der KI-Ära mit massiven Investitionen und Modellentwicklung, während China versucht, mit weniger fortschrittlicher Chip-Technologie aufzuholen, was die Spannungen um Taiwan verschärft. | Daniel Gross (via Text), John, Jordy | TBPN |
| Venture Capital & IPO-Markt im Umbruch | Der Venture-Capital-Markt zeigt seit 25 Jahren mediane Renditen unterhalb des S&P 500, während der IPO-Markt trotz großer Erwartungen langsam bleibt, was zu einer Konzentration von Kapital in Top-Fonds und einer Zunahme von Illiquidität führt. | Dan Primack, John, Jordy | TBPN |
| Hardware-Test & -Betrieb für kritische Infrastruktur | Nominal entwickelt eine Plattform für Hardware-Tests und -Betrieb, die die Qualitätssicherung und den Lebenszyklus von physischen Assets von der Fertigung bis zum Einsatz in kritischen Bereichen revolutioniert, unterstützt durch KI-Testagenten und robuste Bereitstellungsoptionen. | Cameron Record, John, Jordy | TBPN |

# 🎙 Deep-Dive: Die Kern-Analysen

## ⚡ KI-Infrastruktur & Rohstoffe: Der Kampf um Chips, Energie und Kupfer

Laut der Diskussion konzentriert sich der Wert im KI-Zeitalter stark auf die Infrastrukturschicht, insbesondere auf Chips, deren Verpackung und die Energieversorgung. Dies führt zu einer massiven Nachfrage nach grundlegenden Rohstoffen und kritischen Komponenten, die Engpässe in der Lieferkette verursachen.

**Konkrete Details aus dem Gespräch:**
- Nvidia verzeichnete seit Januar 2024 einen Marktkapitalzuwachs von 3,2 Billionen Dollar, während Microsoft trotz 80 Milliarden Dollar AI CAPEX nur 4% zulegte.
- Der Kupferpreis stieg von 3,75 auf 6,61 Dollar pro Pfund (Allzeithoch), da ein Nvidia G-200 NVL-72 Server-Rack über 5.000 Kupferdrähte (2 Meilen lang) benötigt.
- Ein 100-Megawatt-Rechenzentrum benötigt etwa 3.000 Tonnen Kupfer; Rechenzentren werden in wenigen Jahren jährlich eine halbe Million Tonnen Kupfer verbrauchen.
- Lieferzeiten für Leistungstransformatoren erreichten über drei Jahre mit einem Angebotsdefizit von 30%; die Kosten stiegen seit 2020 um 150%.
- Microsoft schloss einen 16-Milliarden-Dollar-PPA zum Neustart von Three Mile Island; Google und Meta sicherten sich ebenfalls Kernkraft für Rechenzentren.
- Frontier-KI-Modelle wurden bisher nicht auf Hardware trainiert, die älter als 5-Nanometer ist; Chinas beste Anstrengung (Huawei Ascend 910C auf Smics 7-Nanometer-DUV-Prozess) ist für Inferenz wettbewerbsfähig, erfordert aber dramatisch mehr Chips und Energie für das Training.

**🇪🇺 Europa-Relevanz:**
- Tim Höttges (Telekom) warnt, dass Europa nur 5% der KI-Hochleistungschips nutzt, verglichen mit 70% in den USA – ein Indikator für Europas Abhängigkeit und den Bedarf an eigener Infrastruktur.
- Die EU mobilisiert mit InvestAI €200 Mrd. für KI, davon €20 Mrd. für 4-5 KI-Gigafactories mit je ~100.000 Next-Gen-AI-Chips, um die Chip-Abhängigkeit zu reduzieren.
- Schwarz Digits investiert €11 Mrd. in ein Rechenzentrum in Lübbenau (Brandenburg) für bis zu 100.000 GPUs, während die Deutsche Telekom mit Nvidia ein KI-Rechenzentrum in München (~€1 Mrd., 10.000 GPUs) baut, um der steigenden Nachfrage nach Rechenleistung zu begegnen.
- Die EU-Strompreise sind 2-3x höher als in den USA, und Deutschland hat die höchsten Industriestrompreise in Europa, was den Aufbau energieintensiver KI-Infrastruktur erschwert.

## 🌍 Geopolitische Implikationen der KI-Dominanz: USA, China und Taiwan

Die USA haben sich als dominanter Akteur in der KI-Ära etabliert, mit erheblich höheren privaten Investitionen und einer führenden Rolle bei der Entwicklung von KI-Modellen im Vergleich zu China. China versucht, durch den Einsatz von weniger fortschrittlicher Chip-Technologie aufzuholen, was jedoch für das Training von Frontier-Modellen ineffizient ist. Diese technologische Asymmetrie verschärft die geopolitischen Spannungen, insbesondere im Hinblick auf Taiwan, das eine kritische Rolle in der globalen Halbleiterlieferkette spielt.

**Konkrete Details aus dem Gespräch:**
- Die USA verzeichneten 2024 private KI-Investitionen von 109 Milliarden Dollar (kumulativ 470 Milliarden seit 2013), gegenüber Chinas 9,3 Milliarden Dollar im Jahr 2024.
- Die USA produzierten 2024 40 bemerkenswerte KI-Modelle, China 15.
- Kein Frontier-Modell wurde auf Hardware trainiert, die älter als 5-Nanometer ist; Chinas Huawei Ascend 910C auf Smics 7-Nanometer-DUV-Prozess erfordert für das Training dramatisch mehr Chips und Energie.
- China führte im Oktober 2024 und Dezember 2025 Militärübungen um Taiwan durch, bei denen Raketen in Taiwans angrenzende Zone einschlugen.
- China trennte in seinem 2026-2035-Plan "friedliche" von "Wiedervereinigung" im Kontext Taiwans.
- TSM plant einen Fab-Komplex in Arizona, der 30% der gesamten fortschrittlichen Produktion abwickeln soll, als Reaktion auf die geopolitischen Risiken.

**🇪🇺 Europa-Relevanz:**
- Die EU hat mit dem AI Act (High-Risk-Systeme müssen ab Aug 2026 compliant sein) einen umfassenden Regulierungsansatz gewählt, der im Gegensatz zur US-Selbstregulierung steht und von US-Vizepräsident JD Vance als "authoritarian censorship" kritisiert wurde.
- EVP Henna Virkkunen betont die Notwendigkeit der "Tech-Souveränität" Europas, während die Abhängigkeit von asiatischen Chip-Produzenten und US-KI-Modellen ein strategisches Risiko darstellt.
- Die Mainzer Erklärung der Merz-Regierung fordert KI als "Grundlage für Souveränität und Sicherheit", was die Notwendigkeit eigener Kapazitäten im Kontext der US-China-Spannungen unterstreicht.
- EU-Handelskommissar Maroš Šefčovič verhandelt bilateral mit den USA über Zölle (Section 122-Zölle), während die EU WTO-Verfahren eingeleitet und Gegenmaßnahmen von €93 Mrd. vorbereitet hat, was die Fragilität globaler Handelsbeziehungen zeigt.

## 📉 Venture Capital & IPO-Markt im Umbruch: Hoffnung über Erfahrung?

Dan Primack (Axios) und die Diskussionsteilnehmer beleuchten die anhaltende Schwäche des Venture-Capital-Marktes, dessen mediane Renditen seit 25 Jahren hinter den großen Aktienindizes zurückbleiben. Trotzdem strömt weiterhin Kapital in den Markt, auch durch neue Kanäle wie 401K-Pläne. Der IPO-Markt bleibt zögerlich, obwohl große Namen wie SpaceX und führende KI-Labs einen Börsengang anstreben. Die zunehmende Illiquidität in privaten Märkten und die Möglichkeit, Kapital durch Sekundärtransaktionen zu beschaffen, mindern den Druck für Unternehmen, an die Börse zu gehen.

**Konkrete Details aus dem Gespräch:**
- Mediane VC-Renditen liegen seit 25 Jahren unter S&P 500, NASDAQ und Russell 3000.
- Die Trump-Administration erlaubt 401K-Plänen Investitionen in private Fonds, was "dummes Geld" in den Markt spülen könnte.
- Top-Fonds und junge Fonds erzielen weiterhin die besten Renditen, während der Großteil des Geldes in der Mitte landet.
- Unternehmen bleiben länger privat (10-15 Jahre), was zu "Papierrenditen" und Illiquidität für LPs führt.
- Der IPO-Markt ist 2026 bisher um über 20% bei Preisen und Einreichungen gegenüber dem Vorjahr zurückgegangen.
- Große IPOs wie SpaceX (1,75 Billionen Dollar angestrebt), Databricks, OpenAI und Anthropic werden erwartet, könnten aber große Verluste offenbaren.
- Private Märkte bieten "unendliche Liquidität" durch Sekundärtransaktionen und Continuation Vehicles, was den Druck zum Börsengang mindert.
- CEOs und CFOs lehnen SPVs ab, da sie die Cap-Table komplizieren.

**🇪🇺 Europa-Relevanz:**
- Das EU-VC-Volumen liegt bei nur ~30% des US-Niveaus, was die Herausforderung für Europa unterstreicht, mit der US-Kapitalflut mitzuhalten.
- Die EU mobilisiert mit InvestAI €200 Mrd. für KI, davon €150 Mrd. aus privaten Investitionen (EU AI Champions Initiative), um die Finanzierungslücke zu schließen und europäische KI-Gigafactories zu fördern.
- Der Deutschlandfonds (€30 Mrd. Garantien, €130 Mrd. mobilisiert) zielt darauf ab, private Investitionen in DeepTech, KI und Verteidigung zu lenken, um die Abhängigkeit von öffentlichen Mitteln zu reduzieren.
- Kanzler Merz betont die Notwendigkeit, den europäischen und deutschen Kapitalmarkt besser für die Unternehmensfinanzierung zu nutzen, da die Kapitalmarktunion (CMU) nur langsam Fortschritte macht.
- Die Mainzer Erklärung der Merz-Regierung fordert eine Senkung der Körperschaftsteuer und verbesserte Abschreibungen, um Deutschland als Investitionsstandort attraktiver zu machen und dem US-Kapitalmarkt entgegenzuwirken.

## 🛡️ Hardware-Test & -Betrieb für kritische Infrastruktur: Nominal als Rückgrat der neuen Industrie

Cameron Record (Nominal) stellt eine Plattform für Hardware-Tests und -Betrieb vor, die den gesamten Lebenszyklus physischer Assets von der Fertigung bis zum Einsatz in kritischen Bereichen abdeckt. Das Unternehmen, das eine 80-Millionen-Dollar-Runde bei einer Bewertung von 1 Milliarde Dollar abgeschlossen hat, wächst durch die Verlagerung von F&E zu skalierter Fertigung und die Onshoring-Produktion. Nominal setzt auf KI-Testagenten zur Optimierung von Testprozessen und bietet robuste Bereitstellungsoptionen für Kunden, einschließlich direkter Regierungsaufträge im Verteidigungssektor.

**Konkrete Details aus dem Gespräch:**
- Nominal hat eine 80-Millionen-Dollar-Runde bei einer Bewertung von 1 Milliarde Dollar unter Führung von Founders Fund abgeschlossen.
- Die Plattform verwaltet Hardware-Tests und -Operationen vom Ende der Fertigung (Qualitätstests) bis zu Labortests (Stromversorgungen, Oszilloskope).
- Das Geschäft wächst mit der Verlagerung von F&E zu skalierter Fertigung und der Onshoring-Produktion, da die Qualität in der Branche sinkt.
- Nominal ermöglicht die Korrelation von Telemetrie- und Sensordaten in großem Maßstab, um anomales Verhalten zu überwachen und mit physischen Assets zu verknüpfen.
- Die Branche nutzt noch veraltete Tools wie Excel und MATLAB; Nominal bietet eine Cloud-basierte, horizontal skalierbare Alternative.
- Nominal entwickelt KI-Testagenten, die den nächsten besten Testpunkt bestimmen, um die Wissensmaximierung zu optimieren, anstatt linear durch Testmatrizen zu gehen.
- Das Unternehmen bietet "rugged deployability", einschließlich luftdicht abgeschotteter On-Premise-Server oder Bereitstellung in Kunden-VPCs, und unterstützt klassifizierte Arbeiten mit einer Betriebsstättenfreigabe.
- Rund zwei Drittel der 60 Kunden sind kommerziell, ein Drittel sind direkte Regierungsaufträge (z.B. US Air Force Test Pilot School).

**🇪🇺 Europa-Relevanz:**
- Das EU SAFE-Programm zielt auf autonome europäische Sicherheit und Verteidigung ab, was den Bedarf an robusten Hardware-Test- und Betriebs-Plattformen wie Nominal unterstreicht, um die Fragmentierung der Verteidigungsindustrie zu überwinden.
- Der Deutschlandfonds enthält erstmals ein Modul für Verteidigungs-Startups, um die Entwicklung von Technologien zu fördern, die die Lücke zu US-Anbietern wie Anduril oder Palantir schließen könnten.
- Der Berlin-Anschlag auf das Stromnetz (Jan 2026) hat die Debatte über kritische Infrastruktur (Kritis-Dachgesetz) neu entfacht und den Bedarf an sicheren und zuverlässigen Systemen für deren Überwachung und Wartung hervorgehoben.
- Nominals Expansion mit einem Büro in London zeigt das globale Problem und die europäische Nachfrage nach solchen Lösungen, insbesondere im Kontext der erhöhten geopolitischen Spannungen.

## 📌 Weitere bemerkenswerte Segmente

Die Verzögerungen bei Apples KI-Strategie, insbesondere der Gemini-gestützten Siri, bis voraussichtlich iOS 27, werfen Fragen nach der Wettbewerbsfähigkeit des Unternehmens im KI-Bereich auf, während OpenAI mit Hardware-Gerüchten und potenziellen Durchbrüchen bei Sprachmodellen experimentiert. Max Haot (Vast Space) kündigte eine 500-Millionen-Dollar-Finanzierungsrunde für den Bau der ersten kommerziellen Raumstation Haven 1 an, die die alternde ISS ersetzen und die Kosten für die Raumfahrt senken soll. Christian Howell (Cognito Therapeutics) stellte eine nicht-invasive, auf Licht- und Klangstimulation basierende Therapie für Alzheimer vor, die in einer großen klinischen Studie vielversprechende Ergebnisse bei der Erhaltung von Kognition und Funktion zeigt und eine 105-Millionen-Dollar-Finanzierung erhielt.

# 💭 Zum Drüber Nachdenken

**Europas Rechenzentrum-Illusion: Wenn Trumps Kraftwerks-Zwang auf Höttges' Chip-Mangel trifft**
Kontext: Während US-Tech-Giganten wie Microsoft und Google Kernkraftwerke für ihre Rechenzentren sichern und Oracle sich zum "Rate Payer Protection Pledge" bekennt, warnt Tim Höttges (Telekom) eindringlich: Europa nutzt nur 5% der KI-Hochleistungschips, die USA 70%. Die EU investiert zwar €200 Mrd. in InvestAI und Gigafactories wie Schwarz Digits' €11-Mrd.-Projekt in Lübbenau, doch die 2-3x höheren Strompreise in Europa und die strengeren Genehmigungsverfahren könnten diese Ambitionen untergraben.
Die Frage dahinter: Kann Europa seine KI-Souveränität wirklich aufbauen, wenn es die Energie- und Infrastrukturkosten nicht in den Griff bekommt und gleichzeitig die USA ihre Energieversorgung für KI aggressiv sichern?

**Der AI Act als Fessel oder Schutzschild: Wenn US-Regulierungs-Spott auf europäische Tech-Souveränität prallt**
Kontext: US-Vizepräsident JD Vance verhöhnt den EU AI Act als "autoritäre Zensur", während die EU mit EVP Henna Virkkunen auf Tech-Souveränität pocht und ab August 2026 strenge Compliance-Regeln für High-Risk-KI-Systeme durchsetzt. Gleichzeitig ringt der Digital Omnibus um eine mögliche Verschiebung dieser Deadline bis Dez 2027/Aug 2028. Die US-Dominanz bei KI-Modellen und -Investitionen (40 vs. 15 Modelle in 2024, $109 Mrd. vs. $9.3 Mrd. Investitionen) stellt Europa vor die Wahl: Entweder die eigenen Standards bremsen die Innovation, oder sie schützen vor den unregulierten Auswüchsen der US-Tech-Giganten.
Die Frage dahinter: Ist Europas umfassende KI-Regulierung ein notwendiger Schutz für seine Werte und Bürger, oder wird sie zum Bremsklotz im globalen KI-Wettlauf, der die Abhängigkeit von US-Technologien nur noch verstärkt?