import discord
import datetime
import asyncio
import random
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands, tasks
from itertools import cycle

from cogs.gsheet import *

class checkrole(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.sheet = gsheet()
        self.start_state = False
        self.nameDict= {}
        self.channel = 'nope'
        self.attendance_check = True
        self.attendance_loop = False

        self.luckymember = None
        self.luckymember_check = None

    async def attendance_timer(self, ctx):
        TIMER = 10
        TIME_LIMIT = 10
        time_use = 0

        modmail_channel = discord.utils.get(self.client.get_all_channels(), name="mod-mail")

        while self.attendance_loop:
            await asyncio.sleep(10)
            print(self.channel.members)
            print(f'TIME_LIMIT {TIME_LIMIT}')
            member = random.choice(self.channel.members)
            self.luckymember = member

            channel = await member.create_dm()

            await channel.send('click reaction to check you still active')

            while True:
                print(F"time_use {time_use}")
                print(f'{self.luckymember_check}')
                if self.luckymember_check == True:
                    await channel.send(f'success you use {time_use} to reaction')
                    self.luckymember_check = False
                    break
                elif time_use > TIME_LIMIT:
                    await channel.send('you not reaction in time send infomation to teacher')
                    await modmail_channel.send(f'{member} not reaction in time : {TIME_LIMIT}')
                    break
                time_use += 1

                await asyncio.sleep(1) #ทุกๆ 1 วินาที

            time_use = 0
            await asyncio.sleep(TIMER)
        await ctx.send('End')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        #lucky member
        if str(message.channel.type) == "private" and self.luckymember == message.author:
            print('hello')
            self.luckymember_check = True

    @commands.command()
    async def start(self, ctx):
        self.start_state = True

        member = ctx.author                          
        # roles = [role for role in member.roles]
        # for role in roles:
        #     if role.name == 'teacher':
        #         pass
        try:
            self.channel = discord.utils.get(member.guild.voice_channels, name=f"{member.voice.channel}")
        except AttributeError:
            await ctx.send('No one in voice channel')

        self.channel = discord.utils.get(member.guild.voice_channels, name=f"{member.voice.channel}")
        voice_channels_members = self.channel.members

        for member in voice_channels_members:
            self.nameDict[member.nick] = [datetime.datetime.utcnow()]

        await ctx.send(f'{self.nameDict} {self.channel.name}')
        if self.attendance_check == True:
            self.attendance_loop = True
            self.client.loop.create_task(self.attendance_timer(ctx))
            print('attendance working')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.start_state == True:
            
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

        if self.start_state == True:
            print(self.nameDict)

    @commands.command()
    async def stop(self, ctx):
        self.start_state = False

        if self.attendance_check == True:
            self.attendance_loop = False
            print('stop')


        member = ctx.author                          
        # roles = [role for role in member.roles]
        # check_role = False
        # for role in roles:
        #     if role.name == 'student':
        #         check_role = True
        
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
        #     print('Error: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS,FIELDS-1)

def setup(client):
    client.add_cog(checkrole(client))