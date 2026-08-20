# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| Sicherheit vs. Privatsphäre | Flock Safety bietet Lizenzkennzeichenleser (LPRs) und Drohnen an, die in über 6.000 US-Städten zur Kriminalitätsbekämpfung und Personensuche eingesetzt werden, wobei die Balance zwischen Sicherheit und Privatsphäre durch lokale Entscheidungen über Datenaufbewahrung und -zugriff gefunden werden muss. | Garrett Langley (Flock CEO) | All-In |
| Missbrauchsprävention | Flock Safety hat ein neues "Audit Assistance"-Tool eingeführt, das abnormales Nutzungsverhalten von Polizeibeamten erkennt und Missbrauch des Systems aufdeckt, um die Rechenschaftspflicht zu erhöhen und das Vertrauen in die Technologie zu stärken. | Garrett Langley (Flock CEO) | All-In |
| KI-Einsatz in der Sicherheit | Flock Safety verfolgt einen vorsichtigen Ansatz bei der Integration von KI in die öffentliche Sicherheit, indem es den "Human in the Loop" betont und die Definition von "Verdacht" durch KI ablehnt, um die Risiken von Halluzinationen und Fehlentscheidungen zu minimieren. | Garrett Langley (Flock CEO) | All-In |
| Drohnen in der Sicherheit | Drohnen sind ein schnell wachsendes Geschäftsfeld für Flock Safety, die zur Deeskalation von potenziell gefährlichen Situationen eingesetzt werden können, erfordern jedoch massive Schutzmaßnahmen und Transparenz, da es kaum staatliche oder bundesweite Regulierung gibt. | Garrett Langley (Flock CEO) | All-In |

# 🎙 Deep-Dive: Die Kern-Analysen

## ⚖️ Sicherheit vs. Privatsphäre: Flock Safety und die lokale Autonomie

Garrett Langley (Flock CEO) beschreibt die Mission von Flock Safety, Nachbarschaften sicherer zu machen, indem Lizenzkennzeichenleser (LPRs) und Drohnen eingesetzt werden. Das Unternehmen ist in über 6.000 US-Städten aktiv und hat maßgeblich zur Lösung von über einer Million Verbrechen und zum Auffinden von über 10.000 vermissten Personen beigetragen. Die Entscheidung über die Installation der Kameras und die Dauer der Datenspeicherung liegt bei den demokratisch gewählten Stadträten, wobei der Standard für die Datenspeicherung von 30 auf 7 Tage reduziert wurde.

**Konkrete Details aus dem Gespräch:**
- Flock Safety wurde vor neun Jahren gegründet, um Nachbarschaften sicherer zu machen.
- Die Kerntechnologie sind LPR-Kameras, die Standbilder von Fahrzeugen aufnehmen, Kennzeichen lesen und Merkmale wie Dachgepäckträger oder Schäden erkennen.
- Über eine Million Verbrechen wurden mithilfe von Flock gelöst und über 10.000 vermisste Personen gefunden.
- Flock ist in über 6.000 Städten in den USA im Einsatz.
- Die Kameras erfassen keine Gesichtserkennung, keine Videos und blicken nicht ins Fahrzeuginnere; es ist auch nicht möglich, im System nach Personen zu suchen.
- Die Entscheidung über die Installation und die Dauer der Datenspeicherung (standardmäßig 7 Tage, früher 30 Tage) liegt bei den demokratisch gewählten Stadträten.
- 90% der Verbrechen können innerhalb von sieben Tagen gelöst werden, aber komplexere Fälle erfordern längere Speicherfristen.

**🇪🇺 Europa-Relevanz:**
- Der EU AI Act, der ab August 2026 für High-Risk-KI-Systeme vollständig compliant sein muss, könnte die Implementierung von LPR-Systemen in der EU erschweren, da diese als biometrische Systeme eingestuft werden könnten und strenge Anforderungen an Transparenz und Datenschutz erfüllen müssten.
- Die EU-Kommission hat im Digital Omnibus (Nov 2025) vorgeschlagen, die High-Risk-Deadline um bis zu 16 Monate zu verschieben (Backstop: Dez 2027), was der Industrie mehr Zeit für die Anpassung an solche Technologien geben könnte.
- Die unterschiedlichen Datenaufbewahrungsfristen in den USA (7-30 Tage, New Hampshire 3 Minuten) stehen im Kontrast zu den strengen Datenschutzanforderungen der EU, die eine Zweckbindung und Minimierung der Datenverarbeitung vorschreiben.

