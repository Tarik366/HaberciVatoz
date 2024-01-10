import os
from dotenv.main import load_dotenv

load_dotenv()

from interactions import slash_command, SlashContext, Client, Intents, listen

bot = Client(intents=Intents.DEFAULT)

@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Ready")
    print(f"This bot is owned by {bot.owner}")

@slash_command(name="add", description="My first command :)")
async def my_command_function(ctx: SlashContext):
    await ctx.send("Hello World")

@slash_command(name="my_long_command", description="My second command :)")
async def my_long_command_function(ctx: SlashContext):
    # need to defer it, otherwise, it fails
    await ctx.defer()

    await ctx.send("Hello World")

bot.start(os.getenv('token'))