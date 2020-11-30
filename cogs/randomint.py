import discord
import random
from discord.ext import commands

class randomint(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def random(self, ctx, num):
        await ctx.send(f'Random number is {random.randint(1, int(num))}')

def setup(client):
    client.add_cog(randomint(client))