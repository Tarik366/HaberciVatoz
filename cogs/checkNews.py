import discord
from discord import Embed
from discord.ext import commands, tasks
import feedparser
from Functions import getSeriePicture, getSerieId
from bs4 import BeautifulSoup
import requests

class News(): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    # TODO: repl.it'den latest versiyonr hali ile değiştirilececk
    
    # Role identifications
    MainChannel = 813886736051863554
    devChannel = 1050431310163886191
    AthenaGuildId = 798641429056454686
    devGuildId = 968587864805883995
    devRoleId = 1034897409668546631 
    allRolesId = 996895568381091931
    
    sites = ["https://athenamanga.com/", "https://anime.athenamanga.com/"]

    from Functions import getSeriePicture, getSerieId

    def sanitize(catt):
        catt = catt.replace(" ", "-")
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

    @tasks.loop(seconds=10)
    async def msg1(self, is_dev: bool):
        print("10 saniye geçti")

        if is_dev == True:
            MainChannel = News.devChannel
            AthenaGuildId = News.devGuildId
            allRolesId = News.devRoleId
        else:
            MainChannel = News.MainChannel
            AthenaGuildId = News.AthenaGuildId
            allRolesId = News.allRolesId

        # AthenaFansubのサイトから最後のエピソードとシリーズを取得してる
        lkkl = feedparser.parse(f"{News.sites[0]}feed/")
        entry = lkkl.entries[0]

        le = open("lastEntry.txt", "r", encoding="utf-8")
        ar = le.read()

        class n:
            title = entry.title
            link = entry.link
            cat = entry.category
            catt = News.sanitize(cat)

        h = f"{News.sites[0]}manga/{n.catt}"
        sentry = entry.title

        if sentry not in str(ar):

            headers = {
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            }
            sou = requests.get(h, headers=headers)
            soup = BeautifulSoup(sou.content, 'html.parser')

            emed = Embed(title=f"{entry.title} yayında keyifli okumalar!",
                        description=f"okumak için {entry.link}",
                        url=entry.link)

            hgf = getSeriePicture(h)
            emed = emed.set_image(url=hgf)

            channeul = self.bot.get_channel(MainChannel)
            AthenaDiscord = self.bot.get_guild(AthenaGuildId)

            tümSeriler = AthenaDiscord.get_role(allRolesId)
            SerieRoleIds = getSerieId(h)
            print(SerieRoleIds)

            if SerieRoleIds == ["boş"]:
                await channeul.send(f"{tümSeriler.mention}", embed=emed)
            # if  n.title
            else:
                MentionMessage = ""
                for SerieRoleId in SerieRoleIds:
                    SerieRole = AthenaDiscord.get_role(SerieRoleId)
                    MentionMessage += SerieRole.mention
                    print(MentionMessage)
                    await channeul.send(f"{MentionMessage}\n{tümSeriler.mention}",
                                        embed=emed)

            with open("lastEntry.txt", "w", encoding="utf-8") as wle:
                wle.write(sentry)

    @tasks.loop(seconds=10)
    async def msg2(self, is_dev: bool):
        print("10 saniye geçti")

        if is_dev == True:
            MainChannel = News.devChannel
            AthenaGuildId = News.devGuildId
            allRolesId = News.devRoleId
        else:
            MainChannel = News.MainChannel
            AthenaGuildId = News.AthenaGuildId
            allRolesId = News.allRolesId

        # anime.athenafansub.comから最後のエピソードとシリーズを取得してる
        NF = feedparser.parse(f"{News.sites[1]}feed/")
        entry = NF.entries[0]

        le = open("lastAnimeEntry.txt", "r", encoding="utf-8")
        ar = le.read()

        class n:
            title = entry.title
            link = entry.link
            cat = entry.category
            catt = News.sanitize(cat)

        h = f"{News.sites[1]}anime/{n.catt}"
        sentry = entry.title

        if sentry not in str(ar):

            headers = {
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            }
            sou = requests.get(n.link, headers=headers)
            soup = BeautifulSoup(sou.content, 'html.parser')

            sa = soup.find('a', id='anime_title')
            h = sa['href']

            emed = Embed(title=f"{entry.title} yayında keyifli okumalar!",
                        description=f"izlemek için {entry.link}",
                        url=entry.link)

            hgf = getSeriePicture(h, anime=True)
            emed = emed.set_image(url=hgf)

            channeul = self.bot.get_channel(MainChannel)
            AthenaDiscord = self.bot.get_guild(AthenaGuildId)

            tümSeriler = AthenaDiscord.get_role(allRolesId)
            SerieRoleIds = getSerieId(h)
            print(SerieRoleIds)

            if SerieRoleIds == ["boş"]:
                await channeul.send(f"{tümSeriler.mention}", embed=emed)
            else:
                MentionMessage = ""
                for SerieRoleId in SerieRoleIds:
                    SerieRole = AthenaDiscord.get_role(SerieRoleId)
                    MentionMessage += SerieRole.mention
                    print(MentionMessage)
                    await channeul.send(f"{MentionMessage}\n{tümSeriler.mention}",
                                        embed=emed)

            with open("lastAnimeEntry.txt", "w", encoding="utf-8") as wle:
                wle.write(sentry)