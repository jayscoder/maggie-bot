import os
import discord
import constantly
from enum import Flag, auto
import re
from discord.ext import commands

DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
