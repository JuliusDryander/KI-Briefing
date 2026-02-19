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
        first_full_episode_link = None
        
        for link in all_links:
            href = link.get('href', '')
            if href.startswith("/podcasts/tbpn-live/") and len(href) > len("/podcasts/tbpn-live/") and "page=" not in href:
                if "diet" not in href.lower():
                    first_full_episode_link = href
                    break 
        
        if not first_full_episode_link:
            print("Keine volle Episode gefunden.")
            browser.close()
            return

        ep_url = DOMAIN + first_full_episode_link if first_full_episode_link.startswith('/') else first_full_episode_link
        print(f"Lese echtes Transkript von: {ep_url}")

        # 2. Episoden-Seite laden
        page.goto(ep_url)
        page.wait_for_load_state('networkidle')
        
        # 3. Klicke auf "Read More" falls vorhanden, um den Text zu entpacken
        try:
            buttons = page.locator('button')
            for i in range(buttons.count()):
                text = buttons.nth(i).inner_text().lower()
                if "read more" in text or "load" in text or "show" in text:
                    buttons.nth(i).click(timeout=3000)
                    page.wait_for_timeout(2000) # Kurz warten, bis der Text aufploppt
        except Exception:
            pass # Wenn kein Button da ist, machen wir einfach weiter

        # Jetzt nehmen wir den finalen, fertig gerenderten HTML-Code
        ep_html = page.content()
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
