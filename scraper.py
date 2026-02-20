import datetime
import re
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

BASE_URL = "https://podscripts.co/podcasts/tbpn-live/"
DOMAIN = "https://podscripts.co"

# 1. Der Python-Staubsauger: Hier wird die Funktion definiert!
def clean_transcript(raw_text):
    print("Starte Text-Reinigung (Staubsauger-Modus)...")
    
    # Timestamps entfernen (z.B. "Starting point is 00:00:16" oder "(01:31:33)")
    cleaned = re.sub(r'Starting point is \d{2}:\d{2}:\d{2}', '', raw_text)
    cleaned = re.sub(r'\(\d{2}:\d{2}:\d{2}\)', '', cleaned) 
    
    # Sinnlose Zeilenumbrüche reparieren
    cleaned = re.sub(r'(?<!\n)\n(?!\n)', ' ', cleaned)
    
    # Typische Fehler korrigieren
    replacements = {
        "TVPN": "TBPN",
        "Grogopedia": "Grokopedia",
        "Quen-3": "Qwen-3"
    }
    for wrong, right in replacements.items():
        cleaned = cleaned.replace(wrong, right)
        
    # Überflüssige Leerzeichen bereinigen
    cleaned = re.sub(r' +', ' ', cleaned).strip()
    return cleaned

# 2. Der Haupt-Scraper
def scrape_latest():
    print("Starte unsichtbaren Browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.wait_for_load_state('networkidle')
        
        soup = BeautifulSoup(page.content(), 'html.parser')
        all_links = soup.find_all('a', href=True)
        
        # Alle potenziellen Links sammeln
        episode_links = []
        for link in all_links:
            href = link.get('href', '')
            if href.startswith("/podcasts/tbpn-live/") and len(href) > len("/podcasts/tbpn-live/") and "page=" not in href:
                if "diet" not in href.lower():
                    episode_links.append(href)
        
        final_text = None
        final_title = None
        final_url = None

        # Links nacheinander prüfen, bis eine lange Folge gefunden wird
        for link in episode_links:
            ep_url = DOMAIN + link if link.startswith('/') else link
            print(f"Prüfe Folge: {ep_url}")
            
            page.goto(ep_url)
            page.wait_for_load_state('networkidle')
            
            # Klicke auf alle "Read More" Buttons, um den ganzen Text zu laden
            try:
                buttons = page.locator('button')
                for i in range(buttons.count()):
                    text = buttons.nth(i).inner_text().lower()
                    if "read more" in text or "load" in text or "show" in text:
                        buttons.nth(i).click(timeout=3000)
                        page.wait_for_timeout(2000)
            except Exception:
                pass 

            ep_html = page.content()
            ep_soup = BeautifulSoup(ep_html, 'html.parser')
            
            # Navigationselemente entfernen, damit nur das Transkript bleibt
            for element in ep_soup(["nav", "footer", "header", "script", "style"]):
                element.decompose()
                
            raw_text = ep_soup.get_text(separator='\n\n', strip=True)
            
            # Hier rufen wir die Reinigungsfunktion von oben auf
            clean_text = clean_transcript(raw_text)
            
            # DIE MAGISCHE GRENZE: Wir wollen nur Episoden mit > 50.000 Zeichen (Voll-Episoden)
            if len(clean_text) > 50000:
                print(f"BINGO! Lange Voll-Episode gefunden ({len(clean_text)} Zeichen).")
                final_text = clean_text
                final_title = ep_soup.find('h1').get_text(strip=True) if ep_soup.find('h1') else "Unbekannter Titel"
                final_url = ep_url
                break # Wir haben, was wir wollen, und stoppen die Schleife!
            else:
                print(f"Zu kurz ({len(clean_text)} Zeichen). Das ist wohl eine Bonusfolge. Suche weiter...")

        browser.close()

    # 3. Datei speichern (nur wenn wir eine lange Folge gefunden haben)
    if final_text:
        date_str = datetime.date.today().strftime("%Y-%m-%d")
        for fname in [f"Transcript_{date_str}.txt", "latest.txt"]:
            with open(fname, "w", encoding="utf-8") as f:
                f.write(f"Titel: {final_title}\nQuelle: {final_url}\n\n{final_text}")
        print(f"Erfolg! Die Datei latest.txt wurde aktualisiert.")
    else:
        print("Fehler: Keine ausreichend lange Episode auf der ersten Seite gefunden.")

if __name__ == "__main__":
    scrape_latest()
