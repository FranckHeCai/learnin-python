from playwright.sync_api import sync_playwright
from urllib.parse import urljoin

url = 'https://midu.dev'

with sync_playwright() as p:

  def get_absolute_url(relative_url: str) -> str:
    absolute_url = urljoin(url, relative_url) if relative_url else None
    return absolute_url

  browser = p.chromium.launch()
  page = browser.new_page()
  page.goto(url)

  first_article_anchor = page.locator('article a').first
  first_article_anchor_href = first_article_anchor.get_attribute('href')
  print(f"First link href: {first_article_anchor_href}")
  print(f"First absolute link href: {get_absolute_url(first_article_anchor_href)}")
  

  first_image = first_article_anchor.locator('img').first
  image_src = first_image.get_attribute('src')
  print(f"First image src: {get_absolute_url(image_src)}")

  css_animation_anchor = page.locator("article a").nth(1)
  href = css_animation_anchor.get_attribute("href")
  print(f"CSS Animation link href: {get_absolute_url(href)}")
  #first_article_anchor.click()

  browser.close()
  
