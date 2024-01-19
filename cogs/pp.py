import discord
from discord import Embed, app_commands
from discord.ext import commands

class pp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="pp", description="Seçilen kullanıcının profil fotoğrafını gönderir")
    @app_commands.describe(member="Kullanıcı etiketi")
    async def pp(self, ctx:discord.Interaction, member: discord.Member):
        emed = Embed(title=f"{member} adlı kulllanıcının profil fotoğrafı")
        emed = emed.set_image(url=member.avatar.url)
        await ctx.send(embed=emed)


    @commands.hybrid_command(name="spp", description="Bulunduğunuz sunucunun profil fotoğrafını gönderir")
    async def spp(self, ctx):
        icon_url = ctx.guild.icon
        emed = Embed(title=f"{ctx.guild.name} adlı sunucunun profil fotoğrafı")
        emed = emed.set_image(url=icon_url)
        await ctx.send(embed=emed)

async def setup(bot):
    await bot.add_cog(pp(bot))