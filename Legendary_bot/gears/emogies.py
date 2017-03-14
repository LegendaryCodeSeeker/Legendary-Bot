#imports
import discord
from discord.ext import commands
import time
import datetime
import math
import asyncio
import random
import os

class emgs():
    def __init__(self, bot):
        self.bot = bot
    async def on_message(self, message):
        if 'grass' in message.content:
            print(os.getcwd())
            await self.bot.send_file(message.channel, "gears/res/grass.png")
def setup(bot):
    bot.add_cog(emgs(bot))

