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

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    mbed = discord.Embed(colour=member.color)
    mbed.timestamp = datetime.datetime.utcnow()
    mbed.set_author(name=f"User Info - {member}")
    mbed.set_thumbnail(url=member.avatar_url)
    mbed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    mbed.add_field(name="ID:", value=member.id)
    mbed.add_field(name="Guild name:", value=member.display_name)

    mbed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"))
    mbed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))

    mbed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    mbed.add_field(name="Top role:", value=member.top_role.mention)

    mbed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=mbed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzM1MDkwMzY3NTYwNTQ4NDM0.XxbO8Q.mkZy-MDB9crKcUYat4kNmehX5Ks') 