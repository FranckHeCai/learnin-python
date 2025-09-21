import requests
import re
url = "https://www.apple.com/es/shop/buy-mac/macbook-air"

response = requests.get(url)

if response.status_code == 200:
  print("Success!")
  html = response.text
  #print(html)

  price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'
  match = re.search(price_pattern, html)
  match = re.search
  
  if match:
    print("Price found:", match.group(1))
else:
  print("Error:", response.status_code)
