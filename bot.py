from config import *

import subprocess
import time
import discord
from discord.ext import commands


description = '''A bot ran on Raspberry Pi'''
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
    bashCommand = "free | grep Mem | awk '{printf(\"...\\nFree memory: %.1f%%\\n\", $4/$2*100.0 ) }' && vcgencmd measure_temp | sed 's/temp=/Temperature:\ /g' && df -h | grep root | awk '{printf(\"Free disk space: %s\\n\", $4 ) }'"
#    bashCommand = """free |  grep Mem && vcgencmd measure_temp | sed 's/temp=/Temperature:\ /g' """
    output = subprocess.check_output(['bash','-c', bashCommand])
    await bot.say(output.decode("utf8"))


@bot.command()
async def picture():
    """Take a picture through rasbpi's camera"""
    bashCommand="fswebcam -r 640x480 --jpeg 85 -D 1 --save ./snap.jpg"
    output = subprocess.check_output(['bash','-c', bashCommand])
    time.sleep(1.5)
    await bot.upload("./snap.jpg")


@bot.command()
async def audio(seconds_rec: int=5):
    """records 5 seconds worth of audio from the pi's mic"""
    await bot.say("Recording...")
    try:
       seconds_rec=int(seconds_rec)
    except ValueError:
       await bot.say("Ti si tup trqbva mi chislo")
    bashCommand="arecord -f cd -D plughw:1,0 -d {} ./play.wav".format(seconds_rec)
    output = subprocess.check_output(['bash','-c', bashCommand])
    time.sleep(1)
    await bot.upload("./play.wav")

# @bot.command()
# async def hackme(command: str):
#   output= subprocess.check_output(['bash','-c',command])
#   await bot.say("\n".join(["```", output.decode("utf8"), "```"]))

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
   """get info on a user, usage - ?info @user (stolen from Da532)"""
   embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xff1493)
   embed.add_field(name="Name", value=user.name, inline=True)
   embed.add_field(name="ID", value=user.id, inline=True)
   embed.add_field(name="Status", value=user.status, inline=True)
   embed.add_field(name="Highest role", value=user.top_role)
   embed.add_field(name="Joined", value=user.joined_at)
   embed.set_thumbnail(url=user.avatar_url)
   await bot.say(embed=embed)


@bot.command()
async def plug():
   """shameless"""
   await bot.say("The source code of this discord bot is located at https://github.com/yamozha/discordpibot")
   await bot.say("Please follow me on twitter https://twitter.com/yamozhatcg for more of these projects")

@bot.command()
async def echo(usersaybot: str):
   await bot.say(usersaybot)

bot.run(TOKEN)
