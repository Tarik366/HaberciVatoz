import os.path
import os
import random
import discord
from discord import *
from discord.ext import commands, tasks
from discord.ui import Button
from Vars import *
from Sözler.Hitler import *
from Sözler.Atatürk import *
from Sözler.Lenin import *
from Sözler.Stalin import *
from Sözler.Cengiz import *
from Sözler.CelalŞengör import *
from Sözler.MeteHan import *
from propaganda import *
from hoi4tips import *
from bs4 import BeautifulSoup
import requests
import json
from dotenv.main import load_dotenv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from Seriler import *
import datetime as dt
import feedparser
from keep_alive import keep_alive

a = 813886736051863554
intents = Intents.all()
Bot = commands.Bot("!", help_command=None, intents=intents)
tür = "vatoz"
load_dotenv()
sites = ["https://athenafansub.com/", "https://anime.athenafansub.com/"]


@Bot.event
async def on_ready():
    for site in sites:
        NF = feedparser.parse(f"{site}feed/")
    fentry = NF.entries[0]
    msg1.start()
    msg2.start()
    keep_alive()

@tasks.loop(minutes=3)
async def msg1():
        NF = feedparser.parse("https://athenafansub.com/feed/")
        entry = NF.entries[0]

        le = open("lastEntry.txt", "r", encoding="utf-8")
        ar = le.read()

        class n:
            title = entry.title
            link = entry.link
            cat = entry.category
            catt = cat.replace(" ", "-")
            catt = catt.replace("'", "").lower()

        h = entry.link.replace("https://athenafansub.com/", "https://athenafansub.com/manga")
        sentry = entry.title

        if sentry not in str(ar):

            headers = {
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            }
            sou = requests.get(h, headers=headers)
            soup = BeautifulSoup(sou.content, 'html.parser')

            def ws():
                for s in soup.find_all("div", class_="thumb"):

                    for item in s.find_all('img', class_="wp-post-image"):
                        i = item['src']
                        im = i.split("\n")
                        hgf = im[0]
                        print(hgf)
                        return hgf

            nimg = ws()
            emed = Embed(title=f"{entry.title} yayında keyifli okumalar!",
                         description=f"okumak için {entry.link}",
                         url=entry.link)
            emed = emed.set_image(url=nimg)

            channel = Bot.get_channel(a)
            role = get(channel.guild.roles, name=n.cat)

            print(str(ar))

            with open("lastEntry.txt", "w", encoding="utf-8") as wle:
                wle.write(sentry)

            await channel.send(embed=emed)
            await channel.send(role)

@tasks.loop(minutes=3)
async def msg2():
        NF = feedparser.parse("https://anime.athenafansub.com/feed/")
        entry = NF.entries[0]

        le = open("lastAnimeEntry.txt", "r", encoding="utf-8")
        ar = le.read()

        class n:
            title = entry.title
            link = entry.link
            cat = entry.category
            catt = title.rsplit(' ', 1)[0]
            
        h = entry.link.replace("https://anime.athenafansub.com/", "https://anime.athenafansub.com/anime")
        sentry = entry.title

        if sentry not in str(ar):

            headers = {
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            }
            sou = requests.get(h, headers=headers)
            soup = BeautifulSoup(sou.content, 'html.parser')

            def ws():
                for s in soup.find_all("div", class_="latest"):

                    for item in s.find_all('img', class_="kapak"):
                        i = item['src']
                        im = i.split("\n")
                        hgf = im[0]
                        print(hgf)
                        return hgf

            nimg = ws()
            emed = Embed(title=f"{entry.title} yayında keyifli okumalar!",
                         description=f"okumak için {entry.link}",
                         url=entry.link)
            emed = emed.set_image(url=nimg)

            channel = Bot.get_channel(a)
            role = get(channel.guild.roles, name=n.catt)

            print(str(ar))

            with open("lastAnimeEntry.txt", "w", encoding="utf-8") as wle:
                wle.write(sentry)

            await channel.send(embed=emed)

# Help komutu


@Bot.command()
async def yardım(ctx):
    embed = Embed(title="Yardım",
                  description="Yardım komutları",
                  color=0x8a0a01)
    embed.add_field(name="!yardım",
                    value="yardım komutlarını gösterir",
                    inline=False)
    embed.add_field(name="!yak <@Banlanacak kişi>",
                    value="Etiketlenen kişiyi yakar(banlar)",
                    inline=False)
    embed.add_field(name="!kick <@kicklenecek kişi>",
                    value="Etiketlenen kişiyi kickler",
                    inline=False)
    embed.add_field(
        name="!i <resim ismi>",
        value=
        "110'dan fazla gif veya resimden seçileni atar. Resim listesi için !i help yazabilirsiniz",
        inline=False)
    embed.add_field(name="!başvuru <4 formdan birisi>",
                    value="Seçilen başvuru formunu gönderir",
                    inline=False)
    embed.add_field(name="!ada <Adanacak şey>",
                    value="İstediğiniz bir şeyi hayalet vatoza adar",
                    inline=False)
    embed.add_field(name="!pp <@profil fotoğrafını istediğiniz>",
                    value="Yazan kişinin profil fotoğrafını atar",
                    inline=False)
    embed.add_field(name="!ideoloji <istediğiniz ideoloji veya ülke>",
                    value="130 ideoloji arasından seçilen ideolojiye geçerim",
                    inline=False)
    embed.add_field(name="!söz",
                    value="Rastgele bir kişinin sözünü atar",
                    inline=False)
    embed.add_field(name="!propaganda",
                    value="Random propaganda gönderir",
                    inline=False)
    embed.add_field(
        name="!r <kitap, film, şarkı, oyun, anime veya anime>",
        value=
        "Seçilen kitap, film, şarkı, oyun, anime veya manga seçeneklerden birisi için öneride bulunur gönderir",
        inline=False)
    embed.add_field(name="!fok", value="Foka dönüşürüm", inline=False)
    embed.add_field(name="!hoi4tip",
                    value="Hearts of iron 4 için ipucu veririm")
    await ctx.send(embed=embed)


# gifs


