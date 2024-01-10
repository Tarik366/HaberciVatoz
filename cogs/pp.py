import discord
from discord import Embed
from discord.ext import commands

class pp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pp(self, ctx, Member: discord.Member):
        emed = Embed(title=f"{Member} adlı kulllanıcının profil fotoğrafı")
        emed = emed.set_image(url=Member.avatar.url)
        await ctx.send(embed=emed)


    @commands.command()
    async def spp(self, ctx):
        icon_url = ctx.guild.icon
        emed = Embed(title=f"{ctx.guild.name} adlı sunucunun profil fotoğrafı")
        emed = emed.set_image(url=icon_url)
        await ctx.send(embed=emed)

async def setup(bot):
    await bot.add_cog(pp(bot))