import os
os.system('pip install beautifulsoup4 requests --break-system-packages')

from bs4 import BeautifulSoup
import requests


response = requests.get("https://books.toscrape.com/")


soup = BeautifulSoup(response.text,"html.parser")

Prices = soup.find_all("p", class_="price_color")


for price_color in Prices:
    print("Price:", price_color.get_text(strip=True))
   