@Bot.command()
async def i(ctx, *args):
    if "like" in args:
        await ctx.send(like)
    if "rage" in args:
        await ctx.send(rage)
    if "anakuzusu" in args:
        await ctx.send(anakuzusu)
    if "cry" in args:
        await ctx.send(cry)
    if "freakout" in args:
        await ctx.send(freakout)
    if "haa" in args:
        await ctx.send(haa)
    if "o7konosuba" in args:
        await ctx.send(o7konosuba)
    if "nomnom" in args:
        await ctx.send(nomnom)
    if "like2x" in args:
        await ctx.send(like2x)
    if "shock" in args:
        await ctx.send(shock)
    if "o7" in args:
        await ctx.send(o7)
    if "foksax" in args:
        await ctx.send(foksax)
    if "dwayne" in args:
        await ctx.send(dwayne)
    if "hatsoff" in args:
        await ctx.send(hatsoff)
    if "capitalism" in args:
        await ctx.send(capitalism)
    if "soviet" in args:
        await ctx.send(soviet)
    if "dön" in args:
        await ctx.send(sikin)
    if "susamuru" in args:
        await ctx.send(susamuru)
    if "fire" in args:
        await ctx.send(fire)
    if "marcharmy" in args:
        await ctx.send(marcharmy)
    if "irumadance" in args:
        await ctx.send(irumadance)
    if "taam" in args:
        await ctx.send(taam)
    if "stare" in args:
        await ctx.send(stare)
    if "napim" in args:
        await ctx.send(napim)
    if "hatayapar" in args:
        await ctx.send(hatayapar)
    if "nazifokları" in args:
        await ctx.send(nazifokları)
    if "troll" in args:
        await ctx.send(troll)
    if "yahudiler" in args:
        await ctx.send(yahudiler)
    if "balanced" in args:
        await ctx.send(balanced)
    if "shipbang" in args:
        await ctx.send(shipbang)
    if "tank" in args:
        await ctx.send(tank)
    if "degil" in args:
        await ctx.send(degil)
    if "air" in args:
        await ctx.send(air)
    if "kimclap" in args:
        await ctx.send(kimclap)
    if "worry" in args:
        await ctx.send(worry)
    if "muso" in args:
        await ctx.send(muso)
    if "sob" in args:
        await ctx.send(sob)
    if "kannaeat" in args:
        await ctx.send(kannaeat)
    if "baka" in args:
        await ctx.send(baka)
    if "triggered" in args:
        await ctx.send(triggered)
    if "shinobu" in args:
        await ctx.send(shinobu)
    if "shy" in args:
        await ctx.send(shy)
    if "bang2" in args:
        await ctx.send(bang2)
    if "shutup" in args:
        await ctx.send(shutup)
    if "save" in args:
        await ctx.send(save)
    if "aah" in args:
        await ctx.send(aah)
    if "para" in args:
        await ctx.send(para)
    if "yay" in args:
        await ctx.send(yay)
    if "anlıyorum" in args:
        await ctx.send(anlıyorum)
    if "understood" in args:
        await ctx.send(understood)
    if "igetit" in args:
        await ctx.send(igetit)
    if "benzin" in args:
        await ctx.send(benzin)
    if "why" in args:
        await ctx.send(why)
    if "celebrate" in args:
        await ctx.send(celebrate)
    if "braintime" in args:
        await ctx.send(braintime)
    if "drink" in args:
        await ctx.send(drink)
    if "bb" in args:
        await ctx.send(bb)
    if "dot" in args:
        await ctx.send(dot)
    if "confused" in args:
        await ctx.send(confused)
    if "lenny" in args:
        await ctx.send(lenny)
    if "bang" in args:
        await ctx.send(bang)
    if "slap" in args:
        await ctx.send(slap)
    if "mad" in args:
        await ctx.send(mad)
    if "sob2" in args:
        await ctx.send(sob2)
    if "laugh" in args:
        await ctx.send(laugh)
    if "evilsmile" in args:
        await ctx.send(evilsmile)
    if "dissaper" in args:
        await ctx.send(dissaper)
    if "behind" in args:
        await ctx.send(behind)
    if "like3" in args:
        await ctx.send(like3)
    if "whatanime" in args:
        await ctx.send(whatanime)
    if "nomnomnom" in args:
        await ctx.send(nomnomnom)
    if "bonk" in args:
        await ctx.send(bonk)
    if "yarra" in args:
        await ctx.send(yarra)
    if "katon" in args:
        await ctx.send(katon)
    if "hug" in args:
        await ctx.send(hug)
    if "hug2" in args:
        await ctx.send(hug2)
    if "sob3" in args:
        await ctx.send(sob3)
    if "animechild" in args:
        await ctx.send(animechild)
    if "narutodance" in args:
        await ctx.send(narutodance)
    if "darkstare" in args:
        await ctx.send(darkstare)
    if "think" in args:
        await ctx.send(think)
    if "point" in args:
        await ctx.send(point)
    if "bagıs" in args:
        await ctx.send(bagıs)
    if "stalinpoint" in args:
        await ctx.send(stalinpoint)
    if "serve" in args:
        await ctx.send(serve)
    if "waku" in args:
        await ctx.send(waku)
    if "fail" in args:
        await ctx.send(fail)
    if "comunazi" in args:
        await ctx.send(comunazi)
    if "şaak" in args:
        await ctx.send(şaak)
    if "doom" in args:
        await ctx.send(doom)
    if "omori" in args:
        await ctx.send(omori)
    if "papas" in args:
        await ctx.send(papas)
    if "hans" in args:
        await ctx.send(hans)
    if "yummy" in args:
        await ctx.send(yummy)
    if "okay" in args:
        await ctx.send(okay)
    if "what" in args:
        await ctx.send(what)
    if "sad" in args:
        await ctx.send(sad)
    if "gel" in args:
        await ctx.send(gel)
    if "ekonomi" in args:
        await ctx.send(ekonomi)
    if "mikasa" in args:
        await ctx.send(mikasa)
    if "çıldır" in args:
        await ctx.send(çıldır)
    if "kırk" in args:
        await ctx.send(kırk)
    if "drink2" in args:
        await ctx.send(drink2)
    if "fbi" in args:
        await ctx.send(fbi)
    if "want" in args:
        await ctx.send(want)
    if "want2" in args:
        await ctx.send(want2)
    if "tehe" in args:
        await ctx.send(tehe)
    if "cringe" in args:
        await ctx.send(cringe)
    if "money" in args:
        await ctx.send(money)
    if "yay2" in args:
        await ctx.send(yay2)
    if "nod" in args:
        await ctx.send(nod)
    if "tobi" in args:
        await ctx.send(tobi)
    if "yesmaster" in args:
        await ctx.send(yesmaster)
    if "nope" in args:
        await ctx.send(nope)
    if "blyatiful" in args:
        await ctx.send(blyatiful)


# Bug fix
@Bot.command()
async def aki(ctx):
    print("")


@Bot.command()
async def rank(ctx):
    print("")


@Bot.command()
async def owo(ctx):
    print("")


# ekibe başvuru


@Bot.command()
async def başvuru(ctx, *args):
    if "mangaçevirmen" in args:
        tr = Embed(title="Manga çevirmen başvuru formu",
                   description=translater)
        await ctx.send(embed=tr)
    if "mangaeditör" in args:
        ed = Embed(title="Manga editör başvuru formu", description=editor)
        await ctx.send(embed=ed)
    if "webçevirmen" in args:
        wtr = Embed(title="Webtoon çevirmen başvuru formu",
                    description=webtranslater)
        await ctx.send(embed=wtr)
    if "webeditör" in args:
        wed = Embed(title="Webtoon editör başvuru formu",
                    description=webeditor)
    if "animeçeviri" in args:
        wed = Embed(title="Anime çevirmen başvuru formu",
                    description=animeceviri)
        await ctx.send(embed=wed)


