import discord
import datetime
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

class checkrole(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.start_state = True
        self.nameDict= {}
        self.list_nick = []
        self.channel = 'nope'

    @commands.command()
    async def start(self, ctx):
        self.start_state = True

        member = ctx.author                          
        roles = [role for role in member.roles]
        check_role = False
        for role in roles:
            if role.name == 'student':
                check_role = True
        
        self.channel = discord.utils.get(member.guild.voice_channels, name=f"{member.voice.channel}")
        voice_channels_members = self.channel.members

        for member in voice_channels_members:
            self.nameDict[member.nick] = [datetime.datetime.utcnow()]

        await ctx.send(f'{self.nameDict} {self.channel.name}')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.start_state == True:
            print(self.nameDict)
            channel = discord.utils.get(member.guild.text_channels, name="on_voice_chat")
            if member.bot:
                return

            if not before.channel: #join
                if member.nick not in self.nameDict:
                    self.nameDict[member.nick] = [datetime.datetime.utcnow()]

            if before.channel and not after.channel: #leave
                if len(self.nameDict[member.nick]) == 1:
                    self.nameDict[member.nick].append(datetime.datetime.utcnow())
                else:
                    self.nameDict[member.nick][1] = datetime.datetime.utcnow()

            if before.channel and after.channel:
                if before.channel.id != after.channel.id :
                    mbed = discord.Embed(
                    colour = (discord.Colour.gold()),
                    title = 'User Reported',
                    description = f"{member.display_name} switched to {after.channel.name}"
                )
                    mbed.set_thumbnail(url=f"{member.avatar_url}")
                    mbed.set_author(name=f"{member.display_name}", icon_url=f"{member.avatar_url}")
                    mbed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                    mbed.timestamp = datetime.datetime.utcnow()
                    await channel.send(embed=mbed)

    @commands.command()
    async def stop(self, ctx):
        self.start_state = False

        member = ctx.author                          
        roles = [role for role in member.roles]
        check_role = False
        for role in roles:
            if role.name == 'student':
                check_role = True
        
        self.channel = discord.utils.get(member.guild.voice_channels, name=f"{member.voice.channel}")
        voice_channels_members = self.channel.members

        for member in voice_channels_members:
            self.nameDict[member.nick][1] = datetime.datetime.utcnow()

        await ctx.send(f'{self.nameDict} {self.channel.name}')
            
        
def setup(client):
    client.add_cog(checkrole(client))