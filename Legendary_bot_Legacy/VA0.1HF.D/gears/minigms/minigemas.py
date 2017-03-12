#imports
import discord
from discord.ext import commands
import time
import datetime
import math
import asyncio
import random

class MG():
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(MG(bot))
