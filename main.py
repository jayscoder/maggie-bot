import os
import time
import asyncio
import discord

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message: discord.Message):
    if bot.user == message.author:
        return
    await async_on_message(message)

async def async_on_message(message: discord.Message):
    with message.channel.typing():
        time.sleep(5)

    await message.channel.send('Reply: ' + message.content)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))

