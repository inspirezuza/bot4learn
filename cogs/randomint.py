import discord
import random
import datetime
from discord.ext import commands
from datetime import timezone,tzinfo,timedelta

class randomint(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def random(self, ctx, num):
        mbed = discord.Embed(
                colour = (discord.Colour.gold()),
                title = f'Random number is {random.randint(1, int(num))}',
            )
        mbed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=mbed)

def setup(client):
    client.add_cog(randomint(client))