# Adak sistemi


@Bot.command()
async def ada(ctx, *args):
    author = str(ctx.message.author)
    ad = "adaklar/" + author + ".txt"
    if "temizle" in args:
        os.remove(ad)
        embed = Embed(title="Adağınız başarıyla temizlendi.")
        await ctx.send(embed=embed)
    if os.path.exists(ad) == True and "temizle" not in args:
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.send(embed=msg)
        r = open(ad, "r")
        ar = r.read()
        ada = open(str(ad), "w")
        a = str(ar) + ", " + str(args)
        ada.write(a)
    if os.path.exists(ad) == False and "temizle" not in args:
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.send(embed=msg)
        ada = open(str(ad), "x")
        ada = open(str(ad), "w")
        a = str(args)
        ada.write(a)


@Bot.command()
async def pp(ctx, Member: Member):
    await ctx.send(Member.avatar)


@Bot.command()
async def spp(ctx):
    icon_url = ctx.guild.icon
    await ctx.send(f"{icon_url}")


@Bot.command()
async def fok(ctx):
    print("")


@Bot.command()
async def vatoz(ctx):
    print("")


"""
@Bot.command()
async def ideoloji(ctx, *args):
        if "ak4747" in args:
            dem = open("vatozlar/ak4747.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Etrafa sikmaca"))
            await Bot.user.edit(username="Bilge AK-4747 Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bir can karşılığında bir can. Bence mantıklı bir anlaşma")
            await ctx.send(embed=embed)
        if "almanya" in args:
            dem = open("vatozlar/almanya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşıyor"))
            await Bot.user.edit(username="Bilge Alman Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Alman oldum")
            await ctx.send(embed=embed)
        if "anarşist" in args:
            fas = open("vatozlar/anarşist.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Otoriteye küfür ediyor"))
            await Bot.user.edit(username="Bilge Anarşist Vatoz", avatar=fasc)
            vatoz = "anarşist"
            print(vatoz)
            embed = Embed(title="Otoritede ne?")
            await ctx.send(embed=embed)
        if "anarkoilkel" in args:
            ail = open("vatozlar/Anarko-ilkelcilik_vatoz.jpg", 'rb')
            ailk = ail.read()
            await Bot.change_presence(activity=Game(name="Hayvan avlıyor"))
            await Bot.user.edit(username="Bilge Anarko-ilkelci Vatoz", avatar=fasc)
            vatoz = "anarko ilkelci"
            print(vatoz)
            embed = Embed(title="Yeni dünya boş asıl olay geçmişte var")
            await ctx.send(embed=embed)
        if "anarkokapitalist" in args:
            fas = open("vatozlar/Anarko-kapitalist_vatoz.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Tüccarlık yapıyor"))
            await Bot.user.edit(username="Bilge Anarko Vatoz", avatar=fasc)
            vatoz = "anarko kapitalist"
            print(vatoz)
            embed = Embed(title="Serbest piyasasında tüccarlık yapacağım")
            await ctx.send(embed=embed)
        if "Avusturya" in args:
            dem = open("vatozlar/Avusturya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Avusturyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Avusturyalı oldum")
            await ctx.send(embed=embed)
        if "azerbeycan" in args:
            dem = open("vatozlar/azerbeycan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Azerbeycanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Türk oldum")
            await ctx.send(embed=embed)
        if "Belarus" in args:
            dem = open("vatozlar/Belarus.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Belaruslu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Belaruslu oldum")
            await ctx.send(embed=embed)
        if "Belçika" in args:
            dem = open("vatozlar/Belçika.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Belçikalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Belçikalı oldum")
            await ctx.send(embed=embed)
        if "BosnaHersek" in args:
            dem = open("vatozlar/bosna.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Bosnalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bosnalı oldum")
            await ctx.send(embed=embed)
        if "Bulgaristan" in args:
            dem = open("vatozlar/Bulgaristan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Bulgar Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bulgar oldum")
            await ctx.send(embed=embed)
        if "Çek" in args:
            dem = open("vatozlar/Çek.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Çekli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Çekli oldum")
            await ctx.send(embed=embed)
        if "demokrat" in args:
            dem = open("vatozlar/demokrat.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Oy saymaca"))
            await Bot.user.edit(username="Bilge Demokrat Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Herkes istiklalimde eşit özgür olacak")
            await ctx.send(embed=embed)
        if "Danimarka" in args:
            dem = open("vatozlar/denmark.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Danimarkalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Danimarkalı oldum")
            await ctx.send(embed=embed)
        if "ermenistan" in args:
            dem = open("vatozlar/ermenistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Eremeni Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Ermeni oldum")
            await ctx.send(embed=embed)
        if "Estonya" in args:
            dem = open("vatozlar/estonya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Estonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Estonyalı oldum")
            await ctx.send(embed=embed)
        if "fabrika" in args:
            fas = open("vatozlar/fabrika_vatoz.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Edit yapıyor"))
            await Bot.user.edit(username="Bilge Fabrika Vatoz", avatar=fasc)
            vatoz = "fabrika"
            print(vatoz)
            embed = Embed(title="İdeolojileri boş verdim ben edit yapacağım")
            await ctx.send(embed=embed)
        if "faşist" in args:
            fas = open("vatozlar/fasist_vatoz.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Yahudi yakmaca"))
            await Bot.user.edit(username="Bilge Faşist Vatoz", avatar=fasc)
            vatoz = "faşist"
            embed = Embed(title="Köklerime döndüm")
            await ctx.send(embed=embed)
        if "finlandiya" in args:
            dem = open("vatozlar/finland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Finlandiyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Finlandiyalı oldum")
            await ctx.send(embed=embed)
        if "fransa" in args:
            dem = open("vatozlar/fransa.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Fransız Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Fransız oldum")
            await ctx.send(embed=embed)
        if "gürcistan" in args:
            dem = open("vatozlar/Gürcistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Gürci Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Gürcistanlı oldum")
            await ctx.send(embed=embed)
        if "hırvatistan" in args:
            dem = open("vatozlar/Hırvatistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Hırvat Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Hırvat oldum")
            await ctx.send(embed=embed)
        if "irlanda" in args:
            dem = open("vatozlar/İrlanda.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge İrlandalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İrlandalı oldum")
            await ctx.send(embed=embed)
        if "İspanya" in args:
            dem = open("vatozlar/ispanya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge İspanyol Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İspanyol oldum")
            await ctx.send(embed=embed)
        if "İtalya" in args:
            dem = open("vatozlar/italya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge İtalyan Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İtalyan oldum")
            await ctx.send(embed=embed)
        if "izlanda" in args:
            dem = open("vatozlar/izlanda.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge İzlandalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İzlandalı oldum")
            await ctx.send(embed=embed)
        if "karadağ" in args:
            dem = open("vatozlar/Karadağ.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Karadağlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Karadağlı oldum")
            await ctx.send(embed=embed)
        if "kazakistan" in args:
            dem = open("vatozlar/kazakistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Kazak Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kazak oldum")
            await ctx.send(embed=embed)
        if "kıbrıs" in args:
            dem = open("vatozlar/kıbrıs.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Kıbrıslı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kıbrıslı oldum")
            await ctx.send(embed=embed)
        if "kuma" in args:
            fas = open("vatozlar/kuma vatoz.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Dünyayı kumalıyor"))
            await Bot.user.edit(username="Bilge Kuma Vatoz", avatar=fasc)
            vatoz = "kuma"
            print(vatoz)
            embed = Embed(title="Kuma kuma kuma bear izleyip geldim")
            await ctx.send(embed=embed)
        if "kuzey kıbrıs" in args:
            dem = open("vatozlar/kuzey-kıbrıs.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Kuzey kıbrıslı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kuzey kıbrıslı oldum")
            await ctx.send(embed=embed)
        if "makedonya" in args:
            dem = open("vatozlar/kuzey-makedonya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Makedonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Makedonyalı oldum")
            await ctx.send(embed=embed)
        if "letonya" in args:
            dem = open("vatozlar/Latvia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Letonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Letonyalı oldum")
            await ctx.send(embed=embed)
        if "liberteryanist" in args:
            fas = open("vatozlar/librteryenist.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Özgürlüğün dibine vuruyor"))
            await Bot.user.edit(username="Bilge Liberteryanist Vatoz", avatar=fasc)
            vatoz = "liberteryanist"
            print(vatoz)
            embed = Embed(title="Özgürlük, özgürlük ve daha fazla özgürlük")
            await ctx.send(embed=embed)
        if "liechtenstein" in args:
            dem = open("vatozlar/Liechtenstein.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Liechtensteinlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Liechtensteinlı oldum")
            await ctx.send(embed=embed)
        if "litvanya" in args:
            dem = open("vatozlar/lithuania.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Litvanyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Litvanyalı oldum")
            await ctx.send(embed=embed)
        if "lüksemburg" in args:
            dem = open("vatozlar/Lüksemburg.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Lüksemburglu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Lüksemburglu oldum")
            await ctx.send(embed=embed)
        if "Macaristan" in args:
            dem = open("vatozlar/Macaristan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Macar Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Macar oldum")
            await ctx.send(embed=embed)
        if "mao" in args:
            fas = open("vatozlar/maocu.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Kırlarda hazırlanıyor"))
            await Bot.user.edit(username="Bilge Maocu Vatoz", avatar=fasc)
            vatoz = "maocu"
            print(vatoz)
            embed = Embed(title="马克思主义者认为，只有人们的社会实践，才是人们对于外界认识的真理性的标准。……判定认识或理论之是否真理，不是依主观上觉得如何而定，而是依客观上社会实践的结果如何而定。真理的标准只能是社会的实践。")
            await ctx.send(embed=embed)
        if "moldova" in args:
            dem = open("vatozlar/moldovo.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Moldovalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Moldovalı oldum")
            await ctx.send(embed=embed)
        if "monako" in args:
            dem = open("vatozlar/Monaco.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Monakolu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Monakolu oldum")
            await ctx.send(embed=embed)
        if "norveç" in args:
            dem = open("vatozlar/norway.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Norveçli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Norveçli oldum")
            await ctx.send(embed=embed)
        if "onee-san" in args:
            dem = open("vatozlar/onee-san.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Minoru-kun'la yaşıyor"))
            await Bot.user.edit(username="Bilge Onee-san Vatoz", avatar=demo)
            vatoz = "oppai"
            print(vatoz)
            embed = Embed(title="MINORYU-KYUNNNN!!!")
            await ctx.send(embed=embed)
        if "polonya" in args:
            dem = open("vatozlar/poland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Polonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Polonyalı oldum")
            await ctx.send(embed=embed)
        if "radyoaktif" in args:
            fas = open("vatozlar/radyoaktif.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="α ışıması yapıyor"))
            await Bot.user.edit(username="Bilge Radyoaktif Vatoz", avatar=fasc)
            vatoz = "radyoaktif"
            print(vatoz)
            embed = Embed(title="Yanlışlıkla Uranyuma dokundum umarım sıkıntı olmaz")
            await ctx.send(embed=embed)
        if "romanya" in args:
            dem = open("vatozlar/romania.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Romanyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Romanyalı oldum")
            await ctx.send(embed=embed)
        if "rus" in args:
            dem = open("vatozlar/russia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Rus Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Rus oldum")
            await ctx.send(embed=embed)
        if "sırbistan" in args:
            dem = open("vatozlar/Serbia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Sırp Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Sırp oldum")
            await ctx.send(embed=embed)
        if "slovakya" in args:
            dem = open("vatozlar/slovakia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Slovakyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Slovakyalı oldum")
            await ctx.send(embed=embed)
        if "slovenya" in args:
            dem = open("vatozlar/slovenia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Slovenyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Slovenyalı oldum")
            await ctx.send(embed=embed)
        if "stalin" in args:
            dem = open("vatozlar/Stalin.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Stalin Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Россия - священная наша держава")
            await ctx.send(embed=embed)
        if "isveç" in args:
            dem = open("vatozlar/sweden.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge İsveçli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İsveçli oldum")
            await ctx.send(embed=embed)
        if "isviçre" in args:
            dem = open("vatozlar/switzerland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge İsviçreli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İsviçreli oldum")
            await ctx.send(embed=embed)
        if "turan" in args:
            fas = open("vatozlar/turancı.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Haritayı açık maviye boyuyor"))
            await Bot.user.edit(username="Bilge Turancı Vatoz", avatar=fasc)
            vatoz = "turancı"
            print(vatoz)
            embed = Embed(title="Türkler üstün ırktır ve ben de görevim olan cihan fethini gerçekleştireceğim")
            await ctx.send(embed=embed)
        if "türk" in args:
            fas = open("vatozlar/Türkiye.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Yaşayamıyor"))
            await Bot.user.edit(username="Bilge Türk Vatoz", avatar=fasc)
            vatoz = "turancı"
            print(vatoz)
            embed = Embed(title="Ne mutlu Türküm diyene!")
            await ctx.send(embed=embed)
        if "ukrayna" in args:
            dem = open("vatozlar/ukrayna.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Ukraynalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Ukraynalı oldum")
            await ctx.send(embed=embed)
        if "İngiltere" in args:
            dem = open("vatozlar/Unitend-kingdom.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge İngiliz Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İngiliz oldum")
            await ctx.send(embed=embed)
        if "yunanistan" in args:
            dem = open("vatozlar/yunanistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Yunan Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Yunan oldum")
            await ctx.send(embed=embed)
        if "afganistan" in args:
            dem = open("vatozlar/asya/afganistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Afgan Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Afgan oldum")
            await ctx.send(embed=embed)
        if "bahreyn" in args:
            dem = open("vatozlar/asya/bahreyn.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Bahreynli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bahreynli oldum")
            await ctx.send(embed=embed)
        if "bangladeş" in args:
            dem = open("vatozlar/asya/bangladeş.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Bangladeşli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bangladeşli oldum")
            await ctx.send(embed=embed)
        if "bae" in args:
            dem = open("vatozlar/asya/Birleşik arap emirliği.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Cahil Arap Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Arap oldum")
            await ctx.send(embed=embed)
        if "brunei" in args:
            dem = open("vatozlar/asya/Brunei.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Bruneyli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bruneyli oldum")
            await ctx.send(embed=embed)
        if "butan" in args:
            dem = open("vatozlar/asya/butan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Butanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Butanlı oldum")
            await ctx.send(embed=embed)
        if "çin" in args:
            dem = open("vatozlar/asya/Çin.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Çinli Vatoz", avatar=demo)
            vatoz = "sosyalist"
            print(vatoz)
            embed = Embed(title="近前看其詳上寫着秦香蓮那三十二歲 那狀告當朝驸馬郎")
            await ctx.send(embed=embed)
        if "timor" in args:
            dem = open("vatozlar/asya/doğu timor.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Timorlu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Timorlu oldum")
            await ctx.send(embed=embed)
        if "endonezya" in args:
            dem = open("vatozlar/asya/endonezya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Orospu Endonezyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Endonezyalı oldum")
            await ctx.send(embed=embed)
        if "filipinler" in args:
            dem = open("vatozlar/asya/filipinler.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Filipinli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Filipinli oldum")
            await ctx.send(embed=embed)
        if "güneykore" in args:
            dem = open("vatozlar/asya/güney kore.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Koreli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Koreli oldum")
            await ctx.send(embed=embed)
        if "hindistan" in args:
            dem = open("vatozlar/asya/Hindistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Hintli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Hintli oldum")
            await ctx.send(embed=embed)
        if "hong-kong" in args:
            dem = open("vatozlar/asya/hong-kong.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Hong-konglu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Hong-konglu oldum")
            await ctx.send(embed=embed)
        if "ırak" in args:
            dem = open("vatozlar/asya/ırak.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Cahil Iraklı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="أصبحت عراقيا")
            await ctx.send(embed=embed)
        if "iran" in args:
            dem = open("vatozlar/asya/İran.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Cahil İranlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="أصبحت إيرانيًا")
            await ctx.send(embed=embed)
        if "israil" in args:
            dem = open("vatozlar/asya/israil.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge İsrailli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İsrailli oldum")
            await ctx.send(embed=embed)
        if "japonya" in args:
            dem = open("vatozlar/asya/Japonya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşıyor"))
            await Bot.user.edit(username="Ultra Bilge Japon Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="日本人になった")
            await ctx.send(embed=embed)
        if "kamboçya" in args:
            dem = open("vatozlar/asya/kamboçya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Kmer Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kmer oldum")
            await ctx.send(embed=embed)
        if "katar" in args:
            dem = open("vatozlar/asya/Katar.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Zengin Katar Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Katarlı oldum")
            await ctx.send(embed=embed)
        if "kırgızistan" in args:
            dem = open("vatozlar/asya/Kırgızistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Kırgız Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kırgız oldum")
            await ctx.send(embed=embed)
        if "kuveyt" in args:
            dem = open("vatozlar/asya/kuveyt.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Kuveytli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kuveytli oldum")
            await ctx.send(embed=embed)
        if "kuzey-kore" in args:
            dem = open("vatozlar/asya/kuzey kore.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Kuzey Koreli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kuzey Koreli oldum")
            await ctx.send(embed=embed)
        if "laos" in args:
            dem = open("vatozlar/asya/Laos.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Laoslu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Laoslu oldum")
            await ctx.send(embed=embed)
        if "lübnan" in args:
            dem = open("vatozlar/asya/Lübnan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Lübnanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Lübnanlı oldum")
            await ctx.send(embed=embed)
        if "maldivler" in args:
            dem = open("vatozlar/asya/Maldivler.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Maldivli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Maldivli oldum")
            await ctx.send(embed=embed)
        if "malezya" in args:
            dem = open("vatozlar/asya/malezya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Malezyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Malezyalı oldum")
            await ctx.send(embed=embed)
        if "mısır" in args:
            dem = open("vatozlar/asya/mısır.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Mısırlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Mısırlı oldum")
            await ctx.send(embed=embed)
        if "moğol" in args:
            dem = open("vatozlar/asya/moğolistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Moğol Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Moğol oldum")
            await ctx.send(embed=embed)
        if "myanmar" in args:
            dem = open("vatozlar/asya/Myanmar.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Burmalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Burmalı oldum")
            await ctx.send(embed=embed)
        if "nepal" in args:
            dem = open("vatozlar/asya/nepal.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Nepalli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Nepalli oldum")
            await ctx.send(embed=embed)
        if "oman" in args:
            dem = open("vatozlar/asya/oman.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Cahil Omanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Omanlı oldum")
            await ctx.send(embed=embed)
        if "özbekistan" in args:
            dem = open("vatozlar/asya/özbekistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Türk Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Özbek, Türkmen, Uygur, Tatar, Azer bir boydur \nKarakalpak, Kırgız, Kazak bunlar bir soydur")
            await ctx.send(embed=embed)
        if "pakistan" in args:
            dem = open("vatozlar/asya/pakistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Pakistanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Pakistanlı oldum")
            await ctx.send(embed=embed)
        if "singapur" in args:
            dem = open("vatozlar/asya/singapur.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Singapurlu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Singapurlu oldum")
            await ctx.send(embed=embed)
        if "srilanka" in args:
            dem = open("vatozlar/asya/sri lanka.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Sri Lanka Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Sri Lankalı oldum")
            await ctx.send(embed=embed)
        if "suriye" in args:
            dem = open("vatozlar/asya/Suriye.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Cahil Suriyeli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="أصبحت سوريًا")
            await ctx.send(embed=embed)
        if "suudi" in args:
            dem = open("vatozlar/asya/suudi-america.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Cahil Suudi Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="أصبحت عربيا")
            await ctx.send(embed=embed)
        if "tacikistan" in args:
            dem = open("vatozlar/asya/Tacikistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Tacik Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Ман тоҷикам")
            await ctx.send(embed=embed)
        if "tayland" in args:
            dem = open("vatozlar/asya/tayland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Taylandlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Taylandlı oldum")
            await ctx.send(embed=embed)
        if "tayvan" in args:
            dem = open("vatozlar/asya/tayvan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Tayvanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Tayvanlı oldum")
            await ctx.send(embed=embed)
        if "türkmenistan" in args:
            dem = open("vatozlar/asya/türkmenistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Türk Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Özbek, Türkmen, Uygur, Tatar, Azer bir boydur\nKarakalpak, Kırgız, Kazak bunlar bir soydur")
            await ctx.send(embed=embed)
        if "ürdün" in args:
            dem = open("vatozlar/asya/ürdün.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Cahil Ürdünlü Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Arap oldum")
            await ctx.send(embed=embed)
        if "vietnam" in args:
            dem = open("vatozlar/asya/Vietnam.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Vietnam Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Vietnamlı oldum")
            await ctx.send(embed=embed)
        if "yemen" in args:
            dem = open("vatozlar/asya/yemen.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bilge Yemenli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Yemenli oldum")
            await ctx.send(embed=embed)
"""

