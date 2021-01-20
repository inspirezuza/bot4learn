import discord
import datetime
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

class joinleave(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_member_join(self, ctx, member):
        db = sqlite3.connect('main.sqlite')
        # cursor = db.cursor()
        # cursor.execute(f'SELECT channel_id FROM main WHERE guild_id = {ctx.guild.id}')
        # result = cursor.fetchone()
        if result is None:
            return
        else:
            cursor.execute(f'SELECT msg FROM main WHERE guild_id = {ctx.guild.id}')
            result = cursor.fetchone()
            # members = len(list(member.guild.members))
            # mention = member.mention
            # user = member.name
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
        mbed.set_thumbnail(url=f"{member.avatar_url}")
        mbed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        mbed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        mbed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=mbed)

    @commands.group()
    async def Welcome(self, ctx):
        await ctx.send('Available Setup Commands : \nwelcome channel <#channel>\nwelcome text <message>')

    @welcome.command()
    async def channel(self, ctx, channel:discord.TextChannel):
        if ctx.message.author.guild_permissions.manage_messages:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT channel_id FROM main WHERE guild_id = {ctx.guild.id}')
            result = cursor.fetchone()
            if result is None:
                sql = ('INSERT INTO main(guild_id, channel_id) VALUE(?,?)')
                val = (ctx.guild.id, channel.id)
                await ctx.send(f'Channel has been set to {channel.mention}')
            elif result is not None:
                sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
                val = (channel.id, ctx.guild.id)
                await ctx.send(f'Channel has been updated to {channel.mention}')
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

    @welcome.command()
    async def text(self, ctx, *, text):
        if ctx.message.author.guild_permissions.manage_messages:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT msg FROM main WHERE guild_id = {ctx.guild.id}')
            result = cursor.fetchone()
            if result is None:
                sql = ('INSERT INTO main(guild_id, msg) VALUE(?,?)')
                val = (ctx.guild.id, text)
                await ctx.send(f'Message has been set to {text}')
            elif result is not None:
                sql = ("UPDATE main SET msg = ? WHERE guild_id = ?")
                val = (text, ctx.guild.id)
                await ctx.send(f'Message has been updated to {text}')
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(joinleave(client))