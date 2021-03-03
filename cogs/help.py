import discord
import random
import datetime
from discord.ext import commands
from datetime import timezone,tzinfo,timedelta

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help (self, ctx):
        mbed = discord.Embed(title = "Help", description = "ใช้ !help <command> สำหรับข้อมูลเพิ่มเติมเกี่ยวกับคำสั่ง.", color = ctx.author.color)

        mbed.add_field(name = "All commands", value = '`!attendance`\n'
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
                "\n")

        await ctx.send(embed = mbed)

    @help.command()
    async def attendance(self, ctx):
        mbed = discord.Embed(title = "attendance", description = "เริ่มจับเวลาการเข้าเรียน", color = ctx.author.color)
        mbed.add_field(name = "**Syntax**", value = "!attendace <hr:mn> #ถ้าไม่ระบุเวลาจะเริ่มจับเวลาทันที")
        await ctx.send(embed = mbed)

    @help.command()
    async def clear(self, ctx):
        mbed = discord.Embed(title = "clear", description = "ลบข้อความเก่า", color = ctx.author.color)
        mbed.add_field(name = "**Syntax**", value = "!clear <amount> #ค่ามาตรฐานคือ 5")
        await ctx.send(embed = mbed)
    
    @help.command()
    async def finish(self, ctx):
        mbed = discord.Embed(title = "finish", description = "จบการจับเวลาการเข้าเรียน", color = ctx.author.color)
        mbed.add_field(name = "**Syntax**", value = "!finish #เก็บข้อมูลลงใน Google sheet" )
        await ctx.send(embed = mbed)

    @help.command()
    async def poll(self, ctx):
        mbed = discord.Embed(title = "poll", description = "ตั้งโพลคำถามใช้ในการโหวต", color = ctx.author.color)
        mbed.add_field(name = "**Syntax**", value = "!poll <question> <option1,option2..> #ตั้งคำถาม ตัวเลือก1,ตัวเลือก2..")
        await ctx.send(embed = mbed)

    @help.command()
    async def random(self, ctx):
        mbed = discord.Embed(title = "random", description = "ตั้งโพลคำถามใช้ในการโหวต", color = ctx.author.color)
        mbed.add_field(name = "**Syntax**", value = "!random <number1> <number2> #สุ่มเลขตั้งแต่ จำนวนที่ 1 ถึง จำนวนที่ 2")
        await ctx.send(embed = mbed)

def setup(client):
    client.add_cog(help(client))