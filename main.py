import os
import threading
import time
import asyncio
import discord
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message: discord.Message):
    if bot.user == message.author:
        return

    executor.submit(on_message_task, message)


def on_message_task(message: discord.Message):
    async def task():
        print(f"{message.content} current_thread=" + threading.current_thread().name)
        async with message.channel.typing():
            time.sleep(5)

        await message.channel.send('Reply: ' + message.content)
    asyncio.run(task())
    # asyncio.run_coroutine_threadsafe(task(), asyncio.get_event_loop())



bot.run(os.getenv('DISCORD_BOT_TOKEN'))
