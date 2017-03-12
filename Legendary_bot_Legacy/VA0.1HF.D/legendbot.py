#Legendary Bot V0.2(Alpha)[HF.A] @23:07:00 3/6/17

#Imports
from discord.ext import commands
import discord
import datetime

#Autoloading Items
auto_load = ["gears.sraeg","gears.minigms.minigemas","gears.tstcmds","gears.minigms.lottery","gears.Legends"]

#Main
bot = commands.Bot(command_prefix='||', description="Testing")

#Bot Awaiting Orders
@bot.event
async def on_ready():
    print('The Legend Begins.')
    print('The Legend is about {} with the knowlegd of the scroll called {}'.format(bot.user.name, bot.user.id))
    print('-_-_-_-_-_-_-_-_-_-_-')
    await bot.change_presence(game=discord.Game(name="TattleTaiil"))
    bot.st = datetime.datetime.now()


#Load Extension Command
@bot.command
async def loadExt(extName : str):
    #loading an Extension
    try:
        bot.load_extension(extName)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} Has arrived..".format(extName))

#Unload Extension Command
@bot.command
async def unloadExt(extName : str):
    #Unloading an Extension
    bot.unload_extsion(extName)
    await bot.say("{} Has left.".format(extName))

# Reload extension command
@bot.command()
async def reloadExt(extName : str):
    # Reloads an extension.
    try:
        tmp = await bot.say("Reloading extension {}".format(extName))
        bot.unload_extension(extName)
        bot.load_extension(extName)
        await bot.edit_message(tmp, "Reloaded extension {}!".format(extName))
    except Exception as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))

# Reload startup command
@bot.command()
async def reloadBot():
    for extension in start_up:
        bot.unload_extension(extension)
        try:
            bot.load_extension(extension)
            await bot.say("Reloaded {}!".format(str(extension)))
        except Exception as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))

#Setting up bot

if __name__ == "__main__":
    for extension in auto_load:
        try:
            bot.load_extension(extension)
            print("{} Has arrived.".format(extension))
        except Exception as e:
            print("{}: {}".format(type(e).__name__, e))



bot.run("Mjg4MzIxMTg4MTA1NTUxODcy.C6aA_w.ndPyCdI0GZjpjQr9EBgOnFMC1J0")
