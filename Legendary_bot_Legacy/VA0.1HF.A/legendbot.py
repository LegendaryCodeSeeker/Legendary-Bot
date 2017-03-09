#Legendary B__҉_t V0.1(Alpha)[HF.A] @23:07:00 3/6/17

#Imports
from discord.ext import commands

#Autoloading Items
auto_load = ["gears.sraeg"]

#Main
bot = commands.Bot(command_prefix='||', description="Testing")

#Bot Awaiting Orders
@bot.event
async def on_ready():
    print('The Legend Begins.')
    print('The Legend is about {} with the knowlegd of the scroll called {}'.format(bot.user.name, bot.user.id))
    print('-_-_-_-_-_-_-_-_-_-_-')



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

#Setting up bot

if __name__ == "__main__":
    for extension in auto_load:
        try:
            bot.load_extension(extension)
            print("{} Has arrived.".format(extension))
        except Exception as e:
            print("{}: {}".format(type(e).__name__, e))



bot.run("Mjg4MzIxMTg4MTA1NTUxODcy.C5-OlA.mPmws1SbAjRGzN-fKLo45yrSn6s")
