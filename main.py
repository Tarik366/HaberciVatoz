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
async def clear(ctx, amount=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
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
        await ctx.send(Vars.freakout)
    if "haa" in args:
        await ctx.send(Vars.haa)
    if "o7konosuba" in args:
        await ctx.send(Vars.o7konosuba)
    if "nomnom" in args:
        await ctx.send(Vars.nomnom)
    if "like2x" in args:
        await ctx.send(Vars.like2x)
    if "shock" in args:
        await ctx.send(Vars.shock)
    if "o7" in args:
        await ctx.send(Vars.o7)
    if "saxsaphone" in args:
        await ctx.send(Vars.vatozsax)
    if "Dwayne" in args:
        await ctx.send(Vars.dwayne)
    if "hatsoff" in args:
        await ctx.send(Vars.hatsoff)
    if "capitalism" in args:
        await ctx.send(Vars.capitalism)
    if "soviet" in args:
        await ctx.send(Vars.soviet)
    if "sikin" in args:
        await ctx.send(Vars.sikin)
    if "sosyalist" in args:
        await ctx.send(Vars.sosyalistsusamuru)
    if "fire" in args:
        await ctx.send(Vars.fire)
    if "march" in args:
        await ctx.send(Vars.marcharmy)
    if "dance" in args:
        await ctx.send(Vars.irumadance)
    if "inandım" in args:
        await ctx.send(Vars.taaminandım)
    if "kaptan" in args:
        await ctx.send(Vars.kaptansummary)
    if "stare" in args:
        await ctx.send(Vars.stare)
    if "purge" in args:
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
    if "balaced" in args:
        await ctx.send(Vars.balanced)
    if "jii" in args:
        await ctx.send(Vars.jii)


# ekibe başvuru


@Bot.command()
async def başvuru(ctx, *args):
    if "çevirmen" in args:
        await ctx.send(Vars.translater)
    if "editör" in args:
        await ctx.send(Vars.editor)
    else:
        await ctx.channel.purge(limit=1)


# Responds


Bot.run(token_2.token)
