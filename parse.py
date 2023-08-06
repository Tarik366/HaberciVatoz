import feedparser
import requests
from bs4 import BeautifulSoup
import lxml

NM = feedparser.parse("https://athenafansub.com/feed/")
mentry = NM.entries[0]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
sou = requests.get("https://athenafansub.com/", headers=headers)
soup = BeautifulSoup(sou.content, 'html.parser')
im = ["a"]
for s in soup.find_all("div", class_="utao"):
    for item in s.find_all('img', class_="wp-post-image"):
        i = item['src']
        im = im + i.split("\n")

class n:
    title = mentry.title
    link = mentry.link
    cat = mentry.category
    img = im[1]

print(f"{n.title}, {n.link}, {n.img}")