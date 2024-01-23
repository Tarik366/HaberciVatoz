import discord
from discord import Embed, app_commands
from discord.ext import commands

class select(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # gifs

    from i import ilist

    @commands.hybrid_command(name="resim", description="Adı yazılan resmi atar")
    @app_commands.describe(resim_adı="Resim adı")
    async def i(self, ctx:discord.Interaction, resim_adı:str):
        try:
            await ctx.send(select.ilist.get(resim_adı[0]))
        except:
            iembed = Embed(title="Bir hata oluştu", description="Büyük ihtimalle bir yazım yanlışı yapmış olabilirsin")
            await ctx.send(embed=iembed)

    # ekibe başvuru

    from basvuru import basvurulist

    @commands.hybrid_command(name="başvuru")
    @app_commands.describe(form_adı="Form adı")
    async def başvuru(self, ctx:discord.Interaction, form_adı:str):
        iembed = Embed(title="Bir hata oluştu", description="Büyük ihtimalle bir yazım yanlışı yapmış olabilirsin.\n\nBu komutta kullanabileceğin değişkenler:\nmangaçeviri\nmangaeditör\nwebçeviri\nwebeditör\nanimeçeviri")
        try:
            tr = Embed(title="Başvuru formu", description=select.basvurulist.get(form_adı[0]))
            await ctx.send(embed=tr)
        except:
            await ctx.send(embed=iembed)

    #FIXME - ASAP
    # from idea import get_idea

    # @commands.hybrid_command(name="idea")
    # @app_commands.describe(idea_adı="Fikir adı")
    # async def alya(self, ctx, idea_adı:str):
    #     id = select.get_idea(idea_adı)
    #     try:
    #         dem = open(id.pp, 'rb')
    #         demo = dem.read()
    #         await self.bot.change_presence(activity=discord.Game(name=id.game))
    #         await self.bot.user.edit(username=id.name, avatar=demo)
    #         embed = Embed(title=id.ocm)
    #         await ctx.send(embed=embed)
    #     except:
    #         embed = Embed(title="Bir hata oluştu", description="Lütfen sitemizden geçerli idealara bakınız")
    #         await ctx.send(embed=embed)
    
    # Dersler

    @commands.hybrid_command()
    @app_commands.describe(ders="Seçilen ders")
    async def ders(self, ctx, ders:str):
        if "anime-çeviri" in ders:
            await ctx.send("https://i.imgur.com/DZBjYxg.jpg\nhttps://i.imgur.com/X5r544n.jpg")
        if "manga-edit" in ders:
            await ctx.send("https://drive.google.com/file/d/12Mz-LchkUk1LIIm0lyoT7eagNDx4vExI/view?usp=sharing\nhttps://drive.google.com/file/d/15YyU80w498WVgP6vgySKWRXD99o98z_b/view?usp=sharing")
    
    # Adak sistemi

    from mongodb import adaklara_ekle

    @commands.hybrid_command()
    @app_commands.describe(adak="Adanacak şey")
    async def ada(self, ctx, adak:str):
        author = ctx.message.author
        theHolyThings = ["Alya", "tarık"]
        if adak in theHolyThings:
            msg = Embed(title="Ne yazık ki adağınız kabul edilemedi")
        try:
            select.adaklara_ekle(author.id, author.name, author.avatar.url, ' '.join(adak))
            msg = Embed(title="Adağınız kabul edildi")
            await ctx.send(embed=msg)
        except:
            msg = Embed(title="Ne yazık ki adağınız kabul edilemedi")
            await ctx.send(embed=msg)

async def setup(bot):
    await bot.add_cog(select(bot))