from flask import jsonify
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

print(datetime.now())

relaeseList = ["Kuzey", "Güney", "Doğu", "Batı"]

exceptList = {
 "Filistin": {
  'link': "https://tr.wikipedia.org/wiki/Filistin_Devleti"
 },
 "Birleşik Krallık": {
  'demonim': "İngiliz"
 },
 "Birleşik Arap Emirlikleri": {
  'demonim': 'Arap'
 }
}

headers = {
 'User-Agent':
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# For Turkish vowel changes
import TurkishStemmer

def getBayrak(soup):
 bayrak = f"""https:{str(soup.select('img[alt$="ayrağı"], img[alt$="bayrak"], img[alt$="Bayrak"]')[0]['srcset']).split(', ')[1].replace('250px', '1000px')[:-3]}"""
 return bayrak

#FIXME - Fix this shit
def doExcept(exceptThing, exceptLink = None, exceptList=exceptList):
 list = exceptList[exceptThing]
 try:
  link = list['link']
 except:
  link = exceptLink
 lire = requests.get(link, headers=headers)
 liso = bs(lire.content, 'html.parser')
 try:
  bayrak = list['bayrak']
 except:
  bayrak = getBayrak(liso)
 try:
  denonim = list['demonim']
 except:
  try:
   denonim = liso.select('table.geography tr:has( th a[href$="wiki/Demonim"] ) .infobox-data a')[0].contents[0]
  except:
   denonim = getDemonim(exceptThing)
 return {"link": link, 'demonim': denonim, "flag": bayrak}

def getDemonim(name): #NOTE - In this function, pass means 合格
 splittedName = name.split(' ')
 demonimName = splittedName[0]
 if demonimName in relaeseList:
  demonimName = splittedName[1]
 denonim = f"{demonimName}lı"
 if TurkishStemmer.HasVowelHarmony(denonim):
  pass
 else:
  denonim = f"{demonimName}li"
  if TurkishStemmer.HasVowelHarmony(denonim):
   pass
  else:
   denonim = f"{demonimName}lu"
 return denonim

def getFlags(url):
 ure = requests.get(url, headers=headers)
 uso = bs(ure.content, 'html.parser')
 UnexpectedName = uso.select('.toccolours i b>a')
 countryList = {}
    
 #SECTION - 不認識 - This loop for unrecognized countries
 for item in UnexpectedName:
  link = f"https://tr.wikipedia.org/{item['href']}"
  if item['title'] in exceptList:
   exceptCountryDict = doExcept(item['title'], link, exceptList)
   countryList[item['title']] = exceptCountryDict
  else:
   lire = requests.get(link, headers=headers)
   liso = bs(lire.content, 'html.parser')
   bayrak = getBayrak(liso)
   try:
    denonim = liso.select('table.geography tr:has( th a[href$="wiki/Demonim"] ) .infobox-data a')[0].contents[0]
   except:
    denonim = getDemonim(item['title'])
   countryList[item['title']] = {"link": link, 'demonim': denonim, "flag": bayrak}
 #!SECTION
  
 name = uso.select(".toccolours>tbody>tr>td>a:not([href$='ayra%C4%9F%C4%B1'])")
 #SECTION - 普通 - This loop for recognized countries 
 for item in name:
  link = f"https://tr.wikipedia.org/{item['href']}"
  title = item['title']
  print(title)
  if item['title'] in exceptList:
   exceptCountryDict = doExcept(item['title'], link, exceptList)
   countryList[item['title']] = exceptCountryDict
  else:
   lire = requests.get(link, headers=headers)
   liso = bs(lire.content, 'html.parser')
   bayrak = getBayrak(liso)
   try:
    denonim = liso.select('table.geography tr:has( th a[href$="wiki/Demonim"] ) .infobox-data')[0].contents[0].contents[0] # type: ignore
   except:
    denonim = getDemonim(title)
   countryList[title] = {"link": f"{link}", "demonim": f"{denonim}", "flag": f"{bayrak}"}
 return countryList
 #!SECTION

import json

with open('countries.json', 'w', encoding='utf-8') as file:
 countries = getFlags('https://tr.wikipedia.org/wiki/%C3%9Clke_bayraklar%C4%B1_listesi')
 print(countries)
 file.write(json.dumps(countries, ensure_ascii=False, indent=4))
print(datetime.now())
