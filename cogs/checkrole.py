import discord
import datetime
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

class checkrole(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def check(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        check_role = False
        for role in roles:
            if role.name == 'teacher':
                check_role = True

        channel = discord.utils.get(member.guild.voice_channels, name=f"{member.voice.channel}")
        
        await ctx.send(f'{check_role}, {channel.members}')
        
def setup(client):
    client.add_cog(checkrole(client))