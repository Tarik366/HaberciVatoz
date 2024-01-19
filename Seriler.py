from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

from Functions import getSeriePicture 

def getSeriesR(site):
    url = f"{site}/manga/list-mode/"
    ure = requests.get(url, headers=headers)
    uso = BeautifulSoup(ure.content.decode("utf-8"), 'html.parser')
    serieList = {}
    series = uso.select(".soralist .series")
    for serie in series:
        serieList[f"{serie.contents[0]}"] = serie["href"], serie.contents[0], getSeriePicture(serie["href"])
    return serieList

import json

def ggfd():
    print(getSeriesR("https://athenamanga.com/"))
    with open("./serie-test.json", "w", encoding="utf-8") as file:
        file.write(f"[{str(json.dumps(getSeriesR('https://athenamanga.com/'), ensure_ascii=False, indent=4))}]")
