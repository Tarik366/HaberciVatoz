from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def getSeries(url):
    ure = requests.get(url, headers=headers)
    uso = BeautifulSoup(ure.content.decode("utf-8"), 'html.parser')
    serieList = []
    series = uso.select(".soralist .series")
    for serie in series:
        serieList.append(serie["href"])
    return serieList

def getTheSerie(site):
    ure = requests.get(site, headers=headers)
    uso = BeautifulSoup(ure.content, 'html.parser')
        
    def getSerieDescription(anime=False):

        if anime == True:
            desc = uso.select("#animeDescription")[0].get_text()
            return desc
        else:
            desc = uso.select(".entry-content")[0].get_text()
            return desc
        
    def getSerieName(anime=False):

        if anime is True:
            manga_link = uso.find(id='anime_title').get_text()
        else:
            manga_link = uso.select('.entry-title')[0].get_text()

        return manga_link

    def getSeriePicture(link, anime=False):

        if anime == False:
            for s in uso.find_all("div", class_='thumb'):
                for item in s.find_all('img', class_='wp-post-image'):
                    i = item['src']
                    im = i.split("\n")
                    hgf = f"{im[0]}".replace("i3.wp.com/", "")
                if hgf.startswith("https://") is False:
                    hgf = f"https://athenafansub.com{hgf}"
                return hgf
        if anime == True:
            for s in uso.find_all("div", class_='cover'):
                for item in s.find_all('img', class_='wp-post-image'):
                    i = item['src']
                    im = i.split("\n")
                    hgf = f"{im[0]}".replace("i3.wp.com/", "")
                if hgf.startswith("https://") is False:
                    hgf = f"https://anime.athenafansub.com{hgf}"
                return hgf
    
    serieList = {
        'name': getSerieName(site), 
        'url': site, 
        'cover': getSeriePicture(site), 
        'desc': getSerieDescription(site)
    }
    return serieList

import random 

def getRandomSerie(site):
    series = getSeries(site)
    serie = random.choice(series)
    ser = getTheSerie(serie)
    return ser