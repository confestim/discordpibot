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
async def installpre():
    """Installs the prerequisites needed for this bot to run"""
    import subprocess
    await bot.say("Installing prerequisites")
    bashCommand = "sudo apt-get install alsa-utils;sudo apt-get install fswebcam"
    output = subprocess.check_output(['bash','-c', bashCommand])
    await bot.say("Install Completed")


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
    bashCommand="fswebcam -r 640x480 --jpeg 85 -D 1 --save /home/pi/Yourpathhere/snap.jpg"
    output = subprocess.check_output(['bash','-c', bashCommand])
    time.sleep(1.5)
    await bot.upload("/home/pi/Yourpathhere/snap.jpg")


@bot.command()
async def audio():
    """records 5 seconds worth of audio from the pi's mic"""
    import time
    import subprocess
    await bot.say("Recording...")
    bashCommand="arecord -f cd -D plughw:1,0 -d 5 /home/pi/Yourpathhere/play.wav"
    output = subprocess.check_output(['bash','-c', bashCommand])
    time.sleep(1)
    await bot.upload("/home/pi/Yourpathhere/play.wav")


@bot.command()
async def openfile():
   """this is a seemingly useless command that is made for pentesting of the bot"""
   await bot.say("this command is still work in progress")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
   """get info on a user, usage - ?info @user (i shamelessly stole this from Da532)"""
   embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
   embed.add_field(name="Name", value=user.name, inline=True)
   embed.add_field(name="ID", value=user.id, inline=True)
   embed.add_field(name="Status", value=user.status, inline=True)
   embed.add_field(name="Highest role", value=user.top_role)
   embed.add_field(name="Joined", value=user.joined_at)
   embed.set_thumbnail(url=user.avatar_url)
   await bot.say(embed=embed)

bot.run(TOKEN)