# Söz


@Bot.command()
async def söz(ctx):
    l = random.randint(1, 7)
    if l == 1:
        Hitlerlist = [
            Hitler1, Hitler2, Hitler3, Hitler4, Hitler5, Hitler6, Hitler7,
            Hitler8, Hitler9, Hitler10, Hitler11, Hitler12, Hitler13, Hitler14,
            Hitler15, Hitler16, Hitler17, Hitler18, Hitler19, Hitler20,
            Hitler21, Hitler22, Hitler23, Hitler24, Hitler25, Hitler26,
            Hitler27, Hitler28, Hitler29, Hitler30, Hitler31, Hitler32,
            Hitler33, Hitler34, Hitler35, Hitler36, Hitler37, Hitler38,
            Hitler39, Hitler40, Hitler41, Hitler42, Hitler43, Hitler44,
            Hitler45, Hitler46, Hitler47, Hitler48, Hitler49, Hitler50,
            Hitler51, Hitler52, Hitler53, Hitler54, Hitler55, Hitler56,
            Hitler57, Hitler58, Hitler59, Hitler60, Hitler61, Hitler62,
            Hitler63, Hitler64, Hitler65, Hitler66, Hitler67, Hitler68,
            Hitler69, Hitler70, Hitler71, Hitler72, Hitler73, Hitler74,
            Hitler75, Hitler76, Hitler77, Hitler78, Hitler79, Hitler80,
            Hitler81, Hitler82, Hitler83, Hitler84, Hitler85, Hitler86,
            Hitler87, Hitler88, Hitler89, Hitler90, Hitler91, Hitler92,
            Hitler93, Hitler94, Hitler95, Hitler96, Hitler97, Hitler98,
            Hitler99, Hitler100, Hitler101, Hitler102, Hitler103, Hitler104,
            Hitler105, Hitler106, Hitler107, Hitler108, Hitler109, Hitler110,
            Hitler111, Hitler112, Hitler113, Hitler114, Hitler115, Hitler116,
            Hitler117, Hitler118, Hitler119, Hitler120, Hitler121, Hitler122,
            Hitler123, Hitler124, Hitler125, Hitler126, Hitler127, Hitler128,
            Hitler129, Hitler130, Hitler131, Hitler132, Hitler133, Hitler134,
            Hitler135, Hitler136, Hitler137, Hitler138, Hitler139, Hitler140,
            Hitler141, Hitler142, Hitler143, Hitler144, Hitler145, Hitler146,
            Hitler147, Hitler148, Hitler149, Hitler150, Hitler151, Hitler152,
            Hitler153, Hitler154, Hitler155, Hitler156, Hitler157, Hitler158,
            Hitler159, Hitler160, Hitler161, Hitler162, Hitler163, Hitler164,
            Hitler165, Hitler166, Hitler167, Hitler168, Hitler169, Hitler170,
            Hitler171, Hitler172, Hitler173, Hitler174, Hitler175, Hitler176,
            Hitler177, Hitler178, Hitler179, Hitler180, Hitler181, Hitler182,
            Hitler183, Hitler184, Hitler185, Hitler186, Hitler187, Hitler188,
            Hitler189, Hitler190, Hitler191, Hitler192, Hitler193, Hitler194,
            Hitler195, Hitler196, Hitler197, Hitler198, Hitler199, Hitler200,
            Hitler201, Hitler202, Hitler203, Hitler204, Hitler205, Hitler206,
            Hitler207, Hitler208, Hitler209, Hitler210, Hitler211, Hitler212,
            Hitler213, Hitler214, Hitler215, Hitler216, Hitler217, Hitler218,
            Hitler219, Hitler220, Hitler221, Hitler222, Hitler223, Hitler224,
            Hitler225, Hitler226, Hitler227, Hitler228, Hitler229, Hitler230,
            Hitler231, Hitler232, Hitler233, Hitler234, Hitler235, Hitler236,
            Hitler237, Hitler238, Hitler239, Hitler240, Hitler241, Hitler242,
            Hitler243, Hitler244, Hitler245, Hitler246, Hitler247, Hitler248,
            Hitler249, Hitler250, Hitler251, Hitler252, Hitler253, Hitler254,
            Hitler255, Hitler256, Hitler257
        ]
        f = random.choice(Hitlerlist)
        embed = Embed(title="Hitler derki", description=f)
        await ctx.send(embed=embed)
    if l == 2:
        Ataturklist = [
            Ataturk1, Ataturk2, Ataturk3, Ataturk4, Ataturk5, Ataturk6,
            Ataturk7, Ataturk8, Ataturk9, Ataturk10, Ataturk11, Ataturk12,
            Ataturk13, Ataturk14, Ataturk15, Ataturk16, Ataturk17, Ataturk18,
            Ataturk19, Ataturk20, Ataturk21, Ataturk22, Ataturk23, Ataturk24,
            Ataturk25, Ataturk26, Ataturk27, Ataturk28, Ataturk29, Ataturk30,
            Ataturk31, Ataturk32, Ataturk33, Ataturk34, Ataturk35, Ataturk36,
            Ataturk37, Ataturk38, Ataturk39, Ataturk40, Ataturk41, Ataturk42,
            Ataturk43, Ataturk44, Ataturk45, Ataturk46, Ataturk47, Ataturk48,
            Ataturk49, Ataturk50, Ataturk51, Ataturk52, Ataturk53, Ataturk54,
            Ataturk55, Ataturk56, Ataturk57, Ataturk58, Ataturk59, Ataturk60,
            Ataturk61, Ataturk62, Ataturk63, Ataturk64, Ataturk65, Ataturk66,
            Ataturk67, Ataturk68, Ataturk69, Ataturk70, Ataturk71, Ataturk72,
            Ataturk73, Ataturk74, Ataturk75, Ataturk76, Ataturk77, Ataturk78,
            Ataturk79, Ataturk80, Ataturk81, Ataturk82, Ataturk83, Ataturk84,
            Ataturk85, Ataturk86, Ataturk87, Ataturk88, Ataturk89, Ataturk90,
            Ataturk91, Ataturk92, Ataturk93, Ataturk94, Ataturk95, Ataturk96,
            Ataturk97, Ataturk98, Ataturk99, Ataturk100, Ataturk101,
            Ataturk102, Ataturk103, Ataturk104, Ataturk105, Ataturk106,
            Ataturk107, Ataturk108, Ataturk109, Ataturk110, Ataturk111,
            Ataturk112, Ataturk113, Ataturk114, Ataturk115, Ataturk116,
            Ataturk117, Ataturk118, Ataturk119, Ataturk120, Ataturk121,
            Ataturk122, Ataturk123, Ataturk124, Ataturk125, Ataturk126,
            Ataturk127, Ataturk128, Ataturk129, Ataturk130, Ataturk131,
            Ataturk132, Ataturk133, Ataturk134, Ataturk135, Ataturk136,
            Ataturk137, Ataturk138, Ataturk139, Ataturk140, Ataturk141,
            Ataturk142, Ataturk143, Ataturk144, Ataturk145, Ataturk146,
            Ataturk147, Ataturk148, Ataturk149, Ataturk150, Ataturk151,
            Ataturk152, Ataturk153, Ataturk154, Ataturk155, Ataturk156,
            Ataturk157, Ataturk158, Ataturk159, Ataturk160, Ataturk161,
            Ataturk162, Ataturk163, Ataturk164, Ataturk165, Ataturk166,
            Ataturk167, Ataturk168, Ataturk169, Ataturk170, Ataturk171,
            Ataturk172, Ataturk173, Ataturk174, Ataturk175, Ataturk176,
            Ataturk177, Ataturk178, Ataturk179, Ataturk180, Ataturk181,
            Ataturk182, Ataturk183, Ataturk184, Ataturk185, Ataturk186,
            Ataturk187
        ]
        f = random.choice(Ataturklist)
        embed = Embed(title="Atatürk derki", description=f)
        await ctx.send(embed=embed)
    if l == 3:
        Leninlist = [
            Lenin1, Lenin2, Lenin3, Lenin4, Lenin5, Lenin6, Lenin7, Lenin8,
            Lenin9, Lenin10, Lenin11, Lenin12, Lenin13, Lenin14, Lenin15,
            Lenin16, Lenin17, Lenin18, Lenin19, Lenin20, Lenin21
        ]
        f = random.choice(Leninlist)
        embed = Embed(title="Lenin derki", description=f)
        await ctx.send(embed=embed)
    if l == 4:
        Stalinlist = [
            Stalin1, Stalin2, Stalin3, Stalin4, Stalin5, Stalin6, Stalin7,
            Stalin8, Stalin9, Stalin10, Stalin11, Stalin12, Stalin13, Stalin14,
            Stalin15, Stalin16, Stalin17, Stalin18, Stalin19, Stalin20,
            Stalin21, Stalin22, Stalin23, Stalin24, Stalin25
        ]
        f = random.choice(Stalinlist)
        embed = Embed(title="Stalin derki", description=f)
        await ctx.send(embed=embed)
    if l == 5:
        Cengizlist = [
            CengizHan1, CengizHan2, CengizHan3, CengizHan4, CengizHan5,
            CengizHan6, CengizHan7, CengizHan8, CengizHan9
        ]
        f = random.choice(Cengizlist)
        embed = Embed(title="Cengiz Han derki", description=f)
        await ctx.send(embed=embed)
    if l == 6:
        CelalŞengörlist = [
            Celal1, Celal2, Celal3, Celal4, Celal5, Celal6, Celal7, Celal8,
            Celal9, Celal10, Celal11, Celal12, Celal13, Celal14, Celal15,
            Celal16, Celal17, Celal18, Celal19, Celal20, Celal21, Celal22,
            Celal23, Celal24, Celal25, Celal26, Celal27, Celal28, Celal29,
            Celal30, Celal31, Celal32, Celal33, Celal34, Celal35, Celal36,
            Celal37, Celal38, Celal39, Celal40, Celal41, Celal42, Celal43
        ]
        f = random.choice(CelalŞengörlist)
        embed = Embed(title="Celal Şengör derki", description=f)
        await ctx.send(embed=embed)
    if l == 7:  # TODO 2.7 Eklenecek
        Metehanlist = [
            Metehan1, Metehan2, Metehan3, Metehan4, Metehan5, Metehan6,
            Metehan7
        ]
        f = random.choice(Metehanlist)
        embed = Embed(title="Metehan derki", description=f)
        await ctx.send(embed=embed)


