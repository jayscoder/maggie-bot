import os
import time
import asyncio
import discord

bot = discord.Client(intents=discord.Intents.all())

def coroutine():
    value = yield
    index = 0
    while True:
        value = yield f'收到-{index}: {value}'
        index += 1


coro = coroutine()

async def on_ready(self):
    print(f'{self.user} has connected to Discord!')

async def on_message(self, message: discord.Message):
    if self.user == message.author:
        return
    coro.send(message.content)
    await message.channel.send(next(coro))


bot.run(os.getenv('DISCORD_BOT_TOKEN'))

