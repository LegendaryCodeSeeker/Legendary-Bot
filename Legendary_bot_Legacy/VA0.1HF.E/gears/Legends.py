
#imports
import discord
from discord.ext import commands
import time
import datetime
import math
import asyncio

class LG():
    def __init__(self, bot):
        self.bot = bot
    #Starting a Legend
    @commands.command(pass_context=True)
    async def start_legend(self, ctx, To_d:str, Ob_j:str, leg_name:str, pergen:str, yr:str, temp:str, place:str):
        verbs = ['verb', 'verb1', 'verb2', 'verb3']
        ADverbs = ['adverb', 'adverb1', 'adverb2', 'adverb3']
        nouns = ['noun', 'noun1', 'noun2', 'noun3']
        PROnouns = ['pronoun', 'pronoun1', 'pronoun2', 'pronoun3']
        adjectives = []
        prepostitions = []
        conjunctions = []
        dterminers = []
        exclamation = []
        
def setup(bot):
    bot.add_cog(LG(bot))

