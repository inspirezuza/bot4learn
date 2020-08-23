import discord
import datetime
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

class joinleave(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online!')
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="join-leave")
        mbed = discord.Embed(
            colour = (discord.Colour.magenta()),
            title = 'Welcome massage',
            description = f"Welcome {member}, enjoy your stay!"
        )
        mbed.set_thumbnail(url=f"{member.avatar_url}")
        mbed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        mbed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        mbed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=mbed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="join-leave")
        mbed = discord.Embed(
            colour = (discord.Colour.magenta()),
            title = 'Goodbye massage',
            description = f"Goodbye {member}, Don't comeback!"
        )
        await channel.send(embed=mbed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(joinleave(client))