# Konuşma


@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    if "balık" == message.content and message.author != Bot.user:
        await message.channel.send("BALIKKKK!!!!")
    if "tavşan" == message.content and message.author != Bot.user:
        await message.channel.send("TAVŞANNNN!!!!")
    else:
        await Bot.process_commands(message)


@Bot.command()
async def propaganda(ctx):
    propagandalist = [
        Propaganda1, Propaganda2, Propaganda3, Propaganda4, Propaganda5,
        Propaganda6, Propaganda7, Propaganda8, Propaganda9, Propaganda10,
        Propaganda11, Propaganda12, Propaganda13, Propaganda14, Propaganda15,
        Propaganda16, Propaganda17, Propaganda18, Propaganda19, Propaganda20,
        Propaganda21, Propaganda22, Propaganda23, Propaganda24, Propaganda25,
        Propaganda26, Propaganda27, Propaganda28, Propaganda29, Propaganda30,
        Propaganda31, Propaganda32, Propaganda33, Propaganda34, Propaganda35,
        Propaganda36, Propaganda37, Propaganda38, Propaganda39, Propaganda40,
        Propaganda41, Propaganda42, Propaganda43, Propaganda44, Propaganda45,
        Propaganda46, Propaganda47, Propaganda48, Propaganda49, Propaganda50,
        Propaganda51, Propaganda52, Propaganda53, Propaganda54, Propaganda55,
        Propaganda56, Propaganda57, Propaganda58, Propaganda59, Propaganda60,
        Propaganda61
    ]
    await ctx.send(random.choice(propagandalist))


