import discord
import random
import datetime
from discord.ext import commands
from datetime import timezone,tzinfo,timedelta

class string(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        mbed = discord.Embed(
                colour = (discord.Colour.red()),
                description = f'Clear {amount} messages',
            )
        await ctx.send(embed=mbed)

def setup(client):
    client.add_cog(string(client))