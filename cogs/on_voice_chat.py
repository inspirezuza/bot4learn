import discord
import datetime
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import timezone,tzinfo,timedelta

class on_voice_chat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = discord.utils.get(member.guild.text_channels, name="bot-log")
        if member.bot:
            return

        if not before.channel:
            mbed = discord.Embed(
            colour = (discord.Colour.green()),
            title = 'User Reported',
            description = f"{member.display_name} joined {after.channel.name}"
        )
            mbed.set_thumbnail(url=f"{member.avatar_url}")
            mbed.set_author(name=f"{member.display_name}", icon_url=f"{member.avatar_url}")
            mbed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
            mbed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=mbed)

        if before.channel and not after.channel:
            mbed = discord.Embed(
            colour = (discord.Colour.magenta()),
            title = 'User Reported',
            description = f"{member.display_name} left channel"
        )
            mbed.set_thumbnail(url=f"{member.avatar_url}")
            mbed.set_author(name=f"{member.display_name}", icon_url=f"{member.avatar_url}")
            mbed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
            mbed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=mbed)

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
            
def setup(client):
    client.add_cog(on_voice_chat(client))