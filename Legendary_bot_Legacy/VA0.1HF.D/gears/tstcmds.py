# Imports
import discord
from discord.ext import commands
import datetime
import time
import platform
import os
import math

class TST():
    def __init__(self, bot):
        self.bot = bot

    # Test command, tests the bot to see if it's active.
    @commands.command(pass_context=True)
    async def test(self, ctx):
        await self.bot.say('It works, {0.message.author.mention}!'.format(ctx))
        await self.bot.delete_message(ctx.message)

    #bot gamble test
    @commands.command(pass_context=True)
    async def bgtst(self, ctx, amtofdrps:int):
        await self.bot.say('/coinflip {}'.format(amtofdrps))
        await self.bot.delete_message(ctx.message)

    #bot donate test
    @commands.command(pass_context=True)
    async def bdtst(self, ctx, too, amtfdrops:int):
        await self.bot.say('/donate {} {}'.format(too, amtfdrops))
        await self.bot.delete_message(ctx.message)
def setup(bot):
    bot.add_cog(TST(bot))

