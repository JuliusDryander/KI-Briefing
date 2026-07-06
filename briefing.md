# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| KI-Souveränität | Palantir und Nvidia haben eine "Sovereign AI"-Partnerschaft angekündigt, bei der Palantir Nvidias offene Nemotron-Modelle nutzt, um ein kundenspezifisches Modell für die US-Regierung zu entwickeln, wobei die US-Behörden Hardware, Daten und Modellgewichte besitzen, um die Kontrolle über proprietäres Wissen zu behalten. | Alex Karp (CEO Palantir), David Sacks (ehemaliger AI Czar) | All-In |
| Open Source KI | Unternehmen erkennen zunehmend die Risiken der Weitergabe proprietärer Daten an große Frontier-Modellanbieter, die vertikal integrieren und mit ihren Kunden konkurrieren könnten, und wenden sich stattdessen Open-Source-Modellen und eigener Hardware zu, um Kosten zu senken und die Kontrolle zu behalten. | Chamath Palihapitiya (CEO 8090), David Friedberg (CEO O'Hollow), Jason Calacanis (All-In) | All-In |
| US KI-Exportkontrollen | Die US-Regierung hat vorübergehende Exportbeschränkungen für Anthropics Fable 5 (Mythos 5) verhängt, was laut David Sacks auf spezifische Umstände zurückzuführen war und nicht auf eine generelle Abkehr von Innovations- und Exportförderung. | David Sacks (ehemaliger AI Czar) | All-In |

# 🎙 Deep-Dive: Die Kern-Analysen

## 🛡️ KI-Souveränität und die Palantir-Nvidia-Partnerschaft

Alex Karp (CEO Palantir) und David Sacks (ehemaliger AI Czar) diskutieren die Bedeutung von "Sovereign AI" im Kontext einer neuen Partnerschaft zwischen Palantir und Nvidia. Palantir wird Nvidias offene Nemotron-Modelle nutzen, um ein kundenspezifisches Modell für die US-Regierung zu entwickeln. Dabei sollen die US-Behörden die Hardware, Daten und Modellgewichte besitzen. Karp kritisiert, dass Frontier Labs wie Anthropic proprietäres Wissen von Unternehmen aufsaugen und dann mit ihnen konkurrieren, was er als Vertrauensverlust und Gefahr für die Unternehmenssicherheit ansieht. Sacks betont, dass AI-Sicherheit für Unternehmen bedeutet, die Kontrolle über ihre Daten und Modelle zu behalten, anstatt sie an Dritte zu übertragen.

**Konkrete Details aus dem Gespräch:**
- Palantir nennt die neue Plattform "Sovereign AI Operating System".
- Alex Karp kritisiert, dass Frontier Labs proprietäres Wissen von Unternehmen aufsaugen und dann mit ihnen konkurrieren, wie im Fall von Figma und Claude Design oder Cursor und Claude Code.
- Karp betont, dass technische Kunden Kontrolle über Compute, Modelle, Datenstack und ihr "Alpha" (proprietäres Wissen) wollen.
- David Sacks interpretiert Dario Amodeis (Anthropic) Argumentation, Open-Source-Modelle seien gefährlich, als Versuch, sein Geschäftsmodell zu schützen, das eine geringe Auswahl auf der Modellebene erfordert.
- Sacks definiert AI-Sicherheit für Unternehmen als die Fähigkeit, die Kontrolle über eigene Daten und Modellgewichte zu behalten.

**🇪🇺 Europa-Relevanz:**
- Die EU AI Act-Vorschriften für Hochrisiko-KI-Systeme treten ab August 2026 in Kraft; die US-Diskussion um "Sovereign AI" zeigt, dass auch ohne explizite Regulierung der Schutz proprietärer Daten für Unternehmen kritisch ist.
- EVP Henna Virkkunen betont die Notwendigkeit, "doing business in Europe easier" zu machen, während hohe Standards gewahrt bleiben – die US-Souveränitätsdebatte könnte den Druck auf europäische Anbieter erhöhen, ähnliche Kontrollmechanismen anzubieten.
- Die EU AI Champions Initiative und InvestAI (Ziel: €200 Mrd. für KI) könnten von der "Sovereign AI"-Strategie lernen, indem sie europäische Unternehmen ermutigen, eigene Modelle auf europäischer Infrastruktur zu entwickeln, um Datenlecks zu verhindern.
- Rolf Schumann (Co-CEO Schwarz Digits) und Tim Höttges (Telekom) treiben mit dem €11 Mrd. Rechenzentrum Lübbenau und dem Telekom/Nvidia-Projekt München den Aufbau souveräner KI-Infrastruktur in Deutschland voran, was der US-Sovereign-AI-Logik entspricht.

## 💡 Open Source KI vs. Frontier-Modelle: Die Unternehmensstrategie

Die Diskussionsteilnehmer erörtern die wachsende Skepsis von Unternehmen gegenüber der Weitergabe proprietärer Daten an große Frontier-Modellanbieter. Chamath Palihapitiya (CEO 8090) berichtet von eigenen Tests, bei denen Open-Source-Modelle mit einer "Harness"-Software 16,4-mal günstiger waren als proprietäre Modelle, wenn auch dreimal langsamer. Eine ehemalige Meta-Produktmanagerin argumentiert, dass Open-Source-Modelle auf eigenen GPUs in US-Rechenzentren gehostet werden können, ohne Daten zu teilen, und dabei 100-mal billiger sein können. David Friedberg (CEO O'Hollow) bestätigt, dass Life-Science-Unternehmen sich weigern, ihre Daten mit Anbietern wie Anthropic zu teilen, um eine Kommodifizierung ihrer Assets zu vermeiden. Die Experten prognostizieren eine Verschiebung hin zu einer dezentraleren KI-Infrastruktur mit mehr unternehmenseigenen Modellen und On-Premise-Inferenz.

**Konkrete Details aus dem Gespräch:**
- Chamath Palihapitiya (CEO 8090) berichtet, dass ein Open-Source-Modell mit ihrer Software 16,4x billiger und 1,5x schneller war als Claude Opus 48 für eine Code-Migration.
- Eine Ex-Meta PM weist darauf hin, dass Open-Source-Modelle auf eigenen GPUs in US-Rechenzentren gehostet werden können, ohne Daten zu teilen, und dabei 100x billiger sein können.
- David Friedberg (CEO O'Hollow) berichtet, dass Life-Science-Unternehmen Anthropic ablehnen, ihre proprietären Daten für ein neues Modell zu teilen, da dies ihre Assets kommodifizieren würde.
- Die Modellentwicklung verschiebt sich von großen Hubs/Spokes zu großen Hubs, mittleren Hubs (für unternehmensinterne Trainings) und verteilten Spokes (für On-Premise-Inferenz).
- Nvidia hat mit Nemotron ein Open-Source-LLM, das für 95% der Anfragen mit Claude konkurrenzfähig ist, und fördert Open Source, um eine breitere Käuferbasis für Chips zu schaffen.
- Jason Calacanis warnt Gründer davor, mit großen Plattformen wie Microsoft, Facebook oder OpenAI zu kooperieren, da diese letztendlich die Geschäfte ihrer Partner übernehmen könnten.

**🇪🇺 Europa-Relevanz:**
- Die EU AI Champions Initiative und der Deutschlandfonds (KfW-gestützt, €30 Mrd. Garantien) zielen darauf ab, europäische KI-Technologieunternehmen und -Anwendungen zu fördern, was die Entwicklung eigener Open-Source-Modelle und -Infrastrukturen unterstützen könnte.
- Tim Höttges (Telekom) warnt, dass Europa nur 5% der KI-Hochleistungschips nutzt, während die USA 70% nutzen – die Verlagerung zu On-Premise-Inferenz und eigenen Modellen erfordert massive Investitionen in europäische Chip- und Rechenzentrumskapazitäten.
- Die Schwarz Gruppe investiert €11 Mrd. in das Rechenzentrum Lübbenau (Brandenburg) mit bis zu 100.000 GPUs, um souveräne Cloud- und KI-Infrastruktur bereitzustellen, was die europäische Antwort auf die Notwendigkeit eigener Hardware für Open-Source-Modelle darstellt.
- EVP Henna Virkkunen's Digital Fitness Check (Konsultation bis 11. März 2026) prüft die Wechselwirkung aller EU-Digitalgesetze, um die Umsetzung zu vereinfachen – dies könnte auch Anreize für die Nutzung und Entwicklung von Open-Source-KI in Europa schaffen.

## ⚖️ US KI-Exportkontrollen und regulatorische Dynamik

David Sacks (ehemaliger AI Czar) erläutert die Hintergründe der vorübergehenden US-Exportbeschränkungen für Anthropics Fable 5 (Mythos 5). Er führt die Maßnahme auf drei spezifische Bedingungen zurück: Dario Amodeis (Anthropic) Behauptung, Mythos sei eine "Cyberwaffe", einen Bericht von Amazon über das Versagen der Schutzmechanismen von Fable und Amodeis anfängliche Weigerung, das Modell zurückzuziehen. Sacks betont, dass dies ein einzigartiger Fall war und nicht auf eine generelle Abkehr der Trump-Administration von ihrer pro-innovativen und pro-exportorientierten Haltung hindeutet. Er argumentiert gegen ein Verbot chinesischer Open-Source-Modelle, da diese, einmal geforkt und auf eigener Hardware betrieben, ihre "Nationalität" verlieren und ein Verbot die USA isolieren würde.

**Konkrete Details aus dem Gespräch:**
- Die Exportkontrolle für Anthropics Fable 5 wurde nach zwei Wochen aufgehoben, nachdem Tom Brown (Co-Founder Anthropic) Dario Amodei als Verhandlungsführer abgelöst hatte und proaktiver mit der Trump-Administration kooperierte.
- David Sacks (ehemaliger AI Czar) führt die Exportbeschränkungen auf drei Bedingungen zurück: Dario Amodeis Behauptung, Mythos sei eine "Cyberwaffe", Amazons Bericht über das Versagen der Schutzmechanismen von Fable, und Amodeis anfängliche Weigerung, das Modell zurückzuziehen.
- Sacks betont, dass die Administration pro-Innovation, pro-Export und pro-Infrastruktur sein will und amerikanische Unternehmen im KI-Rennen unterstützen möchte.
- Er argumentiert, dass Open-Source-Modelle "nicht mehr chinesisch" sind, sobald sie geforkt und auf eigener Hardware in den USA betrieben werden, ohne Datenlecks.
- Ein Verbot chinesischer Open-Source-Modelle würde die USA isolieren und amerikanische Unternehmen einem "Token Tax" aussetzen, da der Rest der Welt Open-Source-Modelle nutzen würde.
- Sacks ist nicht grundsätzlich gegen Importbeschränkungen (z.B. chinesische Connected Cars, Roboter), warnt aber vor Vergeltungsmaßnahmen und der Notwendigkeit von Handelsbeziehungen (z.B. für seltene Erden).

**🇪🇺 Europa-Relevanz:**
- Die temporären US-Exportkontrollen für KI-Modelle könnten als Präzedenzfall für die EU dienen, insbesondere im Kontext des Anti-Coercion Instrument (ACI), das EU-Handelskommissar Maroš Šefčovič als Druckmittel in Handelsverhandlungen einsetzen könnte.
- Die Diskussion über die "Nationalität" von Open-Source-Modellen ist für die EU relevant, da die InvestAI-Initiative von EVP Henna Virkkunen fordert, dass "Majority owners should come from Europe" bei EU-finanzierten KI-Gigafactories, um Souveränität zu gewährleisten.
- Die EU hat WTO-Verfahren gegen US-Zölle eingeleitet, und die US-Diskussion über Importbeschränkungen für chinesische KI-Modelle könnte die EU dazu anregen, ihre eigene Position zu Technologieimporten und -souveränität zu klären, insbesondere angesichts der Abhängigkeit von seltenen Erden aus China.
- Die Mainzer Erklärung der deutschen Regierung betont KI als "Grundlage für Souveränität und Sicherheit" – dies könnte eine Grundlage für ähnliche Export- oder Importkontrollen in Deutschland oder der EU schaffen, falls Modelle als kritische Infrastruktur oder Sicherheitsrisiko eingestuft werden.

## 📌 Weitere bemerkenswerte Segmente

**KI und Arbeitsplatzveränderungen:** Die Diskussionsteilnehmer sind sich uneinig, ob KI zu massivem Jobverlust oder primär zu Jobverlagerung führen wird. Während Jason Calacanis (All-In) schnelle Verluste in Bereichen wie Kundenservice und Dateneingabe prognostiziert, verweisen David Sacks (ehemaliger AI Czar) und Chamath Palihapitiya (CEO 8090) auf Studien, die zeigen, dass KI-adoptierende Unternehmen tendenziell schneller wachsen und mehr Mitarbeiter einstellen, auch in Einstiegspositionen. Sie betonen, dass die Medien ein falsches Narrativ des Jobverlusts aufrechterhalten.

**Kaliforniens Haushaltskrise und Staatsführung:** David Friedberg (CEO O'Hollow) kritisiert Kaliforniens "ausgeglichenen" Haushalt als Illusion, da er auf Bilanzierungstricks und Schulden basiert. Er hebt die hohe Abhängigkeit von Top-Steuerzahlern, den Exodus von Unternehmen und Hochvermögenden sowie die steigenden Kosten und ungedeckten Pensionsverpflichtungen hervor, die das Land an den Rand eines möglichen Staatsbankrotts bringen könnten. Chamath Palihapitiya (CEO 8090) stimmt zu und prognostiziert eine komplette Neugestaltung der kalifornischen Verfassung und das Aus für Pensionsansprüche.

# 💭 Zum Drüber Nachdenken

**Europas KI-Souveränität: Ein teurer Traum oder die einzige Überlebensstrategie?**
Kontext: Die US-Debatte zeigt, dass Unternehmen ihre proprietären Daten nicht an große KI-Modellanbieter abgeben wollen, um nicht von diesen vertikal integriert und auskonkurriert zu werden. Stattdessen setzen sie auf eigene Hardware und Open-Source-Modelle. In Europa warnt Tim Höttges (Telekom), dass die EU nur 5% der KI-Hochleistungschips nutzt, während die USA 70% nutzen. Die Schwarz Gruppe investiert €11 Mrd. in ein Rechenzentrum in Lübbenau, um souveräne Infrastruktur zu schaffen.
Die Frage dahinter: Kann Europa es sich leisten, nicht massiv in eigene Chip- und Rechenzentrumskapazitäten zu investieren, um die Kontrolle über seine Daten und KI-Modelle zu behalten, oder ist die Abhängigkeit von US-Anbietern ein unkalkulierbares Risiko für die Wettbewerbsfähigkeit?

**Der EU AI Act: Ein Papiertiger gegen die US-KI-Giganten oder ein Schutzschild für europäische Werte?**
Kontext: Während die EU mit dem AI Act umfassende KI-Regulierung einführt (High-Risk-Systeme ab Aug 2026), kritisieren US-Akteure wie JD Vance den Ansatz als "authoritarian censorship". Gleichzeitig zeigen die temporären US-Exportkontrollen für Anthropics Fable 5, dass auch die USA bei Sicherheitsbedenken schnell handeln können. EVP Henna Virkkunen verhandelt den Digital Omnibus, der die High-Risk-Deadline um bis zu 16 Monate verschieben könnte (Backstop: Dez 2027), um der Industrie entgegenzukommen.
Die Frage dahinter: Ist die europäische Regulierung ein Wettbewerbsnachteil, der Innovation hemmt, oder bietet sie einen notwendigen Rahmen, um die Kontrolle über KI-Technologien zu behalten und europäische Unternehmen vor den aggressiven Strategien der US-Giganten zu schützen, die ihre Partner vertikal integrieren und auskonkurrieren?