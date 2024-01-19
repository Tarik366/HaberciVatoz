from discord.ext import commands

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def kapat(self, ctx):
        au = ctx.author.id
        if au == 618214247742308361:
            await ctx.send("Kapatılıyor...")
            raise Exception('Close')
        if au != 618214247742308361:
            await ctx.send("Kapatma yetkiniz yok")

async def setup(bot):
    await bot.add_cog(admin(bot))