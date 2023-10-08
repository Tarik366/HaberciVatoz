import requests
from bs4 import BeautifulSoup

def getSeriePicture(link, anime=False):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

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
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    sou = requests.get(link, headers=headers)
    soup = BeautifulSoup(sou.content, 'html.parser')

    roleid = soup.find("span", attrs={"id": "roleid"})
    roleid = roleid.get_text()
    roleid = roleid.split(", ")
    r = []
    try:
        for role in roleid:
            r.append(int(role))
    except ValueError:
        r = ["boş"]
    return r

def redacteSerieName(cat):
    catt = cat.replace(" ", "-")
    catt = catt.replace("ğ", "g")
    catt = catt.replace("ı", "i")
    catt = catt.replace("ş", "s")
    catt = catt.replace("ö", "o")
    catt = catt.replace("ü", "u")
    catt = catt.replace("ç", "c")
    catt = catt.replace(",", "")
    catt = catt.replace('"', "")
    catt = catt.replace("%", "")
    catt = catt.replace("#", "")
    catt = catt.replace("@", "")
    catt = catt.replace("!", "")
    catt = catt.replace("&", "")
    catt = catt.replace("/", "")
    catt = catt.replace("(", "")
    catt = catt.replace(")", "")
    catt = catt.replace("[", "")
    catt = catt.replace("]", "")
    catt = catt.replace("{", "")
    catt = catt.replace("}", "")
    catt = catt.replace("═", "")
    catt = catt.replace("=", "")
    catt = catt.replace("↟", "")
    catt = catt.replace("~", "")
    catt = catt.replace("?", "")
    catt = catt.replace("|", "")
    catt = catt.replace("’", "")
    catt = catt.replace("\\", "")
    catt = catt.replace("'", "").lower()
    return catt

