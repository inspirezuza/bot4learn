import discord
import random
import datetime
from discord.ext import commands
from datetime import timezone,tzinfo,timedelta

class string(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()   
    async def help(self, ctx) :
        mbed = discord.Embed(
                colour = (discord.Colour.darker_gray()),
                title = f'Bot for helping online learning Help',
                description = '`!attendance`\n'
                'เริ่มจับเวลาการเข้าเรียน\n'
                "\n"
                '`!clear`\n'
                'ลบข้อความเก่า\n'
                "\n"
                '`!finish`\n'
                'จบการจับเวลาการเข้าเรียน\n'
                "\n"
                '`!poll`\n'
                'ตั้งโพลคำถามใช้ในการโหวต\n'
                "\n"
                '`!random`\n'
                'สุ่มเลข\n'
                "\n"
                            
            )
        await ctx.send(embed=mbed)

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