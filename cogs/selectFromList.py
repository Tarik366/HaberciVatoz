import discord
from discord import Embed
from discord.ext import commands

class select(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # gifs

    from i import ilist

    @commands.command()
    async def i(ctx, *args):
        try:
            await ctx.send(select.ilist.get(args[0]))
        except:
            iembed = Embed(title="Bir hata oluştu", description="Büyük ihtimalle bir yazım yanlışı yapmış olabilirsin")
            await ctx.send(embed=iembed)

    # ekibe başvuru

    from basvuru import basvurulist

    @commands.command()
    async def başvuru(ctx, *args):
        iembed = Embed(title="Bir hata oluştu", description="Büyük ihtimalle bir yazım yanlışı yapmış olabilirsin.\n\nBu komutta kullanabileceğin değişkenler:\nmangaçeviri\nmangaeditör\nwebçeviri\nwebeditör\nanimeçeviri")
        try:
            tr = Embed(title="Başvuru formu", description=select.basvurulist.get(args[0]))
            await ctx.send(embed=tr)
        except:
            await ctx.send(embed=iembed)

    # TODO: Buralar hep dutluktu dedirt

    import alya as a

    @commands.command()
    async def alya(self, ctx, *args):
        if "ak4747" in args:
            dem = open("vatozlar/ak4747.jpg", 'rb')
            demo = dem.read()
            await self.bot.change_presence(activity=Game(name="Etrafa sikmaca"))
            await self.bot.user.edit(username="Bilge AK-4747 Vatoz", avatar=demo)
            embed = Embed(title="Bir can karşılığında bir can. Bence mantıklı bir anlaşma")
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(select(bot))