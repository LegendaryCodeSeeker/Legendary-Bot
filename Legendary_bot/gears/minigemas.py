#imports
import discord
from discord.ext import commands
import time
import datetime
import math
import asyncio
#import sqlite3

class MG():
    def __init__(self, bot):
        self.bot = bot
    #Lottery
    #Lottery start 
    @commands.command(pass_context=True)
    async def lotto_start(self, ctx, lottotime:int, lottodrops:int):
        if lottotime < 300:
             await self.bot.send_message(ctx.message.channel, 'Lottery must last 5 mins or longer')
        else:
            async def lotto_timer():
                starttime = datetime.datetime.now()
                lottoOn = True
                await asyncio.sleep(lottotime)
                lottoOn = False
                await self.bot.send_message(ctx.message.channel, 'The lottery is finished, the winning numbers belong too...')
            self.bot.loop.create_task(lotto_timer())

def setup(bot):
    bot.add_cog(MG(bot))
