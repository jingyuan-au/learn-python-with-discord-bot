import discord
from discord.ext import commands
        
bot = commands.Bot('-')

@bot.event
async def on_ready():
    print('---Bot is online!---')

token = ''
bot.run(token)