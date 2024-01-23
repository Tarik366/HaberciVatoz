# Yeni adı ile Haberci

import os.path
import os
import random
import discord
from discord import * # type: ignore
from discord.ext import commands, tasks
import json
import datetime as dt
from keep_alive import keep_alive

# Discord bot settings
cogs = ["cogs.buttons", "cogs.imageRenderer", "cogs.pp", "cogs.selectFromList", "cogs.random"]

class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("!"),
            intents = discord.Intents.all(),
            help_command = commands.DefaultHelpCommand(dm_help=True)
        )
    
    async def setup_hook(self): #overwriting a handler
        for cog in cogs:
            try:
                await client.load_extension(cog)
                print(cog + " was loaded.")
            except Exception as e:
                print(e)
        # TODO - delete old commands
        await client.tree.sync()
        print("Loaded cogs")

client = Client()
Bot = client

from cogs.checkNews import News as News

@client.event
async def on_ready():
    keep_alive()
    await News.msg1(client)
    await News.msg2(client)

@client.event
async def on_guild_join(self, guild):
    await client.tree.sync()

# Konuşma

@client.event
async def on_message(message):
    if message.author == Bot.user:
        return
    if "alya" == message.content and message.author != Bot.user:
        await message.channel.send("ALYA-SAMA!!!!!!")
    if "tavşan" == message.content and message.author != Bot.user:
        await message.channel.send("TAVŞANNNN!!!!")
    else:
        await Bot.process_commands(message)

if discord.ext.commands.errors.CommandNotFound:
    print("")

try:
    print(os.environ['discord_token'])
    client.run(os.environ['discord_token'])
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')