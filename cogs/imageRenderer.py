import discord
from discord import Embed, app_commands
from discord.ext import commands
import textwrap
from PIL import Image, ImageFont, ImageDraw
import random

class render(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Daha fazla komut ekle

    @commands.hybrid_command(name="change_my_mind", description="Kendi Change My Mind'ını oluşturur.")
    @app_commands.describe(metin="Yazılacak metin")
    async def cmm(self, ctx, metin:str):
        img = Image.open("HaberciVatoz/change-my-mind.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("HaberciVatoz/Roboto-Thin.ttf", 55)
        metin.encode("utf-8")
        y = 550
        margin = offset = 340
        for line in textwrap.wrap(metin, width=20):
            draw.text((margin, y), line, font=font, fill="#000000")
            y += 60
        kdgh = "HaberciVatoz/cmm/" + str(random.randint(0, 10000)) + ".jpg"
        img.save(kdgh)
        await ctx.send(' ', file=discord.File(kdgh))
    
async def setup(bot):
    await bot.add_cog(render(bot))
