import os
os.system('pip install beautifulsoup4 requests --break-system-packages')

from bs4 import BeautifulSoup
import requests


response = requests.get("https://books.toscrape.com/")
# 1- نطلب الصفحة من الموقع

soup = BeautifulSoup(response.text,"html.parser")
# 2- نقرأ محتوى الصفحة
Prices = soup.find_all("p", class_="price_color")
# 3- نجيب كل البلوكات اللي فيها عناوين

for price_color in Prices:
    print("Price:", price_color.get_text(strip=True))
    # 4- نمر عليهم واحد واحد ونطبع التفاصيل