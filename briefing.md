# 📋 Executive Summary

| Thema | Zentrale These | Person(en) | Quelle |
|-------|---------------|------------|--------|
| Sicherheit vs. Privatsphäre | Flock Safety, ein Anbieter von Kennzeichenlesern (LPRs), steht im Zentrum einer Debatte über das Gleichgewicht zwischen Sicherheit und Privatsphäre, da seine Technologie in über 6.000 US-Städten zur Kriminalitätsbekämpfung eingesetzt wird. | Garrett Langley (CEO, Flock), Jason (Host) | All-In |
| Daten-Governance & Missbrauch | Flock hat seine Standards für Datenspeicherung und -zugriff verschärft und verlangt nun von allen Kunden die Nutzung eines Tools zur Erkennung abnormaler Suchmuster, um Missbrauch durch Strafverfolgungsbehörden zu verhindern. | Garrett Langley (CEO, Flock), Jason (Host) | All-In |
| KI in öffentlicher Sicherheit & Drohnen | Flock geht bei der Integration von KI in die öffentliche Sicherheit vorsichtig vor, um Risiken wie Halluzinationen in 911-Systemen zu vermeiden, während Drohnen als schnell wachsendes Geschäftsfeld zur Risikominderung bei Notrufen eingesetzt werden. | Garrett Langley (CEO, Flock), Jason (Host) | All-In |

# 🎙 Deep-Dive: Die Kern-Analysen

## ⚖️ Sicherheit vs. Privatsphäre: Flock Safetys Balanceakt

Garrett Langley (CEO, Flock) beschreibt die Mission seines Unternehmens, Nachbarschaften sicherer zu machen, indem es Kennzeichenleser (LPRs) und Drohnen bereitstellt. Trotz des Erfolgs bei der Kriminalitätsbekämpfung und dem Auffinden vermisster Personen steht Flock im Zentrum einer intensiven Debatte über Privatsphäre. Langley betont, dass Flock bewusst auf Funktionen wie Gesichtserkennung und Videoaufnahmen verzichtet, die von Wettbewerbern angeboten werden, um einen "privacy-first" Ansatz zu verfolgen. Die Diskussion über die Technologie wird oft von Missinformationen und unterschiedlichen Perspektiven geprägt, wobei ärmere Gemeinden die Technologie oft als notwendiges Mittel zur Erhöhung der Sicherheit sehen.

**Konkrete Details aus dem Gespräch:**
- Flock wurde vor neun Jahren gegründet, um Nachbarschaften sicherer zu machen, und ist in über 6.000 US-Städten aktiv.
- Die Technologie erfasst Standbilder von Fahrzeugen, liest Kennzeichen und kann Details wie Dachgepäckträger, Aufkleber oder Schäden erkennen.
- Im letzten Jahr wurden über eine Million Verbrechen mit Flock gelöst und über 10.000 vermisste Personen gefunden.
- Flock verzichtet auf Gesichtserkennung, Videoaufnahmen und die Möglichkeit, Personen zu suchen, im Gegensatz zu einigen Wettbewerbern.
- Einige Städte haben Kameras aufgrund von Missinformationen oder Protesten entfernt, aber viele haben sie später wieder eingeschaltet, nachdem die Kriminalität gestiegen war.
- Die Debatte wird oft von Menschen geführt, die sich aufgrund ihres Privilegs keine Sorgen um Kriminalität machen müssen, während ärmere Gemeinden die Technologie zur Selbstverteidigung benötigen.

**🇪🇺 Europa-Relevanz:**
- Flocks "privacy-first" Ansatz (keine Gesichtserkennung, keine Videosuche nach Personen) steht im Einklang mit den strengen Anforderungen des EU AI Act für Hochrisiko-KI-Systeme, die ab Aug 2026 vollständig compliant sein müssen.
- Die Diskussion um die Datenspeicherung (7-30 Tage in den USA) ist relevant für die GPAI-Transparenzpflichten, die ab Aug 2025 in Kraft treten und von 26 Anbietern (u.a. Microsoft, Google, Amazon, OpenAI, Anthropic) unterzeichnet wurden.
- EVP Henna Virkkunen prüft mit dem Digital Fitness Check (Konsultation bis 11. März 2026) die Wechselwirkung aller EU-Digitalgesetze, was auch die Balance zwischen Sicherheit und Datenschutz betrifft und die Relevanz der US-Debatte für europäische Gesetzgeber unterstreicht.

## 🔒 Daten-Governance & Missbrauchsprävention bei Polizeitechnologien

