import discord
import datetime
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

from cogs.gsheet import *

class checkrole(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.sheet = gsheet()
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

            # if before.channel and after.channel:
            #     if before.channel.id != after.channel.id :
            #         mbed = discord.Embed(
            #         colour = (discord.Colour.gold()),
            #         title = 'User Reported',
            #         description = f"{member.display_name} switched to {after.channel.name}"
            #     )
            #         mbed.set_thumbnail(url=f"{member.avatar_url}")
            #         mbed.set_author(name=f"{member.display_name}", icon_url=f"{member.avatar_url}")
            #         mbed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
            #         mbed.timestamp = datetime.datetime.utcnow()
            #         await channel.send(embed=mbed)

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

        # self.nameDict = {'Faith': [datetime.datetime(2020, 12, 7, 15, 21, 31, 199880), datetime.datetime(2020, 12, 7, 15, 21, 35, 335197)]
        #     ,'Haift': [datetime.datetime(2020, 12, 7, 15, 21, 31, 199880), datetime.datetime(2020, 12, 7, 15, 21, 35, 335197)]
        #     }

        SPREADSHEET_ID = '1QsFYP5Xf_8PXgkcJOSVLde1hZ1xedOrNpB1MUfwopNY' # Add ID here
        RANGE_NAME = 'A1'
        FIELDS = 2 # Amount of fields/cells

        # Code
        for key in self.nameDict: 
            result = [str(e) for e in self.nameDict[key]]
            if len(result) == FIELDS:
                # Add
                DATA = [key] + [123] + [456] + result
                self.sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
                print('Your data has been successfully submitted!')
            else:
                # Needs more/less fields
                print('Error: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS,FIELDS-1))
        # if len(result) == FIELDS:
        #     # Add
        #     print(message.created_at)
        #     DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + result
        #     sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
        #     print('Your data has been successfully submitted!')
        # else:
        #     # Needs more/less fields
        #     print('Error: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS,FIELDS-1))
            
        
def setup(client):
    client.add_cog(checkrole(client))