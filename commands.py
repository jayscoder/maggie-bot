import os
import discord
from discord import app_commands

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
intents = discord.Intents.all()

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


@tree.command(name="test", description="My first application Command")
async def first_command(interaction):
    await interaction.response.send_message("Hello!")


@bot.event
async def on_ready():
    await tree.sync()
    print("Ready!")


bot.run(DISCORD_BOT_TOKEN)

