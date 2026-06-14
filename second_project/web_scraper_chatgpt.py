"""
Web Scraper لموقع 'Books to Scrape'
------------------------------------
السكربت ده بيستخرج:
  - عنوان الكتاب
  - سعر الكتاب
  - تقييم الكتاب
من الصفحة الرئيسية لموقع https://books.toscrape.com/

المكتبات المستخدمة:
    requests        - علشان نجيب محتوى الصفحة من الإنترنت
    BeautifulSoup   - علشان نفكك (نحلل) الـ HTML ونطلع العناصر اللي عايزينها
"""

import requests
from bs4 import BeautifulSoup

# 1) عنوان الموقع اللي هنشتغل عليه
url = "https://books.toscrape.com/"

# 2) ابعت طلب GET علشان تجيب الصفحة
response = requests.get(url)

# لو حصل خطأ في تحميل الصفحة (مش 200) ارفع Exception
if response.status_code != 200:
    raise Exception(f"فشل تحميل الصفحة (الكود: {response.status_code})")

# 3) حلّل محتوى الصفحة بالـ BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 4) هات كل الكتب (كل كتاب موجود جوه <article class="product_pod">)
books = soup.find_all("article", class_="product_pod")

# 5) لف على كل كتاب واستخرج البيانات
for book in books:
    # العنوان موجود في attribute اسمه 'title' جوه <a>
    title = book.h3.a.get("title")

    # السعر موجود في <p class="price_color">
    price = book.find("p", class_="price_color").get_text(strip=True)

    # التقييم موجود كـ class جوه <p class="star-rating">
    rating_tag = book.find("p", class_="star-rating")
    rating = rating_tag["class"][1] if rating_tag else "مفيش تقييم"

    # اطبع البيانات بشكل منظم
    print(f"العنوان: {title} | السعر: {price} | التقييم: {rating}")
