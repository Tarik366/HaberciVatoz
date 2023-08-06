import os.path
import os
import random
import discord
from discord import *
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import requests
import json
from dotenv.main import load_dotenv
from PIL import Image, ImageFont, ImageDraw
import datetime as dt
import feedparser
from keep_alive import keep_alive

Channela = 813886736051863554
Channel = 1050431310163886191
guildida = 798641429056454686
guildid = 968587864805883995
roleid = 1034897409668546631
roleida = 996895568381091931
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


from Functions import getSeriePicture, getSerieId


@tasks.loop(seconds=10)
async def msg1():

    # AthenaFansubのサイトから最後のエピソードとシリーズを取得してる
    lkkl = feedparser.parse("https://athenafansub.com/feed/")
    entry = lkkl.entries[0]

    le = open("lastEntry.txt", "r", encoding="utf-8")
    ar = le.read()

    class n:
        title = entry.title
        link = entry.link
        cat = entry.category
        catt = cat.replace(" ", "-")
        catt = catt.replace("'", "").lower()

    h = f"https://athenafansub.com/manga/{n.catt}"
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

        channeul = Bot.get_channel(Channel)
        AthenaDiscord = Bot.get_guild(guildid)

        tümSeriler = AthenaDiscord.get_role(roleid)
        SerieRoleIds = getSerieId(hgf)

        if SerieRoleIds == ["boş"]:
            await channeul.send(f"{tümSeriler.mention}", embed=emed)
        else:
            MentionMessage = ""
            for SerieRoleId in SerieRoleIds:
                SerieRole = AthenaDiscord.get_role(SerieRoleId)
                MentionMessage += SerieRole.mention
            await channeul.send(f"{MentionMessage}\n{tümSeriler.mention}",
                               embed=emed)

        with open("lastEntry.txt", "w", encoding="utf-8") as wle:
            wle.write(sentry)


@tasks.loop(seconds=10)
async def msg2():

    # anime.athenafansub.comから最後のエピソードとシリーズを取得してる
    NF = feedparser.parse("https://anime.athenafansub.com/feed/")
    entry = NF.entries[0]

    le = open("lastAnimeEntry.txt", "r", encoding="utf-8")
    ar = le.read()

    class n:
        title = entry.title
        link = entry.link
        cat = entry.category
        catt = cat.replace(" ", "-")
        catt = catt.replace("'", "").lower()

    h = ""
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
                     description=f"okumak için {entry.link}",
                     url=entry.link)

        hgf = getSeriePicture(h, anime=True)
        emed = emed.set_image(url=hgf)

        channtel = Bot.get_channel(Channel)
        AthenaDiscord = Bot.get_guild(798641429056454686)

        tümSeriler = AthenaDiscord.get_role(996895568381091931)
        SerieRoleIds = getSerieId(h)

        if SerieRoleIds == ["boş"]:
            await channtel.send(f"{tümSeriler.mention}", embed=emed)
        else:
            MentionMessage = ""
            for SerieRoleId in SerieRoleIds:
                SerieRole = AthenaDiscord.get_role(SerieRoleId)
                MentionMessage += SerieRole.mention
            await channtel.send(f"{MentionMessage}\n{tümSeriler.mention}",
                               embed=emed)

        with open("lastAnimeEntry.txt", "w", encoding="utf-8") as wle:
            wle.write(sentry)

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

from i import ilist

@Bot.command()
async def i(ctx, *args):
    try:
        await ctx.send(ilist.get(args[0]))
    except:
        iembed = Embed(title="Bir hata oluştu", description="Büyük ihtimalle bir yazım yanlışı yapmış olabilirsin")
        await ctx.send(embed=iembed)

# ekibe başvuru

from basvuru import basvurulist

@Bot.command()
async def başvuru(ctx, *args):
    try:
        tr = Embed(title="Başvuru formu", description=ilist.get(args[0]))
        await ctx.send(embed=tr)
    except:
        iembed = Embed(title="Bir hata oluştu", description="Büyük ihtimalle bir yazım yanlışı yapmış olabilirsin.\n\nBu komutta kullanabileceğin değişkenler:\nmangaçeviri\nmangaeditör\nwebçeviri\nwebeditör\nanimeçeviri")
        await ctx.send(embed=iembed)

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

