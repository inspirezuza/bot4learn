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

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 782987819534123089:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'getrole':
            role = discord.utils.get(guild.roles, name="testrolereac")
        else:
            print('need more')
        
        #if role is not None:
         #   member = discord.utils.find(la)

for filename in os.listdir('./cogs'):
    print(filename)
    if filename == 'gsheet.py':
        continue
    elif filename.endswith('.py'):    
            client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzM1MDkwMzY3NTYwNTQ4NDM0.XxbMQA.Ich_4dxZEosUFgQzcoNdxPj0hr4') 