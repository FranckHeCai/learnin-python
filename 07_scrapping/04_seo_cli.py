from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin
import requests

parser = argparse.ArgumentParser(description="Web scraping tool to check SEO on a given URL")
parser.add_argument("url", type=str, help="The URL of the webpage to scrape")
args = parser.parse_args()
url = args.url

headers = {
  "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36"
}

response = requests.get(url)
if response.status_code == 200:
  print("Success!")
  soup = BeautifulSoup(response.text, 'html.parser')

  print("Checking SEO for:", url)

  title_tag = soup.title.string
  if title_tag:
    print("Title:", title_tag)
    if 100 > len(title_tag) > 50:
      print("  - Title length is optimal.")
    else:
      print("  - Title length is not optimal (should be between 70 and 100 characters).")

  titles = [titulo.text for titulo in soup.find_all('h1')]
  if titles:
    for title in titles:
      print("H1 Title:", title)
  else:
    print("No H1 titles found")