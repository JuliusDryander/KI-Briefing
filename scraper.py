import requests
from bs4 import BeautifulSoup
import datetime

BASE_URL = "https://podscripts.co/podcasts/tbpn-live/"
DOMAIN = "https://podscripts.co"

def scrape_latest():
    print("Suche nach der neuesten Voll-Episode (>2h)...")
    
    # Header hinzufügen, damit die Website uns nicht für einen einfachen Bot hält
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    
    response = requests.get(BASE_URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_links = soup.find_all('a', href=True)
    first_full_episode_link = None
    
    for link in all_links:
        href = link['href']
        if href.startswith("/podcasts/tbpn-live/") and len(href) > len("/podcasts/tbpn-live/") and "page=" not in href:
            if "diet" not in href.lower():
                first_full_episode_link = href
                break 
    
    if not first_full_episode_link:
        print("Keine volle Episode gefunden.")
        return

    ep_url = DOMAIN + first_full_episode_link if first_full_episode_link.startswith('/') else first_full_episode_link
    print(f"Lese Transkript von: {ep_url}")

    ep_res = requests.get(ep_url, headers=headers)
    ep_soup = BeautifulSoup(ep_res.text, 'html.parser')
    
    title = ep_soup.find('h1').get_text(strip=True) if ep_soup.find('h1') else "Unbekannter Titel"
    
    # NEU: Aggressive Text-Extraktion
    full_text = ""
    
    # 1. Versuch: Typische Container für Transkripte
    transcript_container = ep_soup.find('div', id='transcript') or \
                           ep_soup.find('div', class_='transcript') or \
                           ep_soup.find('article') or \
                           ep_soup.find('main')
    
    if transcript_container:
        # Zieht jeden Text heraus, egal ob p, span oder div, und setzt Absätze
        full_text = transcript_container.get_text(separator='\n\n', strip=True)
    else:
        # 2. Versuch: Finde alle potenziellen Transkript-Zeilen (falls kein Hauptcontainer existiert)
        rows = ep_soup.find_all(['div', 'p'], class_=lambda x: x and 'transcript' in x.lower())
        if rows:
            full_text = "\n\n".join([row.get_text(separator=' ', strip=True) for row in rows])
        else:
            # 3. Notfall-Fallback: Den gesamten Text der Seite nehmen (Body)
            if ep_soup.body:
                full_text = ep_soup.body.get_text(separator='\n\n', strip=True)
            else:
                full_text = "Fehler: Konnte den Text auf der Seite nicht extrahieren."

    date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    for fname in [f"Transcript_{date_str}.txt", "latest.txt"]:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(f"Titel: {title}\nQuelle: {ep_url}\n\n{full_text}")
    
    print(f"Erfolg! Textlänge: {len(full_text)} Zeichen.")

if __name__ == "__main__":
    scrape_latest()