@Bot.command()
async def r(ctx, *args):
    if "kitap" in args:
        page = requests.get(
            "https://www.generatormix.com/random-book-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div", class_="col-7")
        b = a.text.replace("Get it on Amazon US", "")
        c = b.replace("Fiction", "Kurgu")
        d = c.replace("keywords", "Anahtar Kelimeler")
        e = d.replace("\n\n", "\n")
        f = e.replace("\nby ", "\nYazar: ")
        g = f.replace("Get it on Amazon DE", "")
        embed = Embed(title="Random Kitap Önerisi",
                      description=f,
                      color=0x990000)
        await ctx.send(embed=embed)
    if "film" in args:
        page = requests.get(
            "https://www.generatormix.com/random-movie-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div",
                      class_="thumbnail-col-3 tile-block-inner marg-top first")
        b = a.text.replace("Watch trailer", "")
        d = b.replace("Get it on Amazon US", "")
        embed = Embed(title="Random Film Önerisi",
                      description=d,
                      color=0x990000)
        await ctx.send(embed=embed)
    if "şarkı" in args:
        page = requests.get(
            "https://www.generatormix.com/random-spotify-songs-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div",
                      class_="thumbnail-col-3 tile-block-inner marg-top first")
        z = soup.find(
            "a", class_="btn btn-default col-10 no-float btn-spotify marg-top"
        )["href"]
        b = a.text.replace("No preview available.", "")
        c = b.replace(" Get track on Spotify", z)
        d = c.replace("Get it on Amazon US", "")
        embed = Embed(title="Random Şarkı Önerisi",
                      description=str(d),
                      color=0x990000)
        await ctx.send(embed=embed)
    if "oyun" in args:
        page = requests.get(
            "https://www.generatormix.com/random-steam-games-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("a", class_="btn btn-steam marg-bottom col-12")["href"]
        await ctx.send(a)
    if "anime" in args:
        query = '''
        query ($id: Int) { # Define which variables will be used in the query (id)
        Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
            id
            title {
            romaji
            }
        }
        }
        '''
        l = random.randint(1, 9999)
        variables = {'id': l}
        url = 'https://graphql.anilist.co'
        response = requests.post(url,
                                 json={
                                     'query': query,
                                     'variables': variables
                                 })
        a = json.loads(response.text)
        url = 'https://anilist.co/anime/' + str(l)
        u = a.get('data').get('Media').get('title').get('romaji')
        embed = Embed(title=u, description=url, color=0x990000)
        await ctx.send(embed=embed)
    if "manga" in args:
        l = random.randint(1, 20700)
        url = 'https://myanimelist.net/manga/' + str(l)
        embed = Embed(title="Random manga önerisi",
                      description=url,
                      color=0x990000)
        await ctx.send(embed=embed)


@Bot.command()
async def zar(ctx):
    z = random.randint(1, 6)
    embed = Embed(title="Zar atıldı!", description=z, color=0x990000)
    await ctx.send(embed=embed)


# HOI4 Tips


@Bot.command()
async def hoi4tip(ctx):
    Hoitiplist = [
        hoitip1, hoitip2, hoitip3, hoitip4, hoitip5, hoitip6, hoitip7, hoitip8,
        hoitip9, hoitip10, hoitip11, hoitip12, hoitip13, hoitip14, hoitip15,
        hoitip16, hoitip17, hoitip18, hoitip19, hoitip20, hoitip21, hoitip22,
        hoitip23, hoitip24, hoitip25, hoitip26, hoitip27, hoitip28, hoitip29,
        hoitip30, hoitip31, hoitip32, hoitip33, hoitip34, hoitip35, hoitip36,
        hoitip37, hoitip38, hoitip39, hoitip40, hoitip41, hoitip42, hoitip43,
        hoitip44, hoitip45
    ]
    await ctx.send(random.choice(Hoitiplist))


# Dersler


@Bot.command()
async def ders(ctx, *args):
    if "anime-çeviri" in args:
        await ctx.send(
            "https://i.imgur.com/DZBjYxg.jpg\nhttps://i.imgur.com/X5r544n.jpg")


@Bot.command()
async def cmm(ctx, *args):
    img = Image.open("change-my-mind.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("impact.ttf", 55, encoding="utf-8")
    metin = str(args).replace("(", "")
    metin = metin.replace(")", "")
    metin = metin.replace("'", "")
    metin = metin.replace(",", "")
    metin = metin.replace("-", " ")
    y = 550
    for i, metin in enumerate(metin.split(' ')):
        draw.text((340, y), metin, (0, 0, 0), font=font)
        y = y + 60
    kdgh = "cmm/" + str(random.randint(0, 10000)) + ".jpg"
    img.save(kdgh)
    await ctx.send(' ', file=File(kdgh))


# 4.2


class Menu(ui.View):

    def __init__(self):
        super().__init__()
        self.value = None


@Bot.command()
async def seri(ctx):
    se = [
        seri_1, seri_2, seri_3, seri_4, seri_5, seri_6, seri_7, seri_8, seri_9,
        seri_10, seri_11, seri_12, seri_13, seri_14, seri_15, seri_16, seri_17,
        seri_18, seri_19, seri_20, seri_21, seri_22, seri_23, seri_24, seri_25,
        seri_26
    ]
    seri = random.choice(se)
    view = Menu()
    view.add_item(
        ui.Button(label="Sitemizden oku", style=ButtonStyle.url, url=seri.url))
    embed = Embed(title=seri.ad, description=seri.desc)
    embed.set_image(url=seri.image)
    await ctx.reply(embed=embed, view=view)

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    global b
class RolButton(Button):
    def __init__(self, rol_name):
        global a
        a = rol_name
        super().__init__(label=rol_name, style=ButtonStyle.green)

    async def callback(self, interaction):
        author = interaction.user
        
        role = discord.utils.get(author.guild.roles, name=a)
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

@Bot.command()
async def rol(ctx, seri, *args):
    args = str(args).replace("(", "").replace(")", "").replace("', '", " ").replace("'", "").replace(",", "")
    await ctx.channel.purge(limit=1)
    button = RolButton(args)
    view = MyView()
    guild = ctx.guild
    await guild.create_role(name=args)
    view.add_item(button)
    embed = Embed(
        title= f"{seri} rolleri",
        description=f"{seri} rollerini alabilmek için aşağıdaki tuşlara basın"
    )
    await ctx.send(embed=embed, view=view)

@Bot.command()
async def rolekle(ctx, *args):
    args = str(args).replace("(", "").replace(")", "").replace("', '", " ").replace("'", "").replace(",", "")
    guild = ctx.guild
    new_role = await guild.create_role(name=args)
    # delete command message
    await ctx.message.delete()
    view = MyView()
    async for message in ctx.channel.history(limit=1):
        for row in message.components:
            for button in row.children: 
                view.add_item(RolButton(button.label))
        view.add_item(RolButton(new_role.name))
        await message.edit(view=view)

@Bot.command()
async def Kapat(ctx):
    au = ctx.author.id
    if au == 618214247742308361:
        await ctx.send("Kapatılıyor...")

        exit()
    if au != 618214247742308361:
        await ctx.send("Kapatma yetkiniz yok")


@Bot.command()
async def Yeniden(ctx):
    au = ctx.author.id
    if au == 618214247742308361:
        embed = Embed(title="Yeniden başlatılıyor...", color=0x00ff00)
        await ctx.send(embed=embed)
        os.system("python fasistvatoz.py")
        exit()
    if au != 618214247742308361:
        await ctx.send("Yeniden başlatma yetkiniz yok")


try:
    Bot.run(os.getenv('token'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
