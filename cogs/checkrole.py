import discord
import asyncio
import random
import pytz
from datetime import timezone,tzinfo,timedelta,datetime
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
        self.attendance_check = False
        self.attendance_loop = False

        self.TIMER = 180
        self.TIME_LIMIT = 120
        self.luckymember = None
        self.luckymember_check = None

    @commands.command()
    async def check(self, ctx):
        if self.attendance_check == False:
            self.attendance_check = True
            mbed = discord.Embed(
                    colour = (discord.Colour.green()),
                    title = f'Turn ON attendance check',
                )
            await ctx.send(embed=mbed)

        elif self.attendance_check == True:
            self.attendance_check = False
            mbed = discord.Embed(
                    colour = (discord.Colour.red()),
                    title = f'Turn OFF attendance check',
                )
            await ctx.send(embed=mbed)

    async def attendance_timer(self, ctx):
        await asyncio.sleep(120)
        time_use = 0

        modmail_channel = discord.utils.get(self.client.get_all_channels(), name="mod-mail")

        while self.attendance_loop:
            print(self.channel.members)
            print(f'self.TIME_LIMIT {self.TIME_LIMIT}')
            member = random.choice(self.channel.members)
            self.luckymember = member

            channel = await member.create_dm()

            await channel.send('type anything to check you still active')

            while True:
                print(F"time_use {time_use}")
                print(f'{self.luckymember_check}')
                if self.luckymember_check == True:
                    await channel.send(f'success you use {time_use} seconds to reaction')
                    self.luckymember_check = False
                    break
                elif time_use > self.TIME_LIMIT:
                    await channel.send('you not reaction in time send infomation to teacher')
                    await modmail_channel.send(f'{member.nick} not reaction in time : {self.TIME_LIMIT} seconds')
                    break
                time_use += 1

                await asyncio.sleep(1) #ทุกๆ 1 วินาที

            time_use = 0
            await asyncio.sleep(self.TIMER)
        await ctx.send('End')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        #lucky member
        if str(message.channel.type) == "private" and self.luckymember == message.author:
            self.luckymember_check = True

    @commands.command()
    async def attendance(self, ctx, starttime = '0'):
        if starttime != '0':
            await ctx.send(f'class will start in {starttime} (24-hour clock)')
            while str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16] !=  starttime:
                await asyncio.sleep(1)

        self.start_state = True

        member = ctx.author                          
        try:
            self.channel = discord.utils.get(member.guild.voice_channels, name=f"{member.voice.channel}")
        except AttributeError:
            mbed = discord.Embed(
                    colour = (discord.Colour.red()),
                    description = f'`No one in voice channel',
                )
            await ctx.send(embed=mbed)

        self.channel = discord.utils.get(member.guild.voice_channels, name=f"{member.voice.channel}")
        voice_channels_members = self.channel.members

        for member in voice_channels_members:
            if member.nick == None:
                self.nameDict[str(member)[:-5]] = [str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16]]
            else:
                self.nameDict[member.nick] = [str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16]]
        
        if self.attendance_check == True:
            check_icon = ':white_check_mark:'
        else:
            check_icon = ':negative_squared_cross_mark:'

        mbed = discord.Embed(
                colour = (discord.Colour.green()),
                title = f'START CLASS',
                description = f'Checking attendance: {check_icon}\nDelay between attendance : `{self.TIME_LIMIT + self.TIMER} second`\nTime to react : `{self.TIME_LIMIT} second`'
            )
        await ctx.send(embed=mbed)
        if self.attendance_check == True:
            self.attendance_loop = True
            self.client.loop.create_task(self.attendance_timer(ctx))
            print('attendance working')

        print(self.nameDict)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.start_state == True:
            
            if member.bot:
                return

            if not before.channel: #join
                if member.nick not in self.nameDict:
                    self.nameDict[member.nick] = [str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16]]

            if before.channel and not after.channel: #leave
                if len(self.nameDict[member.nick]) == 1:
                    self.nameDict[member.nick].append(str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16])
                else:
                    self.nameDict[member.nick][1] = str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16]

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
            #         mbed.timestamp = str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16]
            #         await channel.send(embed=mbed)

        if self.start_state == True:
            print(self.nameDict)

    @commands.command()
    async def finish(self, ctx):
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
            if len(self.nameDict[member.nick]) == 1:
                    self.nameDict[member.nick].append(str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16])
            else:
                self.nameDict[member.nick][1] = str(datetime.now(pytz.timezone("Asia/Bangkok")))[11:16]
        dateftime =  str(datetime.now(pytz.timezone("Asia/Bangkok")))[0:16]
        SPREADSHEET_ID = str(self.sheet.create(dateftime)) # Add ID here
        RANGE_NAME = 'A1'
        FIELDS = 1 # Amount of fields/cells

        for key in self.nameDict: 
            result = [f'{self.nameDict[key][0]} - {self.nameDict[key][1]}']
            if len(result) == FIELDS:
                # Add
                teachertime = result

                if key[0:3] == 'ครู':
                    DATA = [key[0:3]] + [key[4:].split()[0]] + [key[4:].split()[1]] + ['ตรงเวลา'] + result
                    self.sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
                    print('hello mother fucker')
                    break
                
        # Code
        for key in self.nameDict: 
            result = [f'{self.nameDict[key][0]} - {self.nameDict[key][1]}']
            if len(result) == FIELDS:
                # Add

                if key[0:3] != 'ครู':
                    print('mother fucky')
                    if result == teachertime:
                        DATA = [key[0:2]] + [key[3:].split()[0]] + [key[3:].split()[1]] + ['ตรงเวลา'] + result
                        self.sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)

                    else:
                        DATA = [key[0:2]] + [key[3:].split()[0]] + [key[3:].split()[1]] + ['สาย'] + result
                        self.sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)

                
                print('Your data has been successfully submitted!')

            else:
                # Needs more/less fields
                print('Error: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS,FIELDS-1))
 
        mbed = discord.Embed(
            colour = (discord.Colour.green()),
            title = f'FINISH CLASS',
            description = f'google sheet:https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit#gid=0'      
            )
        await ctx.send(embed=mbed)

        self.nameDict = {}

def setup(client):
    client.add_cog(checkrole(client))