
from discord import Embed, ui, ButtonStyle
from discord.ext import commands

class random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Söz

    from Sözler.Atatürk import Ataturklist
    from Sözler.Cengiz import Cengizlist
    from Sözler.CelalŞengör import CelalŞengörlist
    from Sözler.MeteHan import Metehanlist
    import random

    @commands.hybrid_command(name="söz", description="Rastgele, önemli bir kişinin, bir sözünü yazar")
    async def söz(self, ctx):

        # TODO -  Search all files in Sözler folder
        # TODO -  Select randomly a file and import it
        # TODO -  Select randomly a text and send it

        l = random.random.randint(1, 7)
        if l == 2:
            f = random.random.choice(list(random.Ataturklist))
            embed = Embed(title="Atatürk derki", description=random.Ataturklist[f])
            await ctx.send(embed=embed)
        if l == 5:
            f = random.random.choice(list(random.Cengizlist))
            embed = Embed(title="Cengiz Han derki", description=f)
            await ctx.send(embed=embed)
        if l == 6:
            f = random.random.choice(list(random.CelalŞengörlist))
            embed = Embed(title="Celal Şengör derki", description=f)
            await ctx.send(embed=embed)
        if l == 7:  
            f = random.random.choice(list(random.Metehanlist))
            embed = Embed(title="Metehan derki", description=(random.Metehanlist[f]))
            await ctx.send(embed=embed)

    from propaganda import propagandalist

    @commands.hybrid_command()
    async def propaganda(self, ctx):
        await ctx.send(random.random.choice(random.propagandalist))

    class Menu(ui.View):

        def __init__(self):
            super().__init__()
            self.value = None
    
    from Seriler import getSeries

    @commands.hybrid_command()
    async def seri(self, ctx):
        seriList = random.getSeries()
        seri = random.random.choice(seriList)
        view = random.Menu()
        view.add_item(
            ui.Button(label="Sitemizden oku", style=ButtonStyle.url, url=seri.url)
        )
        embed = Embed(title=seri.ad, description=seri.desc)
        embed.set_image(url=seri.image)
        await ctx.reply(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(random(bot))