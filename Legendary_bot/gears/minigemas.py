#imports
import discord
from discord.ext import commands
import time
import datetime
import math
import asyncio
import sqlite3

class MG():
    def __init__(self, bot):
        self.bot = bot
        lottoOn = False
    #Lottery
    #Lottery start 
    @commands.command(pass_context=True)
    async def lotto_start(self, ctx, lottotime:int, lottodrops:int):
        if lottoOn == True:
            await self.bot.send_message(ctx.message.channel, 'Sorry but theres a lottery already going on.\n Do `||lotto` for more info')
        else:
            if lottotime < 300:
                 await self.bot.send_message(ctx.message.channel, 'Lottery must last 5 mins or longer')
            else:
                if lottodrops < 50:
                    await self.bot.send_message(ctx.message.channel, 'You must start a Lottery With 50 or more Tea Drops in the pot.')
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
