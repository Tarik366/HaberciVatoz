from discord import Embed
from discord.ext import commands, tasks
import feedparser
from HaberciVatoz.Functions import getSeriePicture, getSerieId, getSerieLink
from bs4 import BeautifulSoup
import requests

class News(): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    # TODO: repl.it'den latest versiyonr hali ile değiştirilececk
    
    # Role identifications
    is_dev = False
    MainChannel = 813886736051863554
    devChannel = 1050431310163886191
    AthenaGuildId = 798641429056454686
    devGuildId = 968587864805883995
    devRoleId = 1034897409668546631 
    allRolesId = 996895568381091931
    
    sites = ["https://athenamanga.com/", "https://anime.athenamanga.com/"]

    @tasks.loop(seconds=10)
    async def msg1(ctx):

        if News.is_dev == True:
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

        le = open("HaberciVatoz/lastEntry.txt", "r", encoding="utf-8")
        ar = le.read()

        class n:
            title = entry.title
            link = entry.link
            serieLink = getSerieLink(link)

        sentry = entry.title

        if sentry not in str(ar):

            headers = {
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            }
            sou = requests.get(n.serieLink, headers=headers)
            soup = BeautifulSoup(sou.content, 'html.parser')

            emed = Embed(title=f"{entry.title} yayında keyifli okumalar!", description=f"okumak için {entry.link}", url=entry.link)

            hgf = getSeriePicture(n.serieLink)
            emed = emed.set_image(url=hgf)

            AthenaDiscord = ctx.get_guild(AthenaGuildId)
            channeul = AthenaDiscord.get_channel(MainChannel)

            tümSeriler = AthenaDiscord.get_role(allRolesId)
            SerieRoleIds = getSerieId(n.serieLink)

            if SerieRoleIds == ["boş"]:
                await channeul.send(f"{tümSeriler.mention}", embed=emed)
            # if  n.title
            else:
                MentionMessage = ""
                for SerieRoleId in SerieRoleIds:
                    SerieRole = AthenaDiscord.get_role(SerieRoleId)
                    MentionMessage += SerieRole.mention
                    await channeul.send(f"{MentionMessage}\n{tümSeriler.mention}", embed=emed)

            with open("lastEntry.txt", "w", encoding="utf-8") as wle:
                wle.write(sentry)

    @tasks.loop(seconds=10)
    async def msg2(self):

        if News.is_dev == True:
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

        le = open("HaberciVatoz/lastAnimeEntry.txt", "r", encoding="utf-8")
        ar = le.read()

        class n:
            title = entry.title
            link = entry.link
            catt = getSerieLink(link, True)

        sentry = entry.title

        if sentry not in str(ar):

            headers = {
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            }
            sou = requests.get(n.link, headers=headers)
            soup = BeautifulSoup(sou.content, 'html.parser')

            emed = Embed(title=f"{entry.title} yayında keyifli okumalar!", description=f"izlemek için {entry.link}", url=entry.link)

            hgf = getSeriePicture(n.serieLink, anime=True)
            emed = emed.set_image(url=hgf)

            channeul = self.get_channel(MainChannel)
            AthenaDiscord = self.get_guild(AthenaGuildId)

            tümSeriler = AthenaDiscord.get_role(allRolesId)
            SerieRoleIds = getSerieId(n.serieLink)

            if SerieRoleIds == ["boş"]:
                await channeul.send(f"{tümSeriler.mention}", embed=emed)
            else:
                MentionMessage = ""
                for SerieRoleId in SerieRoleIds:
                    SerieRole = AthenaDiscord.get_role(SerieRoleId)
                    try:
                        MentionMessage += SerieRole.mention
                    except:
                        pass
                    await channeul.send(f"{MentionMessage}\n{tümSeriler.mention}", embed=emed)

            with open("lastAnimeEntry.txt", "w", encoding="utf-8") as wle:
                wle.write(sentry)