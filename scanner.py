
import requests
from bs4 import BeautifulSoup


urls_to_scan = ["https://www.reuters.com/technology/", "https://techcrunch.com/"]

def fetch_news():
    for url in urls_to_scan:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        titles = [a.text for a in soup.find_all("span", class_="titleline")][:15]

        found_news = "\n".join(f"- {title}" for title in titles)
    
    return found_news