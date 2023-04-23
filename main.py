import os
import threading
import time
import asyncio
import discord
import threads

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message: discord.Message):
    if bot.user == message.author:
        return
    # 每个用户在每个频道一个单独的线程
    loop = threads.new_thread_loop(name=f'{message.channel.id}/{message.author.id}')
    asyncio.run_coroutine_threadsafe(on_message_task(message), loop=loop)


async def on_message_task(message: discord.Message):
    print(f"{message.content} current_thread=" + threading.current_thread().name)
    async with message.channel.typing():
        time.sleep(3)
    await message.channel.send('Reply: ' + message.content)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
