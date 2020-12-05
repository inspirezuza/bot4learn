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
            if role.name == 'student':
                check_role = True

        list_nick = []
        
        channel = discord.utils.get(member.guild.voice_channels, name=f"{member.voice.channel}")
        voice_channels_members = channel.members

        for student in voice_channels_members:
            list_nick.append(student.nick)

        await ctx.send(f'{check_role}, {list_nick}')
        
def setup(client):
    client.add_cog(checkrole(client))