import requests
from bs4 import BeautifulSoup
import datetime
import os

# 1. Die URL der Podcast-Übersicht
BASE_URL = "https://podscripts.co/podcasts/tbpn-live/"
DOMAIN = "https://podscripts.co"

def scrape_latest_transcript():
    # Webseite abrufen
    print("Rufe Übersichtsseite ab...")
    response = requests.get(BASE_URL)
    response.raise_for_status() # Prüfen ob der Abruf erfolgreich war
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 2. Den Link zur neuesten Episode finden
    # (Auf Podscripts sind die Titel der Episoden in der Regel als Links <a> hinterlegt)
    # Wir suchen nach dem ersten Link, der nach einer Episode aussieht.
    # Alternativ sucht man nach einer spezifischen CSS-Klasse (z.B. der Box, die die Episode enthält).
    
    # Hier suchen wir alle Links, die "/episodes/" im Pfad haben könnten oder spezifische Podcast-Links sind.
    # HINWEIS: Je nach exaktem HTML-Code der Seite muss der Selektor leicht angepasst werden.
    links = soup.find_all('a', href=True)
    episode_link = None
    
    for link in links:
        href = link['href']
        # Prüfen, ob der Link zu einer Episode führt (meistens beinhalten diese die ID oder den Titel)
        if "/episodes/" in href or "/podcasts/tbpn-live/" in href:
            # Überspringe Links, die nur Paginierung sind (wie Seite 2, 3)
            if "page=" not in href and href != "/podcasts/tbpn-live/":
                episode_link = href
                break
                
    if not episode_link:
        print("Kein Episoden-Link gefunden. Hat sich das Layout geändert?")
        return

    # Falls der Link relativ ist (z.B. /episodes/123), fügen wir die Domain hinzu
    if episode_link.startswith("/"):
        full_url = DOMAIN + episode_link
    else:
        full_url = episode_link

    print(f"Neueste Episode gefunden: {full_url}")

    # 3. Episoden-Seite abrufen und Transkript extrahiert
    ep_response = requests.get(full_url)
    ep_soup = BeautifulSoup(ep_response.text, 'html.parser')
    
    # Hier suchen wir den Bereich, der das Transkript enthält. 
    # Oft ist das ein <div> mit einer bestimmten Klasse wie 'transcript', 'content' oder 'entry-content'.
    # Da wir den HTML-Code nicht zu 100% sehen, suchen wir nach gängigen Mustern:
    transcript_div = ep_soup.find('div', class_=lambda c: c and 'transcript' in c.lower())
    
    # Wenn es keine Klasse "transcript" gibt, nehmen wir alle Absätze (<p>) als Fallback
    if transcript_div:
        text = transcript_div.get_text(separator="\n\n", strip=True)
    else:
        paragraphs = ep_soup.find_all('p')
        text = "\n\n".join([p.get_text(strip=True) for p in paragraphs])

    # 4. In einer Textdatei speichern (mit heutigem Datum im Namen)
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"TBPN_Transcript_{today}.txt"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"URL: {full_url}\n")
        file.write("="*50 + "\n\n")
        file.write(text)
        
    print(f"Erfolg! Das Transkript wurde unter '{filename}' gespeichert.")

if __name__ == "__main__":
    scrape_latest_transcript()
