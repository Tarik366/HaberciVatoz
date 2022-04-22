import discord
from discord.ext import commands
import Vars as Vars
import token_2
from token_2 import token

Bot = commands.Bot("!")


@Bot.event
async def on_ready():
    print("merhaba")

# moderatrör komutları


@Bot.command()
async def clear(ctx, amount=100000000000000000000000):
    await ctx.channel.purge(limit=amount)


async def ban(ctx, member: discord.Member, *args, reason="Yok"):
    await member.ban(reason=reason)


async def kick(ctx, member: discord.Member, *args, reason="Yok"):
    await member.kick(reason=reason)


# gifs


@Bot.command()
async def i(ctx, *args):
    if "like" in args:
        await ctx.send(Vars.like)
    if "rage" in args:
        await ctx.send(Vars.rage)
    if "anakuzusu" in args:
        await ctx.send(Vars.anakuzusu)
    if "cry" in args:
        await ctx.send(Vars.cry)
    if "freakout" in args:
        await ctx.send(Vars.frakout)
    if "haa" in args:
        await ctx.send(Vars.haa)
    if "o7konosuba" in args:
        await ctx.send(Vars.o7konosuba)
    if "nomnom" in args:
        await ctx.send(Vars.nom)
    if "like2x" in args:
        await ctx.send(Vars.like2x)
    if "shock" in args:
        await ctx.send(Vars.shock)
    if "o7" in args:
        await ctx.send(Vars.o7)
    if "foksax" in args:
        await ctx.send(Vars.foksax)
    if "dwayne" in args:
        await ctx.send(Vars.dwayne)
    if "hatsoff" in args:
        await ctx.send(Vars.hatsoff)
    if "capitalism" in args:
        await ctx.send(Vars.capitalism)
    if "soviet" in args:
        await ctx.send(Vars.soviet)
    if "sikin" in args:
        await ctx.send(Vars.sikin)
    if "susamuru" in args:
        await ctx.send(Vars.susamuru)
    if "fire" in args:
        await ctx.send(Vars.fire)
    if "marcharmy" in args:
        await ctx.send(Vars.marcharmy)
    if "irumadance" in args:
        await ctx.send(Vars.irumadance)
    if "taam" in args:
        await ctx.send(Vars.taam)
    if "milf" in args:
        await ctx.send(Vars.milf)
    if "stare" in args:
        await ctx.send(Vars.stare)
    if "GreatPurge" in args:
        await ctx.send(Vars.GreatPurge)
    if "napim" in args:
        await ctx.send(Vars.napim)
    if "napimdiyeni" in args:
        await ctx.send(Vars.napimdiyeni)
    if "hatayapar" in args:
        await ctx.send(Vars.hatayapar)
    if "nazifokları" in args:
        await ctx.send(Vars.nazifokları)
    if "darkside" in args:
        await ctx.send(Vars.darkside)
    if "troll" in args:
        await ctx.send(Vars.troll)
    if "yahudiler" in args:
        await ctx.send(Vars.yahudiler)
    if "balanced" in args:
        await ctx.send(Vars.balanced)
    if "jii" in args:
        await ctx.send(Vars.jii)
    if "shipbang" in args:
        await ctx.send(Vars.shipbang)
    if "tank" in args:
        await ctx.send(Vars.tank)
    if "degil" in args:
        await ctx.send(Vars.degil)
    if "air" in args:
        await ctx.send(Vars.air)
    if "kimclap" in args:
        await ctx.send(Vars.kimclap)
    if "worry" in args:
        await ctx.send(Vars.worry)
    if "muso" in args:
        await ctx.send(Vars.muso)
    if "sob" in args:
        await ctx.send(Vars.sob)
    if "kannaeat" in args:
        await ctx.send(Vars.kannaeat)
    if "baka" in args:
        await ctx.send(Vars.baka)
    if "triggered" in args:
        await ctx.send(Vars.triggered)
    if "shinobu" in args:
        await ctx.send(Vars.shinobu)
    if "shy" in args:
        await ctx.send(Vars.shy)
    if "bang2" in args:
        await ctx.send(Vars.bang2)
    if "shutup" in args:
        await ctx.send(Vars.shutup)
    if "save" in args:
        await ctx.send(Vars.save)
    if "aah" in args:
        await ctx.send(Vars.aah)
    if "para" in args:
        await ctx.send(Vars.para)
    if "yay" in args:
        await ctx.send(Vars.yay)
    if "anlıyorum" in args:
        await ctx.send(Vars.anlıyorum)
    if "understood" in args:
        await ctx.send(Vars.understood)
    if "igetit" in args:
        await ctx.send(Vars.igetit)
    if "benzin" in args:
        await ctx.send(Vars.benzin)
    if "why" in args:
        await ctx.send(Vars.why)
    if "celebrate" in args:
        await ctx.send(Vars.celebrate)
    if "braintime" in args:
        await ctx.send(Vars.braintime)
    if "drink" in args:
        await ctx.send(Vars.drink)
    if "bb" in args:
        await ctx.send(Vars.bb)
    if "dot" in args:
        await ctx.send(Vars.dot)
    if "confused" in args:
        await ctx.send(Vars.confused)
    if "lenny" in args:
        await ctx.send(Vars.lenny)
    if "bang" in args:
        await ctx.send(Vars.bang)
    if "slap" in args:
        await ctx.send(Vars.slap)
    if "mad" in args:
        await ctx.send(Vars.mad)
    if "sob2" in args:
        await ctx.send(Vars.sob2)
    if "laugh" in args:
        await ctx.send(Vars.laugh)
    if "evilsmile" in args:
        await ctx.send(Vars.evilsmile)
    if "dissaper" in args:
        await ctx.send(Vars.dissaper)
    if "behind" in args:
        await ctx.send(Vars.behind)
    if "like3" in args:
        await ctx.send(Vars.like3)
    if "whatanime" in args:
        await ctx.send(Vars.whatanime)
    if "nomnomnom" in args:
        await ctx.send(Vars.nomnomnom)
    if "bonk" in args:
        await ctx.send(Vars.bonk)
    if "yarra" in args:
        await ctx.send(Vars.yarra)
    if "katon" in args:
        await ctx.send(Vars.katon)
    if "hug" in args:
        await ctx.send(Vars.hug)
    if "hug2" in args:
        await ctx.send(Vars.hug2)
    if "sob3" in args:
        await ctx.send(Vars.sob3)
    if "animechild" in args:
        await ctx.send(Vars.animechild)
    if "narutodance" in args:
        await ctx.send(Vars.narutodance)
    if "darkstare" in args:
        await ctx.send(Vars.darkstare)
    if "think" in args:
        await ctx.send(Vars.think)
    if "point" in args:
        await ctx.send(Vars.point)
    if "bagıs" in args:
        await ctx.send(Vars.bagıs)
    if "stalinpoint" in args:
        await ctx.send(Vars.stalinpoint)
    if "serve" in args:
        await ctx.send(Vars.serve)
    if "waku" in args:
        await ctx.send(Vars.waku)
    if "fail" in args:
        await ctx.send(Vars.fail)
    if "comunazi" in args:
        await ctx.send(Vars.comunazi)
    if "şaak" in args:
        await ctx.send(Vars.şaak)
    if "doom" in args:
        await ctx.send(Vars.doom)
    if "omori" in args:
        await ctx.send(Vars.omori)
    if "callvatoz" in args:
        await ctx.send(Vars.callvatoz)
    if "vatozlar" in args:
        await ctx.send(Vars.knowvatoz)
    if "papas" in args:
        await ctx.send(Vars.papas)
    if "hans" in args:
        await ctx.send(Vars.hans)


# ekibe başvuru


@Bot.command()
async def başvuru(ctx, *args):
    if "mangaçevirmen" in args:
        await ctx.send(Vars.translater)
    if "mangaeditör" in args:
        await ctx.send(Vars.editor)
    if "webçevirmen" in args:
        await ctx.send(Vars.webtranslater)
    if "webeditör" in args:
        await ctx.send(Vars.webeditor)


# Responds


@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(947935677813772332)
    await channel.send(f"Hoş geldin {member} https://c.tenor.com/ZyzG4mOlthkAAAAC/yoink-dance.gif")


Bot.run(token_2.token)
