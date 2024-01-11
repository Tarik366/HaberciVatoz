# main.py
import discord
from discord.ext import commands
import os
from dotenv.main import load_dotenv
load_dotenv()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("&"),
            intents = discord.Intents.all(),
            help_command = commands.DefaultHelpCommand(dm_help=True)
        )
    
    async def setup_hook(self): #overwriting a handler
        print(f"\033[31mLogged in as {client.user}\033[39m")
        cogs = ["cogs.imageRenderer", "cogs.pp"]
        for filename in cogs:
            await client.load_extension(filename)
        await client.tree.sync()
        print("Loaded cogs")

client = Client()
client.run(os.getenv("token"))