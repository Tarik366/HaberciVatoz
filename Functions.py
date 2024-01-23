import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def getSerieLink(link, anime=False):

    sou = requests.get(link, headers=headers)
    soup = BeautifulSoup(sou.content, 'html.parser')

    if anime is True:
        manga_link = soup.find(id='anime_title')
    else:
        manga_link = soup.select('.allc a')[0]

    return manga_link['href']

def getSerieName(link, anime=False):

    ure = requests.get(link, headers=headers)
    uso = BeautifulSoup(ure.content, 'html.parser')

    if anime is True:
        manga_link = uso.find(id='anime_title').get_text()
    else:
        manga_link = uso.select('.entry-title')[0].get_text()

    return manga_link

def getSeriePicture(link, anime=False):

    sou = requests.get(link, headers=headers)
    soup = BeautifulSoup(sou.content, 'html.parser')

    if anime == False:
        for s in soup.find_all("div", class_='thumb'):
            for item in s.find_all('img', class_='wp-post-image'):
                i = item['src']
                im = i.split("\n")
                hgf = f"{im[0]}".replace("i3.wp.com/", "")
            if hgf.startswith("https://") is False:
                hgf = f"https://athenafansub.com{hgf}"
            return hgf
    if anime == True:
        for s in soup.find_all("div", class_='cover'):
            for item in s.find_all('img', class_='wp-post-image'):
                i = item['src']
                im = i.split("\n")
                hgf = f"{im[0]}".replace("i3.wp.com/", "")
            if hgf.startswith("https://") is False:
                hgf = f"https://anime.athenafansub.com{hgf}"
            return hgf

def getSerieId(link):

    sou = requests.get(link, headers=headers)
    soup = BeautifulSoup(sou.content, 'html.parser')
    r = []
    try:
        roleid = soup.find("span", attrs={"id": "roleid"})
        roleid = roleid.get_text()
        roleid = roleid.split(", ")
        for role in roleid:
            r.append(int(role))
    except:
        r = ["boş"]
    return r

def getSerieDescription(site, anime=False):

    sou = requests.get(site, headers=headers)
    soup = BeautifulSoup(sou.content, 'html.parser')

    if anime == True:
        desc = soup.select("#animeDescription")[0].get_text()
        return desc
    else:
        desc = soup.select(".entry-content")[0].get_text()
        return desc