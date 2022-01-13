import os
from threading import Thread
from replit import db
import json
import library
import pandas as pd
import neversleep
import discord
import youtube_dl
import file
from discord.ext import commands


############### RUBBISH ###############################################
neversleep.awake("https://capubot.marcocapusso.repl.co", True)
TOKEN = "ODg0ODc5Mjc2NTYwNzc3MjI3.YTe6Cw.60dze1UiGeygUnCiGtLGKqva2ck"
GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client()
bot = commands.Bot(command_prefix='-')



  ######################## CODE #######################################

## Initialize the DB
try:
  if db["leagues"]:
    pass
except:
  db["leagues"] = []

## Initialize the Players
try:
  if db["players"]:
    pass
except:
  db["players"] = []




  ############### EVENTS ###############################################

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}  

# voice_client = None

def endSong(guild, path):
    os.remove(path) 


# @bot.command(name="play")
# async def play(ctx, arg):
#     voiceChannel = ctx.author.voice.channel;
#     url = arg
#     if not ctx.author.voice:
#       await ctx.send("Se vuoi ascoltare la musica fa che ti metti in un canale vocale")
#     else:
#       channel = ctx.author.voice.channel
    
#     try:
#       voice_client = await channel.connect()
#       print(voice_client)
#     except:
#       voice_client = ctx

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         file = ydl.extract_info(url, download=True)
#         path = str(file['title']) + "-" + str(file['id'] + ".mp3")
#         await ctx.channel.send("Now Playing: " + file['title'])
#     guild = ctx.guild
    
#     voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
#     voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

#     await ctx.send("OK")                             

# @bot.event
# async def on_message(message):
#   if message.author == bot.user:
#       return
#   msg = message.content
#   # ctx = await client.get_context(message)
#   # print(ctx)
#   params = msg.split(" ")
#   roles = message.author.roles
#   # ctx = await message.get_context(message)
#   voiceChannel = message.author.voice.channel;
  
#   ## Show Personal Id
#   if params[0].lower() == "-p" or params[0].lower() == "-play":
#     url = params[1]
#     response = "Playing: " + str(params[1])
#     # await message.channel.send(response)
#     if not message.author.voice:
#         await message.channel.send("Se vuoi ascoltare la musica fa che ti metti in un canale vocale")
#         # await ctx.send('you are not connected to a voice channel')
#         return

#     else:
#         channel = message.author.voice.channel

#     try:
#       voice_client = await channel.connect()
#       print(voice_client)
#       print(message.author.voice)
#     except:
#       voice_client = message.author.voice

#     guild = message.guild

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         file = ydl.extract_info(url, download=True)
#         path = str(file['title']) + "-" + str(file['id'] + ".mp3")
#         await message.channel.send("Now Playing: " + file['title'])

#     voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
#     voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

#     # await message.channel.send("Music Playing")

# # while voice_client.is_playing():
# #         await asyncio.sleep(1)
#     # else:
#   # await voice_client.disconnect()
#   # print("Disconnected")

#   if params[0].lower() == "-leave" or params[0].lower() == "-l":
#     await voice_client.disconnect()
#     print("Disconnected")
#     await message.channel.send("Addio coglione")

#   if params[0].lower() == "-pause" or params[0].lower() == "-ps":
#     if voice_client.is_playing():
#       voice_client.pause()
#       await message.channel.send("Music has been paused")

#   if params[0].lower() == "-resume" or params[0].lower() == "-r":
#     if voice_client.is_paused():
#       voice_client.resume()
#       await message.channel.send("Music has been resumed")
  
#   if params[0].lower() == "-stop" or params[0].lower() == "-s":
#     if voice_client.is_playing():
#       voice_client.stop()
#       await message.channel.send("Music has been stopped")


# bot.run(TOKEN)
# bot.options.http.api = "https://discord.com/api"
file.setup(bot)