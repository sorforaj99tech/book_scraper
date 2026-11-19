import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')\

books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
content = str(books)

re_book_title = r'<a href=".*?" title="(.*?)"'

re_prices = r'<p class="price_color">(.*?)</p>'

re_availability = r'<p class="instoke availability">(.*?)</p>'

titles = re.findall(re_book_title, content)
prices = re.findall(re_prices, content)
availability = re.findall(re_availability, content)

for i in zip(titles, prices,availability):
    print(i)