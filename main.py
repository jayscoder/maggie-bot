import os
import discord
import constantly
from enum import Flag, auto
import re
from discord.ext import commands
import discord
from discord_slash import SlashCommand, SlashContext
slash = SlashCommand(bot, sync_commands=True)

DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# 定义bot登陆事件
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    for guild in bot.guilds:
        for channel in guild.text_channels:
            # if channel.name == '欢迎光临！':
            # await channel.send('我上线啦')
            print(channel)


@bot.command("")

# 定义bot接受到消息的事件
@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    print(message.content)
    await message.channel.send(f"收到: {message.content}")


@slash.slash(name="hello", description="Says hello to the user")
async def hello(ctx: SlashContext):
    await ctx.send(f"Hello {ctx.author.mention}!")

bot.run(DISCORD_BOT_TOKEN)
