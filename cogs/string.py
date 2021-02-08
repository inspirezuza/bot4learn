import discord
import random
import datetime
from discord.ext import commands
from datetime import timezone,tzinfo,timedelta

class string(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def attendance(self, ctx):
        mbed = discord.Embed(
                colour = (discord.Colour.green()),
                title = f'START CLASS' ,
                description = f'Checking attendance : :white_check_mark: \n Delay between attendance : `5 minute` \n Time to react : `2 minute` ',
            )
        # mbed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=mbed)

    @commands.command()
    async def finish(self, ctx):
        mbed = discord.Embed(
                colour = (discord.Colour.red()),
                title = f'FINISH CLASS' ,
                description = f'google sheet : https://docs.google.com/spreadsheets/d/1QsFYP5Xf_8PXgkcJOSVLde1hZ1xedOrNpB1MUfwopNY/edit#gid=0',
            )
        mbed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=mbed)

    @commands.command()
    async def clear(self, ctx, amount=5):
       await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(string(client))