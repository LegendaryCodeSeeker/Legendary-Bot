#imports
import discord
from discord.ext import commands
import time
import math
import asyncio

class MG():
    def __init__(self, bot):
        self.bot = bot
    #Lottery
    #Lottery start 
    @commands.command(pass_context=True)
    async def lotto_start(self, ctx, lottotime:int):
        async def lotto_timer():
            await asyncio.sleep(lottotime)
            await print("Lotto is over, picking winner.")
        self.bot.loop.create_task(lotto_timer())

def setup(bot):
    bot.add_cog(MG(bot))
