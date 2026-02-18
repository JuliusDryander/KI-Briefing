import requests
from bs4 import BeautifulSoup
import datetime

# Ziel-URL
BASE_URL = "https://podscripts.co/podcasts/tbpn-live/"
DOMAIN = "https://podscripts.co"

def scrape_latest():
    print("Suche nach der neuesten Episode...")
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Suche alle Links, die mit dem Podcast-Pfad beginnen
    all_links = soup.find_all('a', href=True)
    first_episode_link = None
    
    for link in all_links:
        href = link['href']
        # Wir suchen einen Link, der länger ist als die Basis-URL und keine Seitenzahl ist
        if href.startswith("/podcasts/tbpn-live/") and len(href) > len("/podcasts/tbpn-live/") and "page=" not in href:
            first_episode_link = href
            break
    
    if not first_episode_link:
        print("Keine Episode gefunden. Prüfe die Struktur der Seite.")
        return

    ep_url = DOMAIN + first_episode_link if first_episode_link.startswith('/') else first_episode_link
    print(f"Lese Transkript von: {ep_url}")

    # Episodenseite laden
    ep_res = requests.get(ep_url)
    ep_soup = BeautifulSoup(ep_res.text, 'html.parser')
    
    # Titel finden
    title = ep_soup.find('h1').get_text(strip=True) if ep_soup.find('h1') else "Unbekannter Titel"
    
    # Transkript-Container finden
    transcript_parts = ep_soup.select('div#transcript p, div.transcript-row p')
    if not transcript_parts:
        transcript_parts = ep_soup.find_all('p')

    full_text = "\n\n".join([p.get_text(strip=True) for p in transcript_parts])

    # Dateien speichern
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    # Archiv-Datei
    with open(f"Transcript_{date_str}.txt", "w", encoding="utf-8") as f:
        f.write(f"Titel: {title}\nQuelle: {ep_url}\n\n{full_text}")
    
    # Datei für Gemini (latest.txt)
    with open("latest.txt", "w", encoding="utf-8") as f:
        f.write(f"Titel: {title}\nQuelle: {ep_url}\n\n{full_text}")
    
    print(f"Erfolg! 'latest.txt' wurde aktualisiert.")

if __name__ == "__main__":
    scrape_latest()
