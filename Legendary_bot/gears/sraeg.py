# Basic Command Gears

# Imports
import discord
from discord.ext import commands
import datetime
import time
import platform
import os
import math

class general_cmds():
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
    
    # Test command, tests the bot to see if it's active.
    @commands.command(pass_context=True)
    async def test(self, ctx):
        await self.bot.say('It works, {0.message.author.mention}!'.format(ctx))
        await self.bot.delete_message(ctx.message)
    
    # About command, tells basic info about the bot.
    @commands.command(pass_context=True)
    async def about(self, ctx):
        # Create about embed
        about = discord.Embed(color=discord.Colour.teal())
        about.add_field(name="W.I.P.", value="Not finished, nothing is fully done, buggy.")
        about.add_field(name="test", value="test1")
        about.set_author(name="", icon_url=self.bot.user.avatar_url)
        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=about)
    
    # Help command, tells the commands of the bot in a DM.
    @commands.command(name="help", pass_context=True)
    async def helpcmd(self, ctx):
        # Create help embed
        embed = discord.Embed(colour=discord.Colour(0x9c9b4f))
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text="Legendary Bot V0.1 Alpha HF.B")
        embed.add_field(name="General Commands", value="||test - Tests the bot to make sure it's working\n||help - Gives commands in DM\n||about - Tells you about the bot.\n||lotto_help - for info on how to lottery")
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.author, embed=embed)     
    #bot last boot & ping
    @commands.command(pass_context=True)
    async def status(self, ctx):
        before = time.time()
        await (await self.bot.ws.ping())
        after = time.time()
        delta = after - before

        embed = discord.Embed(title="Bot Status", colour=discord.Colour(0x3b6353), timestamp=datetime.datetime.utcnow())
        
        embed.set_footer(text=platform.system() + " " + platform.release())
        
        embed.add_field(name="Ping", value=str(math.ceil(delta*1000)) + " ms")
        embed.add_field(name="Started at", value=str(self.bot.st).split('.')[0])

        await self.bot.say(embed=embed)        

def setup(bot):
    bot.add_cog(general_cmds(bot))