Garrett Langley (CEO, Flock) erläutert, wie Flock seine Verantwortung als Technologieanbieter weiterentwickelt hat, um Missbrauch durch Strafverfolgungsbehörden zu verhindern. Das Unternehmen hat die Standard-Datenspeicherdauer von 30 auf 7 Tage reduziert, wobei die endgültige Entscheidung über die Dauer bei den demokratisch gewählten lokalen Regierungen liegt. Flock hat ein neues "Audit Assistance"-Tool eingeführt, das anomale Suchmuster erkennt, die auf Missbrauch hindeuten, und dieses Tool für alle Kunden obligatorisch gemacht. Diese Maßnahme hat bereits zur Entlassung von "vielen schlechten Polizisten" geführt, was die Wirksamkeit des Systems unterstreicht. Flock ist bereit, Kunden zu verlieren, die keine Rechenschaftspflicht wünschen.

**Konkrete Details aus dem Gespräch:**
- Die Entscheidung über die Datenspeicherdauer liegt bei den demokratisch gewählten Stadt- oder Staatsräten; der Standard von Flock wurde von 30 auf 7 Tage reduziert.
- 90% der Verbrechen werden voraussichtlich innerhalb von sieben Tagen gelöst, aber 10% (z.B. Mord, Vergewaltigung) erfordern längere Datenretention.
- Flock erkannte, dass das Vertrauen in die Polizei ein Kernproblem ist und dass Machtpositionen Missbrauch begünstigen können.
- Ein neues "Audit Assistance"-Tool wurde entwickelt, das anomale Suchmuster (z.B. wiederholte Suche nach demselben Fahrzeug) erkennt, die auf Missbrauch hindeuten.
- Dieses Tool ist jetzt eine obligatorische Funktion für alle Kunden, was zur Entlassung von "vielen schlechten Polizisten" geführt hat.
- Flock ist bereit, Kunden zu verlieren, die keine Rechenschaftspflicht wünschen, da dies langfristig dem Unternehmen schaden würde.

**🇪🇺 Europa-Relevanz:**
- Flocks "Audit Assistance"-Tool zur Erkennung von Missbrauch durch Beamte ist ein konkretes Beispiel für die "Human in the Loop"-Anforderung des EU AI Act für Hochrisiko-Systeme (z.B. im Bereich Strafverfolgung), die ab Aug 2026 gelten.
- Die Bußgelder für Verstöße gegen den EU AI Act können bis zu €35 Mio. oder 7% des Umsatzes betragen, was die Notwendigkeit robuster Missbrauchserkennungssysteme wie dem von Flock unterstreicht und die Relevanz für europäische Technologieanbieter und Behörden erhöht.
- Der Digital Omnibus, der aktuell das Gesetzgebungsverfahren durchläuft, erlaubt unter strengen Auflagen die Bias-Erkennung mit sensiblen Daten, was die Relevanz von Audits und Missbrauchserkennung für EU-Anbieter erhöht.

## 🤖 KI in öffentlicher Sicherheit & Drohneneinsatz

Garrett Langley (CEO, Flock) betont die vorsichtige Herangehensweise von Flock an die Integration von Künstlicher Intelligenz in die öffentliche Sicherheit. Das Unternehmen lehnt den Einsatz von KI zur "Definition von Verdacht" oder für prädiktive Polizeiarbeit ab und besteht auf einem "Human in the Loop"-Ansatz. Gleichzeitig sind Drohnen zu einem schnell wachsenden Geschäftsfeld für Flock geworden. Diese Drohnen können bei 911-Anrufen vor einem Beamten entsandt werden, um Situationen zu bewerten und Risiken zu mindern, wie ein Beispiel zeigte, bei dem ein vermeintlicher bewaffneter Mann als Person mit einem Spielzeugfeuerzeug identifiziert wurde. Langley weist auf die mangelnde Regulierung für Drohneneinsätze in den USA hin.

**Konkrete Details aus dem Gespräch:**
- Flock vermeidet die Nutzung von KI zur "Definition von Verdacht" oder für prädiktive Polizeiarbeit und betont die Notwendigkeit eines "Human in the Loop".
- Es gibt Bedenken hinsichtlich des Einsatzes von KI in 911-Systemen aufgrund des hohen Risikos von Fehlern ("Halluzinationen") bei kritischen Situationen.
- Drohnen sind Flocks am schnellsten wachsendes Geschäftsfeld und werden typischerweise von Polizeidienststellen oder Feuerwehren von Docks auf Dächern gestartet.
- Drohnen können bei 911-Anrufen vor einem Beamten entsandt werden, fliegen mit 60 mph in unter einer Minute zum Einsatzort und verfügen über einen 40-fachen optischen Zoom.
- Ein Beispiel zeigte, wie eine Drohne einen vermeintlichen bewaffneten Mann als Person mit einem Spielzeugfeuerzeug identifizierte, wodurch eine potenziell gefährliche Situation entschärft wurde.
- Es gibt kaum staatliche und keine bundesweite Regulierung für Drohneneinsätze in den USA, abgesehen von der Flugsicherheit.