## 👮 Missbrauchsprävention und Rechenschaftspflicht bei Überwachungstechnologien

Garrett Langley (Flock CEO) thematisiert die Bedenken hinsichtlich des Missbrauchs von Überwachungssystemen durch "schmutzige Polizisten". Flock hat darauf reagiert, indem es ein neues "Audit Assistance"-Tool eingeführt hat. Dieses Tool erkennt abnormales Nutzungsverhalten, wie wiederholte Suchanfragen nach demselben Fahrzeug, und hat bereits zahlreiche Fälle von Missbrauch aufgedeckt, was zu Entlassungen von Beamten führte. Das "Audit Assistance"-Tool ist nun eine obligatorische Funktion für alle Flock-Kunden.

**Konkrete Details aus dem Gespräch:**
- Die Sorge vor Missbrauch durch "schmutzige Polizisten" ist ein zentrales Thema, da jedes datenaufzeichnende System missbraucht werden kann.
- Flock hatte bereits Audit-Logs, erkannte aber, dass diese bei großen Polizeibehörden nicht effektiv manuell überprüft werden konnten.
- Das neue "Audit Assistance"-Tool, das vor vier Monaten eingeführt wurde, nutzt Mustererkennung, um ungewöhnliche Suchanfragen (z.B. wiederholte Suche nach demselben Fahrzeug über Tage hinweg) zu identifizieren.
- Das Tool hat bereits "viele schlechte Polizisten" überführt, was zu Entlassungen führte (z.B. neun Beamte in Georgia).
- "Audit Assistance" ist jetzt eine obligatorische Funktion für alle Flock-Kunden.
- Garrett Langley betont, dass die Verantwortung für die Prävention von Missbrauch beim Technologieanbieter liegt, auch wenn es sich um ein "Werkzeug" handelt.
- In Kalifornien gab es im letzten Jahr 7.000 gemeldete Missbräuche der staatlichen Datenbank, was die Notwendigkeit solcher Tools unterstreicht.

**🇪🇺 Europa-Relevanz:**
- Das "Audit Assistance"-Tool von Flock könnte als Best Practice für die Einhaltung der strengen Anforderungen des EU AI Act dienen, insbesondere für High-Risk-KI-Systeme, die ab August 2026 umfassende Überwachungs- und Rechenschaftspflichten erfüllen müssen (Bußgelder bis €35 Mio. / 7% Umsatz).
- Das EU AI Office, das ab August 2025 operativ ist, könnte solche Tools zur Überwachung der GPAI-Transparenzpflichten und zur Durchsetzung des Code of Practice nutzen, um Missbrauch in europäischen KI-Systemen zu verhindern.
- Die Mainzer Erklärung (Jan 2026) der Merz-Regierung betont KI als "Grundlage für Souveränität und Sicherheit", was die Notwendigkeit vertrauenswürdiger und missbrauchssicherer Technologien unterstreicht.

## 🤖 KI-Einsatz in der öffentlichen Sicherheit – Chancen und Risiken

Garrett Langley (Flock CEO) erläutert den vorsichtigen Ansatz von Flock Safety bei der Integration von Künstlicher Intelligenz (KI) in die öffentliche Sicherheit. Das Unternehmen lehnt es ab, KI zur Definition von "Verdacht" einzusetzen und betont die Notwendigkeit eines "Human in the Loop", da es bei der öffentlichen Sicherheit um Menschenleben geht. Er warnt vor einem "rücksichtslosen" Einsatz von KI, wie er bei 911-Systemen beobachtet wird, und fordert eine unabhängige "Third-Party Proper Attestation", um die Zuverlässigkeit und Objektivität von KI-Produkten zu gewährleisten.

