# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| KI-Markt & Anthropic | Trotz explosiven Wachstums von 45% Quartal zu Quartal verfehlte Anthropic die überzogenen Markterwartungen, was zu einem breiten Rückgang im KI-Sektor führte, da Anleger eine leichte Verlangsamung des exponentiellen Wachstums als "Dezeleration" interpretierten. | Hosts | TBPN |
| KI-Alignment | Neue Forschungen zeigen, dass neuronale Netze in KI-Modellen, selbst mit Billionen von Parametern, weitgehend interpretierbar sind, was die Hoffnung auf eine erfolgreiche Ausrichtung ("alignment") der KI stärkt. | Nick Camerata, Rune | TBPN |
| Cloud-Infrastruktur | Oxide Computer Company entwickelt Rack-Scale-Maschinen mit Hardware- und Software-Co-Design für On-Premise-Cloud-Lösungen, um Unternehmen eine Alternative zu Commodity-Hardware und Public Clouds zu bieten. | Bryan Cantrill | TBPN |
| Unterirdische Infrastruktur | Advanced Spade Company spezialisiert sich auf den Bau unterirdischer Versorgungsleitungen, indem sie Nischenarbeiten durch datengestützte Technologie effizienter gestaltet und so schrittweise größere Projekte akquiriert. | Daniel Kimminau | TBPN |
| KI & Kapitalmärkte | Die massive Kapitalverschiebung in KI-bezogene CAPEX wird in den nächsten zehn Jahren zu einem Anstieg der Zinssätze führen, was zunächst eine Panik auslöst, aber nach drei Jahren in Euphorie umschlägt, da die Investitionen hohe Renditen abwerfen. | Blake Byers | TBPN |

# 🎙 Deep-Dive: Die Kern-Analysen

## 📉 KI-Markt & Anthropic: Explosives Wachstum trifft auf überzogene Erwartungen

Laut der Diskussion verfehlte Anthropic trotz eines Quartalswachstums von 45% die überzogenen Markterwartungen, was zu einem breiten Rückgang im KI-Sektor führte. Anleger interpretierten eine leichte Verlangsamung des exponentiellen Wachstums als "Dezeleration", was den Markt verunsicherte. Das "Tall Poppy Syndrome" im Frontier-KI-Bereich führt dazu, dass andere Unternehmen Deals mit Wettbewerbern eingehen, um Monopole zu verhindern.

**Konkrete Details aus dem Gespräch:**
- Anthropic meldete einen Q3-Umsatz von $16.8 Mrd., der auf $67.2 Mrd. annualisiert wird, was jedoch unter den Erwartungen von $90-150 Mrd. lag.
- Coreweave ist im letzten Monat um ca. 50% gefallen, was die breite Marktschwäche im KI-Sektor unterstreicht.
- Distillation (Modell-Diebstahl) macht 5-7% des Umsatzes von Anthropic aus, was einem Betrug von $5 Mrd. entspricht und das Umsatzwachstum bremst.
- Meta hat auf eigene Modelle umgestellt und drohte, Anthropic-Käufe einzustellen, um deren IPO-Bewertung zu beeinflussen.
- Die NASDAQ ist nur leicht gefallen, während der Dow um fast ein Prozent gestiegen ist, was auf eine Kapitalrotation hindeutet.

**🇪🇺 Europa-Relevanz:**
- Anthropic ist einer der 26 Anbieter, die den GPAI Code of Practice unterzeichnet haben (Aug 2025), was Transparenzpflichten mit sich bringt, während das Unternehmen in den USA mit Markterwartungen kämpft.
- Die EU AI Act-Vorschriften für High-Risk-KI-Systeme treten ab Aug 2026 in Kraft; die Diskussion um "Dezeleration" könnte den Wettbewerbsdruck auf EU-Anbieter erhöhen, die gleichzeitig hohe Compliance-Kosten tragen.
- EVP Henna Virkkunen prüft mit dem Digital Fitness Check (Konsultation bis 11. März 2026) die Wechselwirkung aller EU-Digitalgesetze, um das Geschäft in Europa zu erleichtern, während US-Firmen mit Markterwartungen kämpfen.

## 🧠 KI-Alignment: Neuronale Netze sind interpretierbarer als gedacht

