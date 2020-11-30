import discord
import os
import datetime
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

client = commands.Bot(command_prefix='.') #กำหนด Prefix

                                                                                                          
@client.command()
async def load(ctx, extension) :
    client.load_extension(f'cogs.{extension}')
    print(f'load {extension}')

@client.command()
async def unload(ctx, extension) :
    client.unload_extension(f'cogs.{extension}')
    print(f'unload {extension}')

@client.command()
async def reload(ctx, extension) :
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'reload {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzQ3MDI0NTUxODY2NjYyOTk1.X0I21A.Ce21eLpat5wZAbuW5B3Vla-zUEs') 