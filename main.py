import os
import time
import asyncio
import discord

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message: discord.Message):
        if self.user == message.author:
            return
        for i in range(5):
            await asyncio.sleep(3)
            await message.channel.send(f'{message.content}: {i}')

bot = CustomClient(intents=discord.Intents.all())
bot.run(os.getenv('DISCORD_BOT_TOKEN'))

