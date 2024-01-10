# Yeni adı ile Haberci

import os.path
import os
import random
import discord
from discord import *
from discord.ext import commands, tasks
import json
from dotenv.main import load_dotenv
import datetime as dt
from keep_alive import keep_alive

# Discord bot settings
intents = Intents.all()
Bot = commands.Bot("!", help_command=None, intents=intents)
load_dotenv()
cogs = ["cogs.imageRenderer", "cogs.pp"]

from cogs.checkNews import News

@Bot.event
async def on_ready():
    keep_alive()
    for cog in cogs:
        try:
            await Bot.load_extension(cog)
            print(cog + " was loaded.")
        except Exception as e:
            print(e)
    await News.msg1(Bot, True)

# TODO: Help komutu yenilenecek

@Bot.command()
async def yardım(ctx):
    embed = Embed(title="Yardım", description="Yardım komutları", color=0x8a0a01)
    embed.add_field(name="!yardım", value="yardım komutlarını gösterir", inline=False)
    embed.add_field(name="!yak <@Banlanacak kişi>", value="Etiketlenen kişiyi yakar(banlar)",
                    inline=False)
    embed.add_field(name="!kick <@kicklenecek kişi>", value="Etiketlenen kişiyi kickler",
                    inline=False)
    embed.add_field(name="!i <resim ismi>",value="110'dan fazla gif veya resimden seçileni atar. Resim listesi için !i help yazabilirsiniz", inline=False)
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
    iembed = Embed(title="Bir hata oluştu", description="Büyük ihtimalle bir yazım yanlışı yapmış olabilirsin.\n\nBu komutta kullanabileceğin değişkenler:\nmangaçeviri\nmangaeditör\nwebçeviri\nwebeditör\nanimeçeviri")
    try:
        tr = Embed(title="Başvuru formu", description=ilist.get(args[0]))
        await ctx.send(embed=tr)
    except:
        await ctx.send(embed=iembed)

# Adak sistemi

from mongodb import adak

@Bot.command()
async def ada(ctx, *args):
    author = ctx.message.author
    theHolyThings = ["Alya", "tarık"]
    if args in theHolyThings:
        msg = Embed(title="Ne yazık ki adağınız kabul edilemedi")
    try:
        adak(author.id, author.name, author.avatar.url, ' '.join(args))
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.send(embed=msg)
    except:
        msg = Embed(title="Ne yazık ki adağınız kabul edilemedi")
        await ctx.send(embed=msg)

# TODO: Buralar hep dutluktu dedirt

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
        """
if l == 3:
        f = random.choice(list(LeninList))
        embed = Embed(title="Lenin derki", description=LeninList[f])
        await ctx.send(embed=embed)
"""
    if l == 5:
        f = random.choice(list(Cengizlist))
        embed = Embed(title="Cengiz Han derki", description=f)
        await ctx.send(embed=embed)
    if l == 6:
        f = random.choice(list(CelalŞengörlist))
        embed = Embed(title="Celal Şengör derki", description=f)
        await ctx.send(embed=embed)
    if l == 7:  
        f = random.choice(list(Metehanlist))
        embed = Embed(title="Metehan derki", description=(AlyaList[f]))
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

from propaganda import propagandalist

@Bot.command()
async def propaganda(ctx):
    await ctx.send(random.choice(propagandalist))

# Dersler

@Bot.command()
async def ders(ctx, *args):
    if "anime-çeviri" in args:
        await ctx.send("https://i.imgur.com/DZBjYxg.jpg\nhttps://i.imgur.com/X5r544n.jpg")
    if "manga-edit" in args:
        await ctx.send("https://drive.google.com/file/d/12Mz-LchkUk1LIIm0lyoT7eagNDx4vExI/view?usp=sharing\nhttps://drive.google.com/file/d/15YyU80w498WVgP6vgySKWRXD99o98z_b/view?usp=sharing")

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
    ctx = Bot.get_channel(MainChannel)
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
