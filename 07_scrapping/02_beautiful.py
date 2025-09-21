from bs4 import BeautifulSoup
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-air"

response = requests.get(url)

if response.status_code == 200:
  print("Success!")
  soup = BeautifulSoup(response.text, 'html.parser')
  #print(soup.prettify())

  title_tag = soup.find('title')

  if title_tag:
    print("Title:", title_tag.text)

  price_span = soup.find('span', class_ = "rc-prices-fullprice")
  print("Price:", price_span.text if price_span else "Price not found")

  # price_spans = soup.find_all('span', class_ = "rc-prices-fullprice")
  # if price_spans:
  #   for price in price_spans:
  #     print("Price found:", price.text)
  
  #Find product names and prices
  products = soup.find_all(class_ = 'rc-productselection-item')
  for product in products:
    name = product.find(class_ = 'list-title').text
    price = product.find(class_ = 'rc-prices-fullprice').text
    print(f"Product Name: {name} - Price: {price}")

else:
  print("Error:", response.status_code)
