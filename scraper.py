import datetime
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

BASE_URL = "https://podscripts.co/podcasts/tbpn-live/"
DOMAIN = "https://podscripts.co"

def scrape_latest():
    print("Starte unsichtbaren Browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 1. Hauptseite laden
        page.goto(BASE_URL)
        page.wait_for_load_state('networkidle') # Wartet, bis die Seite komplett geladen ist
        
        soup = BeautifulSoup(page.content(), 'html.parser')
        
        all_links = soup.find_all('a', href=True)
        all_links = soup.find_all('a', href=True)
        
        # Wir sammeln ALLE potenziellen Folgen-Links, nicht nur den ersten
        episode_links = []
        for link in all_links:
            href = link.get('href', '')
            if href.startswith("/podcasts/tbpn-live/") and len(href) > len("/podcasts/tbpn-live/") and "page=" not in href:
                if "diet" not in href.lower():
                    episode_links.append(href)
        
        # Jetzt testen wir die Links nacheinander, bis wir einen LANGEN finden
        for link in episode_links:
            ep_url = DOMAIN + link if link.startswith('/') else link
            print(f"Prüfe Folge: {ep_url}")
            
            page.goto(ep_url)
            page.wait_for_load_state('networkidle')
            
            # (Hier kommt dein Klick-Code für "Read More" rein)
            
            ep_html = page.content()
            ep_soup = BeautifulSoup(ep_html, 'html.parser')
            raw_text = ep_soup.get_text(separator='\n\n', strip=True)
            clean_text = clean_transcript(raw_text)
            
            # DIE NEUE MAGISCHE REGEL: Nur > 50.000 Zeichen werden akzeptiert!
            if len(clean_text) > 50000:
                print(f"BINGO! Lange Voll-Episode gefunden ({len(clean_text)} Zeichen).")
                title = ep_soup.find('h1').get_text(strip=True) if ep_soup.find('h1') else "Unbekannter Titel"
                break # Wir stoppen die Schleife, wir haben unseren Text!
            else:
                print(f"Zu kurz ({len(clean_text)} Zeichen). Ist wohl eine Bonusfolge. Suche weiter...")
                continue # Geht zum nächsten Link in der Liste
                
        browser.close()

    # 4. Text sauber extrahieren
    ep_soup = BeautifulSoup(ep_html, 'html.parser')
    title = ep_soup.find('h1').get_text(strip=True) if ep_soup.find('h1') else "Unbekannter Titel"
    
    # Wir löschen die Navigation und den Footer raus, damit wir nur das Transkript behalten
    for element in ep_soup(["nav", "footer", "header", "script", "style"]):
        element.decompose()
        
    full_text = ep_soup.get_text(separator='\n\n', strip=True)

    # 5. Speichern
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    for fname in [f"Transcript_{date_str}.txt", "latest.txt"]:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(f"Titel: {title}\nQuelle: {ep_url}\n\n{full_text}")
    
    print(f"Erfolg! Textlänge: {len(full_text)} Zeichen.")

if __name__ == "__main__":
    scrape_latest()