import alya as a

@Bot.command()
async def alya(ctx, *args):
    if "ak4747" in args:
        dem = open("vatozlar/ak4747.jpg", 'rb')
        demo = dem.read()
        await Bot.change_presence(activity=Game(name="Etrafa sikmaca"))
        await Bot.user.edit(username="Bilge AK-4747 Vatoz", avatar=demo)
        embed = Embed(title="Bir can karşılığında bir can. Bence mantıklı bir anlaşma")
        await ctx.send(embed=embed)

# Söz

from Sözler.Alya import *
from Sözler.Atatürk import *
from Sözler.Lenin import *
from Sözler.Stalin import *
from Sözler.Cengiz import *
from Sözler.CelalŞengör import *
from Sözler.MeteHan import *

@Bot.command()
async def söz(ctx):

    l = random.randint(1, 7)
    if l == 1:
        f = random.choice(list(AlyaList))
        embed = Embed(title="Alya-sama derki", description=AlyaList[f])
        await ctx.send(embed=embed)
    if l == 2:
        f = random.choice(list(Ataturklist))
        embed = Embed(title="Atatürk derki", description=Ataturklist[f])
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
        f = random.choice(list(Cengizlist))
        embed = Embed(title="Cengiz Han derki", description=f)
        await ctx.send(embed=embed)
    if l == 6:
        f = random.choice(list(CelalŞengörlist))
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
    if "alya" == message.content and message.author != Bot.user:
        await message.channel.send("ALYA-SAMA!!!!!!")
    if "tavşan" == message.content and message.author != Bot.user:
        await message.channel.send("TAVŞANNNN!!!!")
    else:
        await Bot.process_commands(message)

from propaganda import *

@Bot.command()
async def propaganda(ctx):
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

# HOI4 Tips

from hoi4tips import *

@Bot.command()
async def hoi4tip(ctx):
    await ctx.send(random.choice(list(Hoitiplist)))

# Dersler

@Bot.command()
async def ders(ctx, *args):
    if "anime-çeviri" in args:
        await ctx.send("https://i.imgur.com/DZBjYxg.jpg\nhttps://i.imgur.com/X5r544n.jpg")
    if "manga-edit" in args:
        await ctx.send("https://drive.google.com/file/d/12Mz-LchkUk1LIIm0lyoT7eagNDx4vExI/view?usp=sharing\nhttps://drive.google.com/file/d/15YyU80w498WVgP6vgySKWRXD99o98z_b/view?usp=sharing")

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

from Seriler import *

@Bot.command()
async def seri(ctx):
    seri = random.choice(SeriList)
    view = Menu()
    view.add_item(
        ui.Button(label="Sitemizden oku", style=ButtonStyle.url, url=seri.url)
    )
    embed = Embed(title=seri.ad, description=seri.desc)
    embed.set_image(url=seri.image)
    await ctx.reply(embed=embed, view=view)

from discord.utils import get

class RolMenu(ui.View):

    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Japonca sohbet", style=ButtonStyle.grey)
    async def Japonca(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Japonca Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(
                f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

    @discord.ui.button(label="Korece sohbet", style=ButtonStyle.grey)
    async def Korece(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Korece Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(
                f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

    @discord.ui.button(label="Rusça sohbet", style=ButtonStyle.grey)
    async def Rusça(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Rusça Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(
                f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

    @discord.ui.button(label="Almanca sohbet", style=ButtonStyle.grey)
    async def Almanca(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Almanca Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(
                f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)


@tasks.loop(minutes=3)
async def dilrol():
    view = RolMenu()
    embed = Embed(
        title="Dillere göre sohbet rolleri",
        description="Aynı dili bilen insanlarla konuşma alıştırması yapabileceğiniz kanalları açar"
    )
    ctx = Bot.get_channel(Channel)
    await ctx.send(embed=embed, view=view)


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

if discord.ext.commands.errors.CommandNotFound:
    print("")

try:
    Bot.run(os.getenv('token'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
