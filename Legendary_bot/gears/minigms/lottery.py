#imports
import discord
from discord.ext import commands
import time
import datetime
import math
import asyncio
import random

lottoOn = False

class LTry():
    def __init__(self, bot):
        self.bot = bot

    #Lottery
    #Lottery start
    @commands.command(pass_context=True)
    async def lotto_start(self, ctx, lottotime:int, lottodrops:int):
        if lottoOn == True:
            await self.bot.send_message(ctx.message.channel, 'Sorry but theres a lottery already going on.\n Do ||lotto for more info')
        else:
            if lottotime < 180 or lottotime > 10800:
                 await self.bot.send_message(ctx.message.channel, 'Lottery must last 3 mins or longer, but no longer than 3hrs.')
            else:
                if lottodrops < 50:
                    await self.bot.send_message(ctx.message.channel, 'You must start a Lottery With 50 or more Tea Drops in the pot.')
                else:
                    async def lotto_timer():
                        starttime = datetime.datetime.now()
                        lottoOn = True
                        hlf = lottotime / 2
                        frth = lottotime / 4
                        ggt = str(hlf)
                        hjk = str(frth)
                        await self.bot.send_message(ctx.message.channel, "Attention @everyone a Lottery is starting with {} Tea Drops in the pot for {} seconds".format(lottodrops, lottotime))
                        await asyncio.sleep(lottotime/2)
                        await self.bot.send_message(ctx.message.channel, "@everyone Lottery has {} seconds left".format(ggt))
                        await asyncio.sleep(lottotime/4)
                        await self.bot.send_message(ctx.message.channel, "@everyone Lottery has {} seconds left".format(hjk))
                        await asyncio.sleep(lottotime/4)
                        await self.bot.send_message(ctx.message.channel, '@everyone The lottery is finished, the winning numbers belong too...')
                        await asyncio.sleep(random.randrange(4))
                        await self.bot.send_message(ctx.message.channel, '@everyone Nobody, sorry try again netx time')
                        lottoOn = False
                    self.bot.loop.create_task(lotto_timer())

def setup(bot):
    bot.add_cog(LTry(bot))
