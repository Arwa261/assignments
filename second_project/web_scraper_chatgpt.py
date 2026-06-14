
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"فشل تحميل الصفحة (الكود: {response.status_code})")

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")


for book in books:
   
    title = book.h3.a.get("title")

    
    price = book.find("p", class_="price_color").get_text(strip=True)

   
    rating_tag = book.find("p", class_="star-rating")
    rating = rating_tag["class"][1] if rating_tag else "مفيش تقييم"

   
    print(f"العنوان: {title} | السعر: {price} | التقييم: {rating}")
