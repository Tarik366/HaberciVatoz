import discord
from discord import *
from discord import Embed, app_commands
from discord.ext import commands

class Menu(ui.View):

    def __init__(self):
        super().__init__()
        self.value = None

from discord.utils import get

class RolMenu(ui.View):

    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Japonca sohbet", style=ButtonStyle.grey)
    async def Japonca(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Japonca Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(
                f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

    @discord.ui.button(label="Korece sohbet", style=ButtonStyle.grey)
    async def Korece(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Korece Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(
                f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

    @discord.ui.button(label="Rusça sohbet", style=ButtonStyle.grey)
    async def Rusça(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Rusça Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(
                f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

    @discord.ui.button(label="Almanca sohbet", style=ButtonStyle.grey)
    async def Almanca(self, interaction: Interaction, button: ui.Button):
        author = interaction.user
        role = get(author.guild.roles, name="Almanca Öğrenenler")
        if role in author.roles:
            await author.remove_roles(role)
            await interaction.response.send_message(
                f"{role} rolünü bıraktınız", ephemeral=True)
        else:
            author = interaction.user
            await author.add_roles(role)
            await interaction.response.send_message(f"{role} rolünü aldınız", ephemeral=True)

class buttons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(name="dilbuton", description="Kendi Change My Mind'ını oluşturur.")
    async def rolbtt(self, ctx):
        view = RolMenu()
        embed = Embed(
            title="Dillere göre sohbet rolleri",
            description="Aynı dili bilen insanlarla konuşma alıştırması yapabileceğiniz kanalları açar"
        )
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(buttons(bot))