Nick Camerata, ein ehemaliger OpenAI-Mitarbeiter, berichtet von neuen Forschungen, die zeigen, dass neuronale Netze in KI-Modellen, selbst mit Billionen von Parametern, weitgehend interpretierbar sind. Entgegen früherer Skepsis, dass diese Systeme "willkürlich verwickelte Knoten" bilden, erweisen sich ihre internen Schaltkreise als "schön" strukturiert. Diese Erkenntnisse stärken die Hoffnung auf eine erfolgreiche Ausrichtung ("alignment") der KI.

**Konkrete Details aus dem Gespräch:**
- Nick Camerata war bei frühen Arbeiten bei OpenAI pessimistisch, da nur etwa 2% der Neuronen mit primitiven Tools lesbar waren.
- Mit modernen, agentischen Tools und genauerer Betrachtung sind die meisten Neuronen in Modellen mit Billionen von Parametern lesbar.
- Viele berühmte Beispiele für "verwickelte Neuronen" wurden als missverstanden entlarvt.
- Die erwarteten Hindernisse für die Interpretierbarkeit sind größtenteils nicht vorhanden.
- Diese Fortschritte sind sowohl für die Sicherheit als auch für die Fähigkeiten von KI-Modellen nützlich.

**🇪🇺 Europa-Relevanz:**
- Der EU AI Act verbietet ab Feb 2025 bestimmte KI-Praktiken und verlangt ab Aug 2026 vollständige Compliance für High-Risk-Systeme; verbesserte Interpretierbarkeit könnte die Einhaltung dieser Vorschriften erleichtern und die Entwicklung sichererer KI-Systeme in der EU fördern.
- Die EU fördert mit InvestAI €200 Mrd. für KI, darunter einen "CERN für KI"-Ansatz, der offene, kooperative Entwicklung komplexester Modelle anstrebt; Interpretierbarkeit ist hierfür entscheidend, um die europäische Vision einer vertrauenswürdigen KI zu realisieren.
- EVP Henna Virkkunen betont die Notwendigkeit, Geschäfte in Europa zu erleichtern, ohne hohe Standards zu kompromittieren; Interpretierbarkeit könnte ein Schlüssel zur Balance zwischen Innovation und Regulierung sein, indem sie die Überprüfbarkeit von KI-Systemen verbessert.

## ☁️ Cloud-Infrastruktur: Oxide Computer Company setzt auf Hardware-Software-Co-Design On-Premise

Bryan Cantrill, Co-Founder und CTO von Oxide Computer Company, beschreibt die "ikonoklastische" Strategie seines Unternehmens, Rack-Scale-Maschinen mit Hardware- und Software-Co-Design für On-Premise-Cloud-Lösungen zu entwickeln. Die Gründung 2019 basierte auf der Erkenntnis, dass Hyperscaler ihre eigenen, integrierten Systeme bauen, während andere Unternehmen auf Commodity-Hardware angewiesen sind, die bei großer Skalierung versagt.

**Konkrete Details aus dem Gespräch:**
- Oxide Computer Company wurde 2019 gegründet, um Rack-Scale-Maschinen mit Hardware- und Software-Co-Design für On-Premise-Cloud-Lösungen anzubieten.
- Das Unternehmen erhielt eine Seed-Finanzierung von $20 Mio. von Eclipse, was 2019 als sehr hohe Summe für eine Seed-Runde galt.
- Oxide verfolgt einen hohen technischen Anspruch, indem es eigene Compute-Sliding, Switches, Firmware und Kontrollsysteme entwickelt und UEFI-Bias eliminiert.
- Das Geschäftsmodell konzentriert sich auf sehr große Kunden und langfristige Beziehungen, im Gegensatz zu einem schnellen Rollout nach einer Einzelrack-Bestellung.
- Ein wichtiger Meilenstein ist das Erreichen von "mehr Racks als Mitarbeiter", was die Effizienz und Skalierbarkeit des Geschäftsmodells unterstreicht.

**🇪🇺 Europa-Relevanz:**
- Die EU mobilisiert €200 Mrd. für KI-Investitionen (InvestAI), darunter €20 Mrd. für 4-5 KI-Gigafactories mit je ~100.000 Next-Gen-AI-Chips; Oxide's Ansatz könnte für den Aufbau souveräner europäischer Rechenzentrumsinfrastruktur relevant sein.
- Rolf Schumann (Co-CEO Schwarz Digits) investiert €11 Mrd. in das Rechenzentrum Lübbenau (Brandenburg) mit bis zu 100.000 GPUs, um Europas "AI Infrastructure Gap" zu schließen – ein potenzieller Markt für integrierte Hardware-Lösungen wie die von Oxide.
- Tim Höttges (Telekom) kritisiert, dass Europa nur 5% der KI-Hochleistungschips nutzt; Oxide's Fokus auf effiziente, co-designte Hardware könnte helfen, diese Lücke zu schließen und die Abhängigkeit von US-Hyperscalern zu reduzieren.

