import requests
from bs4 import BeautifulSoup
import datetime

BASE_URL = "https://podscripts.co/podcasts/tbpn-live/"
DOMAIN = "https://podscripts.co"

def scrape_latest():
    print("Suche nach der neuesten Episode...")
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Findet den Link der neuesten Folge
    first_episode = soup.select_one('div.col-md-8 a[href*="/podcasts/tbpn-live/"]')
    
    if not first_episode:
        print("Keine Episode gefunden.")
        return

    ep_url = DOMAIN + first_episode['href'] if first_episode['href'].startswith('/') else first_episode['href']
    
    ep_res = requests.get(ep_url)
    ep_soup = BeautifulSoup(ep_res.text, 'html.parser')
    
    title = ep_soup.find('h1').get_text(strip=True) if ep_soup.find('h1') else "Unbekannter Titel"
    transcript_parts = ep_soup.select('div#transcript p, div.transcript-row p')
    
    if not transcript_parts:
        transcript_parts = ep_soup.find_all('p')

    full_text = "\n\n".join([p.get_text(strip=True) for p in transcript_parts])

    # SPEICHERN: Einmal mit Datum und einmal als 'latest.txt'
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    # Datei 1 (Archiv):
    filename = f"Transcript_{date_str}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Titel: {title}\nQuelle: {ep_url}\n\n{full_text}")
    
    # Datei 2 (Für Gemini):
    with open("latest.txt", "w", encoding="utf-8") as f:
        f.write(f"Titel: {title}\nQuelle: {ep_url}\n\n{full_text}")
    
    print(f"Erfolg! Archiv unter '{filename}' und aktuelle Version unter 'latest.txt' gespeichert.")

if __name__ == "__main__":
    scrape_latest()
