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
async def yoot():
     await bot.say("yeet")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    if not left or not right:
        await bot.say("give me two ints to add")
    await bot.say(left + right)


@bot.command()
async def status():
    """Show some system info"""
    import subprocess
    bashCommand = "free | grep Mem | awk '{printf(\"...\\nFree memory: %.1f%%\\n\", $4/$2*100.0 ) }' && vcgencmd measure_temp | sed 's/temp=/Temperature:\ /g' && df -h | grep root | awk '{printf(\"Free disk space: %s\\n\", $4 ) }'"
#    bashCommand = """free |  grep Mem && vcgencmd measure_temp | sed 's/temp=/Temperature:\ /g' """
    output = subprocess.check_output(['bash','-c', bashCommand])
    await bot.say(output.decode("utf8"))


@bot.command()
async def picture():
	"""Take a picture through rasbpi's camera"""
	import time
	import subprocess
	bashCommand="fswebcam -r 640x480 --jpeg 85 -D 1 --save /home/pi/Projects/discordbot/pic.jpg"
	output = subprocess.check_output(['bash','-c', bashCommand])
	time.sleep(1.5)
	await bot.upload("/home/pi/Projects/discordbot/pic.jpg")


bot.run(TOKEN)

