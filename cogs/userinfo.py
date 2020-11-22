import discord
import datetime
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

class userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        mbed = discord.Embed(colour=member.color)
        mbed.timestamp = datetime.datetime.utcnow()
        mbed.set_author(name=f"User Info - {member}")
        mbed.set_thumbnail(url=member.avatar_url)
        mbed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        mbed.add_field(name="ID:", value=member.id)
        mbed.add_field(name="Guild name:", value=member.display_name)

        mbed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        mbed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))

        mbed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        mbed.add_field(name="Top role:", value=member.top_role.mention)

        mbed.add_field(name="Bot?", value=member.bot)

        await ctx.send(embed=mbed)

def setup(client):
    client.add_cog(userinfo(client))