**🇪🇺 Europa-Relevanz:**
- Flocks vorsichtiger Ansatz bei KI in 911-Systemen spiegelt die Bedenken des EU AI Act wider, der KI in kritischen Infrastrukturen (z.B. Notfalldienste) als Hochrisiko einstuft und strenge Anforderungen an Robustheit und menschliche Aufsicht stellt, die ab Aug 2026 gelten.
- Die fehlende Regulierung für Drohneneinsätze in den USA steht im Gegensatz zu den umfassenden EU-Regulierungsbemühungen, die auch den Einsatz von KI-gestützten Drohnen in öffentlichen Diensten betreffen könnten und im Kritis-Dachgesetz diskutiert werden.
- Die €200 Mrd. InvestAI-Initiative der EU zielt darauf ab, KI-Gigafactories zu schaffen, die auch die Infrastruktur für solche KI-Anwendungen bereitstellen sollen, wobei die "Majority owners should come from Europe" Regelung die Kontrolle über solche Technologien sichern soll.

## 📌 Weitere bemerkenswerte Segmente

Die Diskussion berührte auch die Herausforderungen der öffentlichen Wahrnehmung und der Kommunikation, wobei Flock im letzten Jahr mit einer "PR-Katastrophe" konfrontiert war, die die interne Moral beeinträchtigte. Jason verglich Flocks Situation mit der von Mark Zuckerberg (Facebook), der ebenfalls lernen musste, proaktiv mit den negativen Auswirkungen seiner Technologien umzugehen. Trotzdem ist das Geschäft von Flock in guter Verfassung und wächst weiter, auch wenn das Unternehmen bereit ist, Kunden zu verlieren, die keine Rechenschaftspflicht akzeptieren.

# 💭 Zum Drüber Nachdenken

**Europas KI-Regulierungs-Korsett: Bremse für die Sicherheit oder Schutzschild vor dem Überwachungsstaat?**
Kontext: Während US-Gemeinden wie Austin nach Kriminalitätsspitzen Flock-Kameras (LPRs) mit 7-30 Tagen Datenspeicherung wieder aktivieren, um die Sicherheit zu erhöhen, reguliert die EU mit dem AI Act Hochrisiko-KI-Systeme umfassend. EVP Virkkunen betont die Notwendigkeit, "doing business in Europe easier without compromising our high standards", doch die Debatte um Flock zeigt, dass die Balance zwischen Sicherheit und Privatsphäre auch in den USA eine Herausforderung ist. Die EU mobilisiert €200 Mrd. für InvestAI, um eine "CERN für KI" zu schaffen, aber die Frage bleibt, wie schnell und flexibel europäische Städte datengestützte Sicherheitslösungen implementieren können.
Die Frage dahinter: Kann Europa seine hohen Standards halten und gleichzeitig effektive, datengestützte Sicherheitslösungen wie Flock schnell implementieren, oder führt die Regulierung zu einem "AI Infrastructure Gap" im Kampf gegen Kriminalität?

**Flocks 'Bad Cop'-Jäger: Ein Weckruf für Europas fragmentierte Polizeisysteme?**
Kontext: Flock hat mit seinem "Audit Assistance"-Tool Dutzende "Bad Cops" entlarvt, die das System missbrauchten, und macht dieses Tool für alle Kunden obligatorisch. Gleichzeitig fehlt in den USA eine umfassende Regulierung für den Einsatz von Drohnen durch die Polizei. In Europa, wo der EU AI Act ab Aug 2026 strenge Anforderungen an die menschliche Aufsicht und Robustheit von KI-Systemen stellt, könnten solche Tools zur Missbrauchserkennung als Best Practice dienen. Die Mainzer Erklärung der Merz-Regierung betont die Notwendigkeit von KI für Souveränität und Sicherheit, aber die Implementierung von Rechenschaftspflicht und Transparenz in fragmentierten Polizeisystemen bleibt eine Herausforderung.
Die Frage dahinter: Sollte die EU, angesichts der US-Erfahrungen mit Missbrauch und fehlender Drohnenregulierung, proaktiv europaweite Standards für Audit-Trails und Transparenz bei Polizeitechnologien einführen, um das Vertrauen der Bürger zu stärken und die Durchsetzung des AI Act zu untermauern?