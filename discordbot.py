import discord
import os
import datetime
import sys
import sqlite3

from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

client = commands.Bot(command_prefix='!') #กำหนด Prefix
client.remove_command('help')
print('loading')

@client.command()   
async def mail(ctx) :
    pass

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
                                                                                                  
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension) :
    client.load_extension(f'cogs.{extension}')
    print(f'load {extension}')

@client.command()   
@commands.has_permissions(administrator=True)
async def unload(ctx, extension) :
    client.unload_extension(f'cogs.{extension}')
    print(f'unload {extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def r(ctx, extension) :
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'reload {extension}')

for filename in os.listdir('./cogs'):
    if filename == 'gsheet.py':
        continue
    elif filename.endswith('.py'):    
            client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzM1MDkwMzY3NTYwNTQ4NDM0.XxbMQA.-SSCuZWL-ZrXW7N-0GWPvFHCVlU') 

# NzQ3MDI0NTUxODY2NjYyOTk1.X0I21A.xxK2DWyopQdPqpnsGTz9xzRQ6oA สำหรับบอทกาก
# NzM1MDkwMzY3NTYwNTQ4NDM0.XxbMQA.-SSCuZWL-ZrXW7N-0GWPvFHCVlU สำหรับของจริงa