**Konkrete Details aus dem Gespräch:**
- Flock geht bei der Einführung von KI-Funktionen bewusst "sehr langsam" vor.
- Das Unternehmen lehnt es ab, KI zur Definition von "Verdacht" einzusetzen, da dies als "wirklich gefährlich" erachtet wird.
- Ein "Human in the Loop" ist bei der öffentlichen Sicherheit unerlässlich, da es um Menschenleben geht.
- Als Beispiel für riskanten KI-Einsatz werden 911-Systeme genannt, bei denen KI-Bots bei Notrufen fehlerhaft reagieren könnten.
- Ein "smarterer" KI-Einsatz wäre, KI nur dann zu aktivieren, wenn Telefonleitungen vollständig ausgelastet sind.
- KI-Produkte sollten mit "Third-Party Proper Attestation" (externer, unabhängiger Bestätigung) eingesetzt werden, um sicherzustellen, dass sie wie erwartet funktionieren und Beamte effektiver und objektiver machen.
- Das Ziel ist, die Anzahl der gelösten Verbrechen zu erhöhen und die Wahrscheinlichkeit zu verringern, die falsche Person zu identifizieren.

**🇪🇺 Europa-Relevanz:**
- Der von Flock betonte "Human in the Loop"-Ansatz ist eine Kernanforderung des EU AI Act für High-Risk-KI-Systeme, um menschliche Aufsicht und Kontrolle über KI-Entscheidungen zu gewährleisten und Risiken wie "Halluzinationen" zu minimieren.
- Die Forderung nach "Third-Party Proper Attestation" für KI-Produkte entspricht dem EU-Ansatz der Konformitätsbewertung und externen Audits, die für High-Risk-KI-Systeme verpflichtend sind, um deren Sicherheit und Zuverlässigkeit zu bestätigen.
- EVP Henna Virkkunen (Tech-Souveränität) betont, dass Europa "doing business easier" machen muss, ohne "high standards" zu kompromittieren – ein Spannungsfeld, das Flock's vorsichtiger KI-Ansatz in den USA widerspiegelt.

## 🚁 Drohnen in der öffentlichen Sicherheit – Deeskalation und Transparenz

Garrett Langley (Flock CEO) hebt hervor, dass Drohnen die am schnellsten wachsende Geschäftseinheit von Flock Safety sind. Diese Drohnen werden in speziellen Docks auf Dächern gelagert und können bei 911-Anrufen entsandt werden, um Situationen zu deeskalieren, bevor Beamte eintreffen. Ein Beispiel zeigt, wie eine Drohne ein vermeintliches Gewehr als Feuerzeug identifizierte und so eine potenziell gefährliche Konfrontation verhinderte. Langley betont die Notwendigkeit massiver Schutzmaßnahmen und Transparenz, da es kaum spezifische staatliche oder bundesweite Regulierung für Drohneneinsätze in der öffentlichen Sicherheit gibt.

**Konkrete Details aus dem Gespräch:**
- Drohnen sind derzeit die am schnellsten wachsende Geschäftseinheit von Flock.
- Die Drohnen sind in HVAC-Kontrollboxen auf Dächern (z.B. Polizeireviere, Feuerwehren) untergebracht und können bei 911-Anrufen anstelle von Beamten entsandt werden.
- Sie fliegen in 400 Fuß Höhe mit 60 Meilen pro Stunde und erreichen den Einsatzort in weniger als einer Minute.
- Mit einem 40-fachen optischen Zoom können sie Details aus der Ferne erkennen, wie im Beispiel eines Mannes mit einem vermeintlichen Gewehr, das sich als Feuerzeug herausstellte.
- Dieser Einsatz führte zur Deeskalation einer potenziell gefährlichen Situation und erhöhte das Sicherheitsgefühl der Anruferin.
- Es gibt derzeit keine staatliche oder bundesweite Regulierung für den Einsatz von Drohnen in der öffentlichen Sicherheit, außer für die Flugsicherheit.
- Flock-Kunden haben Transparenzportale, die Audit-Logs und Drohnenflüge anzeigen können (mit einer Verzögerung, um aktive Ermittlungen nicht zu gefährden).
- Die Branche muss Entscheidungen über Standard-Defaults für Drohneneinsätze treffen, ähnlich wie bei LPRs.

