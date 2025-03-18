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

from dotenv.main import load_dotenv
load_dotenv()

# Discord bot settings
cogs = []

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
    await News.msg1(client)

@client.event
async def on_guild_join(self, guild):
    await client.tree.sync()

if discord.ext.commands.errors.CommandNotFound:
    print("")

def application():
    try:
        client.run(os.environ['discord_token'])
    except discord.errors.HTTPException:
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
