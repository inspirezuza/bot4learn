import discord
from discord.ext import commands

class joinleave(commands.Cog):

        def __init__(self, client):
            self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print('Bot is online!')
            
        @commands.Cog.listener()
        async def on_member_join(self, member):
            print(f'{member} has joined a server!')

        @commands.Cog.listener()
        async def on_member_remove(self, member):
            print(f'{member} has left a server!')

        @commands.command()
        async def ping(self, ctx):
            await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(joinleave(client))