**🇪🇺 Europa-Relevanz:**
- Die fehlende spezifische Regulierung für Drohneneinsätze in der öffentlichen Sicherheit in den USA steht im Kontrast zu den strengeren EU-Regularien für Drohnen (z.B. EASA-Vorschriften) und dem Kritis-Dachgesetz in Deutschland, das die Sicherheit kritischer Infrastrukturen (inkl. möglicher Drohnen-Einsätze) regelt.
- Die Diskussion um Transparenzportale und Audit-Logs für Drohnenflüge in den USA könnte als Vorbild für die Entwicklung von EU-weiten Standards dienen, um die Akzeptanz dieser Technologien zu erhöhen und gleichzeitig die Privatsphäre zu schützen.
- Die Merz-Regierung hat einen Nationalen Sicherheitsrat eingerichtet und plant ein neues Wehrdienstgesetz, was die Bedeutung von Sicherheitstechnologien wie Drohnen für die Verteidigung und innere Sicherheit unterstreicht, aber auch die Notwendigkeit klarer Einsatzregeln.

## 📌 Weitere bemerkenswerte Segmente

Flock Safety sah sich im letzten Jahr mit einer "PR-Katastrophe" konfrontiert, da die Öffentlichkeit die Technologie oft falsch versteht und fälschlicherweise Gesichtserkennung oder permanente Aufzeichnungen annimmt. Das Unternehmen arbeitet daran, seine Kommunikation zu verbessern, um Missverständnisse zu beseitigen und die Funktionsweise der Technologie transparent zu machen. Im Wettbewerbsumfeld grenzt sich Flock von Konkurrenten ab, die "rücksichtsloser" agieren und keine vergleichbaren Tools zur Rechenschaftspflicht anbieten, wobei Flock bereit ist, Kunden zu verlieren, die diese Standards nicht akzeptieren wollen.

# 💭 Zum Drüber Nachdenken

**Trumps Kraftwerks-Zwang entlarvt Europas Rechenzentrum-Illusion**
Kontext: Während US-Städte über die Balance zwischen Sicherheit und Privatsphäre bei Überwachungstechnologien wie LPRs und Drohnen debattieren, steht Europa vor der fundamentaleren Frage, ob es die notwendige Infrastruktur für KI überhaupt bereitstellen kann. Tim Höttges (Telekom) warnt, dass Europa nur 5% der KI-Hochleistungschips nutzt, verglichen mit 70% in den USA. Projekte wie das €11-Mrd.-Rechenzentrum Lübbenau von Schwarz Digits und die €200 Mrd. schwere InvestAI-Initiative sollen gegensteuern, doch die regulatorische Asymmetrie und die hohen Energiepreise in der EU könnten die Wettbewerbsfähigkeit weiter untergraben.
Die Frage dahinter: Kann Europa seine "Tech-Souveränität" wirklich erreichen, wenn es bei der physischen KI-Infrastruktur so massiv hinterherhinkt und gleichzeitig US-Ansätze als "autoritäre Zensur" kritisiert?

**Der "Dirty Cop"-Algorithmus: Europas Chance für vertrauenswürdige KI-Überwachung?**
Kontext: Flock Safety hat mit seinem "Audit Assistance"-Tool erfolgreich "schmutzige Polizisten" überführt, die Überwachungssysteme missbrauchten – ein obligatorisches Feature, das abnormales Nutzungsverhalten erkennt. In der EU tritt der AI Act ab August 2026 für High-Risk-KI-Systeme in Kraft, mit potenziellen Bußgeldern bis €35 Mio. EVP Henna Virkkunen betont die Notwendigkeit, Geschäfte in Europa zu erleichtern, ohne hohe Standards zu kompromittieren, und der Digital Omnibus könnte die High-Risk-Deadline bis zu 16 Monate verschieben.
Die Frage dahinter: Sollte Europa die US-Erfahrungen mit Missbrauchsprävention aktiv in die Entwicklung und Implementierung von KI-Systemen für die öffentliche Sicherheit integrieren, um von Anfang an Vertrauen aufzubauen und den AI Act als Chance für "Privacy-by-Design"-Lösungen zu nutzen, anstatt nur zu regulieren?