## ⛏️ Unterirdische Infrastruktur: Advanced Spade Company revolutioniert den Bau von Versorgungsleitungen

Daniel Kimminau, Gründer und CEO der Advanced Spade Company und ehemaliger Mitarbeiter der Boring Company, spezialisiert sich auf den Bau unterirdischer Infrastruktur, insbesondere Versorgungsleitungen. Das Unternehmen beginnt mit unbeliebten Nischenarbeiten und nutzt datengestützte Technologie und verbesserte Werkzeuge, um diese effizienter zu gestalten. Dadurch akquiriert es schrittweise größere Projekte und verkauft seine entwickelten Tools an Dritte.

**Konkrete Details aus dem Gespräch:**
- Daniel Kimminau war an der Hyperloop- und Boring Company beteiligt und erkannte dort die Herausforderungen des unterirdischen Baus.
- Advanced Spade Company begann mit "billigster, beschissenster Arbeit, die niemand will" (private Versorgungsleitungssuche) und optimierte diese Prozesse durch Ingenieure und Datenintegration.
- Das Unternehmen erweitert seinen Umfang auf Bohrarbeiten und nutzt dabei gute Datensätze und Karten als Wettbewerbsvorteil.
- Entwickelte Tools werden an kleinere "Mom-and-Pop"-Betriebe verkauft, nachdem Advanced Spade den Markt mit überlegener Effizienz dominiert hat.
- Die Nachfrage nach unterirdischen Leitungen steigt aufgrund von Zuverlässigkeitsproblemen bei oberirdischen Leitungen (z.B. Waldbrände in LA) und dem Bedarf an "trenchless" Lösungen in Städten.
- Der Rechenzentrums-Boom treibt die Nachfrage nach unterirdischer Infrastruktur voran.

**🇪🇺 Europa-Relevanz:**
- In der EU sind Strompreise 2-3x höher als in den USA, und Deutschland hat die höchsten Industriestrompreise; unterirdische Leitungen können die Netzzuverlässigkeit erhöhen und damit indirekt zur Kostensenkung beitragen, was für energieintensive Industrien in der EU entscheidend ist.
- Der Berlin-Anschlag auf das Stromnetz (Jan 2026) hat die Debatte über kritische Infrastruktur (Kritis-Dachgesetz) neu entfacht; Advanced Spade's Fokus auf unterirdische Versorgungsleitungen ist hier direkt relevant für die Resilienz und Sicherheit europäischer Netze.
- Rechenzentren in der EU (z.B. Frankfurt, Irland) stehen unter Druck wegen des hohen Stromverbrauchs und Genehmigungsstopps; effizientere unterirdische Infrastruktur könnte den Ausbau erleichtern und den REPowerEU-Zielen (45% Erneuerbare bis 2030) dienen.

## 💰 KI & Kapitalmärkte: Zinsspitzen durch CAPEX, dann 5% Wachstum als neue Norm

Blake Byers prognostiziert, dass die massive Kapitalverschiebung in KI-bezogene CAPEX in den nächsten zehn Jahren zu einem Anstieg der Zinssätze führen wird. Dies löst zunächst eine kurzfristige Panik aus, da die Schuldendienstkosten für Regierungen und Kreditnehmer (z.B. Immobilienentwickler) steigen. Nach etwa drei Jahren wird sich dies jedoch in Euphorie wandeln, da die Investitionen hohe Renditen abwerfen und 5% Wirtschaftswachstum zur neuen Norm werden.

**Konkrete Details aus dem Gespräch:**
- Kapital verschiebt sich von Staatsanleihen zu Investitionen mit höheren KI-Renditen.
- Kurzfristige Panik durch hohe Zinskosten für Regierungen und Kreditnehmer, was zu Refinanzierungsproblemen und Verkäufen führt.
- Nach drei Jahren wird klar, dass sich die Investitionen auszahlen und die erhöhten Einnahmen die höheren Kreditkosten überkompensieren.
- Wirtschaftswachstum von 5% wird zur neuen Normalität, wobei 10% erwartet werden, um zufrieden zu sein.
- Gesundheitskonsum und Forschung & Entwicklung wachsen als Prozentsatz des BIP.
- Der Anteil der Werbeausgaben am BIP stieg von 1-2% auf 2-3% und könnte weiter steigen.

