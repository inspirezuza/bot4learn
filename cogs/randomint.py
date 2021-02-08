import discord
import random
import datetime
from discord.ext import commands
from datetime import timezone,tzinfo,timedelta

class randomint(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def random(self, ctx, *num):
        print(num)
        if len(num) == 1:
            mbed = discord.Embed(
                    colour = (discord.Colour.gold()),
                    title = f'Random number is {random.randint(1, int(num[0]))}',
                )
            mbed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=mbed)
        elif len(num) == 2:
            mbed = discord.Embed(
                    colour = (discord.Colour.gold()),
                    title = f'Random number is {random.randint(int(num[0]), int(num[1]) )  }',
                    )
            mbed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=mbed)

def setup(client):
    client.add_cog(randomint(client))