from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

url = "https://es.wikipedia.org/wiki/Web_scraping"

headers = {
  "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36"
}

url = "https://www.apple.com/es/shop/buy-mac/macbook-air"

def scrape_url(url):
  response = requests.get(url)
  if response.status_code == 200:
    print("Success!")
    soup = BeautifulSoup(response.text, 'html.parser')

    #Extraer todos los titulos <h1>
    # links = [link.string for link in soup.find_all('h1')]
    # print("Links:", links)
    #Extraer todos los enlaces
    links = [link.get('href') for link in soup.find_all('a')]
    relative_links = [urljoin('https://www.apple.com/', link) for link in links if link and not link.startswith('https://')]
    # for link in links:
    #   if link and not link.startswith('https://') :
    #     relative_links.append(urljoin('https://www.apple.com/', link))
    print("Relative links:", relative_links)
  else:
    print("Error:", response.status_code)

scrape_url(url)

