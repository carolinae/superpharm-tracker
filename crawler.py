from bs4 import BeautifulSoup
import requests, json

products = []
f = open('products.txt', "r")
products = json.load(f)
f.close()

for product in products:
    product_html = requests.get(product["url"]).text
    source = BeautifulSoup(product_html, "html.parser")
    current_price = source.find_all("div", {"class": "shekels money-sign"})
    current_picture = source.find_all("img", {"class": "cloudzoom"})
    product.update({'current_price': current_price[0].text})
    product.update({'current_picture': current_picture[0].get('src')})

f = open('products.txt', "w")
json.dump(products, f)
f.close()









#superpharm_html = requests.get("https://shop.super-pharm.co.il/care/hair-care/shampoo-conditioner/shampoo/פינוק-שמפו-רגיל-700/p/215410").text

#source = BeautifulSoup(superpharm_html, "html.parser")
#prices = source.find_all("div", {"class": "shekels money-sign"})
#for price in prices:
 #   print(float(price.text))


