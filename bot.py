from config import *

import discord
from discord.ext import commands


description = '''rasbpi status'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello():
     await bot.say("yeet")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    if not left or not right:
        await bot.say("give me two ints to add")
    await bot.say(left + right)


@bot.command()
async def status():
    import subprocess
    bashCommand = "/opt/vc/bin/vcgencmd measure_temp"
    output = subprocess.check_output(['bash','-c', bashCommand])
    await bot.say(output.decode("utf8"))



bot.run(TOKEN)
