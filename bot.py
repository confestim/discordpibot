from config import *

from random import randint
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
async def yoot():
     await bot.say("yeet")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    left=int(left)
    right=int(right)
    if ValueError:
        await bot.say("u dumb give me 2 numbers like this 'num1 num2'")
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
    takingpic = await bot.say("Taking picture")
    bashCommand="fswebcam -r 640x480 --jpeg 85 -D 1 --save ./snap.jpg"
    output = subprocess.check_output(['bash','-c', bashCommand])
    time.sleep(1.5)
    await bot.delete_message(takingpic)
    await bot.upload("./snap.jpg")


@bot.command()
async def audio(seconds_rec: int=5):
    """records () seconds worth of audio from the pi's mic"""
    await bot.say("Recording...")
    try:
       seconds_rec=int(seconds_rec)
    except ValueError:
       await bot.say("Ti si tup trqbva mi chislo")
    bashCommand="arecord -f cd -D plughw:1,0 -d {} ./play.wav".format(seconds_rec)
    output = subprocess.check_output(['bash','-c', bashCommand])
    time.sleep(1)
    await bot.upload("./play.wav")

#@bot.command()
#async def hackme(command: str):
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
   plug1 = await bot.say("The source code of this discord bot is located at https://github.com/yamozha/discordpibot")
   plug2 = await bot.say("Please follow me on twitter https://twitter.com/yamozhatcg for more of these projects")
   time.sleep(6)
   await bot.delete_messages((plug1,plug2))


@bot.command()
async def echo(usersaybot: str):
   await bot.say(usersaybot)


@bot.command(pass_context=True)
async def gambling(ctx, randomvar, regarir: int=3):
   """guess the number the bot is thinking of from 1-10"""
   import random
   regarir = int(regarir)
   randomvar = random.randrange(0,10,1)
   msg1 = await bot.say("The number I'm thinking of is {}".format(randomvar))
   time.sleep(1)
   if regarir == randomvar:
      msg2 = await bot.say("Well done, you guessed the number! :o :cake:")
   else:
      msg2 = await bot.say("You didnt guess it, better luck next time! :cry:")
   time.sleep(2)
   await bot.delete_messages((msg1,msg2))

@bot.command(pass_context = 1)
async def roles(context):
    ''' Displays all roles '''
    roles = context.message.server.roles
    result = 'The roles are '
    for role in roles:
        result += role.name + ': ' + role.id + ', '
    await bot.say(result) #check

@bot.listen()
async def on_message(message):
    if message.content == "pepe":
        await bot.send_message(message.channel, "https://i.guim.co.uk/img/media/327e46c3ab049358fad80575146be9e0e65686e7/0_0_1023_742/master/1023.jpg?w=1920&q=55&auto=format&usm=12&fit=max&s=ecc0b8c0c657bcc0fd231c0e35f89a39")

@bot.listen()
async def on_member_join(member):
    server = member.server
    layout = 'Welcome {0.mention} to {1.name}!'
    await bot.say(discord.Object(id = '''ENTER THE CHANNEL-ID HERE!!!'''), layout.format(member, server))
    for role in member.roles:
        await bot.change_nickname(member, '~/user/' + str(member))


@bot.command()
async def coins():
    """gets the price of monero, bitcoin and dogecoin"""
    import requests
    bitcoin = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/").json()
    monero = requests.get("https://api.coinmarketcap.com/v1/ticker/Monero/").json()
    dogecoin = requests.get("https://api.coinmarketcap.com/v1/ticker/dogecoin/").json()
    await bot.say('1 Bitcoin: {0:.2f}$'.format(float(bitcoin[0]["price_usd"])))
    await bot.say('1 Monero {0:.2f}$'.format(float(monero[0]["price_usd"])))
    await bot.say('1 DogeCoin: {0:.3f}$'.format(float(dogecoin[0]["price_usd"])))


@bot.listen()
async def on_message(message):
   if message.content == "nice meme":
       await bot.send_message(message.channel, "http://niceme.me/")


bot.run(TOKEN)