**🇪🇺 Europa-Relevanz:**
- Der Deutschlandfonds (Dez 2025) mobilisiert €30 Mrd. Garantien und €3,2 Mrd. Eigenmittel, um bis zu €130 Mrd. private Investitionen in DeepTech, KI und Energie zu hebeln – direkt im Einklang mit der These von Byers über die Notwendigkeit von KI-bezogenen CAPEX-Investitionen.
- Kanzler Merz fordert eine F&E-Quote von 3,5% des BIP (aktuell unter 3%) und betont KI als Grundlage für Souveränität und Sicherheit, was die Notwendigkeit von KI-bezogenen CAPEX-Investitionen unterstreicht, um Europas Wettbewerbsfähigkeit zu sichern.
- Die EU AI Champions Initiative (Feb 2025) mit €150 Mrd. Investitionszusage europäischer Unternehmen zielt darauf ab, KI-Technologieunternehmen und kritische Infrastruktur zu fördern, um die europäische Wettbewerbsfähigkeit zu stärken und die Abhängigkeit von externen Kapitalmärkten zu reduzieren.

## 📌 Weitere bemerkenswerte Segmente

**Gersner's Markteinschätzung:** Brad Gersner (CNBC) hat alle Coreweave-Anteile verkauft und 10% seines Portfolios in Meta und Tesla umgeschichtet, da er den KI-Markt als "überschossen" ansieht und eine Konsolidierungsphase erwartet. (TBPN)

**Valar Atomics VC-Streit:** Isaiah Taylor (Valar Atomics) befindet sich in einem öffentlichen Streit mit Day One Ventures über Pro-Rata-Rechte, da Day One kontroverse internationale Verbindungen hat, was die Komplexität von VC-Beziehungen und die Bedeutung von Informationsrechten aufzeigt. (TBPN)

**Open Source Alliance & Regulierung:** Reed Albergotti diskutiert, dass Hyperscaler Open Source KI verbieten möchten, aber die rechtliche Umsetzung schwierig ist, während die Marktkapitalisierung von Befürwortern (z.B. Nvidia) die politische Debatte beeinflusst. (TBPN)

# 💭 Zum Drüber Nachdenken

**Europas KI-Gigafactory-Träume kollidieren mit der US-Realität der "Dezeleration" – ist der €200 Mrd. InvestAI-Plan schon veraltet?**
Kontext: Anthropic wächst mit 45% QoQ, verfehlt aber 10x-Erwartungen, was den US-KI-Markt erschüttert. Gleichzeitig plant die EU mit InvestAI €200 Mrd. für KI, darunter €20 Mrd. für 4-5 Gigafactories (z.B. Schwarz Digits Lübbenau mit €11 Mrd. und 100.000 GPUs). Die US-Diskussion um "Tall Poppy Syndrome" und die Abwanderung von Kapital aus überbewerteten KI-Aktien zeigt, dass selbst explosives Wachstum nicht ausreicht, wenn die Erwartungen utopisch sind.
Die Frage dahinter: Kann Europa mit seinem "CERN für KI"-Ansatz und dem Fokus auf souveräne Infrastruktur die "Dezeleration" im US-Markt als Chance nutzen, oder droht die europäische Strategie, auf überzogenen Erwartungen aufzubauen, die bereits in den USA korrigiert werden?

**Während US-Investoren auf 5% Wirtschaftswachstum durch AGI hoffen, kämpft Europa mit 2-3x höheren Strompreisen – ist die "AI-Infrastructure Gap" unüberwindbar?**
Kontext: Blake Byers prognostiziert, dass KI-CAPEX die Zinsen in den USA in die Höhe treibt, aber nach drei Jahren zu 5% Wirtschaftswachstum führt. In Europa sind die Strompreise 2-3x höher als in den USA, und Deutschland hat die höchsten Industriestrompreise. Tim Höttges (Telekom) warnt, dass Europa nur 5% der KI-Hochleistungschips nutzt. Initiativen wie der Deutschlandfonds (€130 Mrd. mobilisiert) und das €11 Mrd. Rechenzentrum Lübbenau sollen gegensteuern.
Die Frage dahinter: Kann Europa die notwendigen Infrastrukturinvestitionen tätigen und die Energiepreise senken, um mit dem prognostizierten US-Wachstum Schritt zu halten, oder wird die "AI-Infrastructure Gap" die europäische Wettbewerbsfähigkeit langfristig untergraben, selbst wenn die US-Zinsen steigen?