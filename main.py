import discord
from discord.ext import commands, tasks
import Vars as vars

Bot = commands.Bot("!")


@Bot.event
async def on_ready():
    print("merhaba")

# moderatrör komutları


@Bot.command()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@Bot.command()
async def başvuru(ctx, *args):
    if "çevirmen" in args:
        await ctx.send(vars.translater)
    if "editör" in args:
        await ctx.send(vars.editor)
    else:
        await ctx.channel.purge(limit=1)


@Bot.command()
async def i(ctx, *args):
    if "like" in args:
        await ctx.send(vars.like)
    if "rage" in args:
        await ctx.send(vars.rage)
    if "anakuzusu" in args:
        await ctx.send(vars.anakuzusu)
    if "cry" in args:
        await ctx.send(vars.cry)
    if "freakout" in args:
        await ctx.send(vars.freakout)
    if "haa" in args:
        await ctx.send(vars.haa)
    if "o7konosuba" in args:
        await ctx.send(vars.o7konosuba)
    if "nomnom" in args:
        await ctx.send(vars.nomnom)
    if "like2x" in args:
        await ctx.send(vars.like2x)
    if "shock" in args:
        await ctx.send(vars.shock)
    if "o7" in args:
        await ctx.send(vars.o7)
    if "saxsaphone" in args:
        await ctx.send(vars.vatozsax)
    if "Dwayne" in args:
        await ctx.send(vars.dwayne)
    if "hatsoff" in args:
        await ctx.send(vars.hatsoff)
    if "capitalism" in args:
        await ctx.send(vars.capitalism)
    if "soviet" in args:
        await ctx.send(vars.soviet)
    if "sikin" in args:
        await ctx.send(vars.sikin)
    if "sosyalist" in args:
        await ctx.send(vars.sosyalistsusamuru)
    if "fire" in args:
        await ctx.send(vars.fire)
    if "march" in args:
        await ctx.send(vars.marcharmy)
    if "dance" in args:
        await ctx.send(vars.irumadance)
    if "inandım" in args:
        await ctx.send(vars.taaminandım)
    if "kaptan" in args:
        await ctx.send(vars.kaptansummary)
    if "stare" in args:
        await ctx.send(vars.stare)
    if "purge" in args:
        await ctx.send(vars.GreatPurge)
    if "napim" in args:
        await ctx.send(vars.napim)
    if "napimdiyeni" in args:
        await ctx.send(vars.napimdiyeni)
    if "hatayapar" in args:
        await ctx.send(vars.hatayapar)
    if "nazifokları" in args:
        await ctx.send(vars.nazifokları)
    if "darkside" in args:
        await ctx.send(vars.darkside)
    if "troll" in args:
        await ctx.send(vars.troll)
    if "yahudiler" in args:
        await ctx.send(vars.yahudiler)
    if "balaced" in args:
        await ctx.send(vars.balanced)
    if "jii" in args:
        await ctx.send(vars.jii)


Bot.run("ODU1MzI2MjYyMDc1NDU3NTQ2.YMw2qA.9HBOqUW55KIWb9CffNCyfKq2n6c")
