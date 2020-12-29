import discord
import random
from discord.ext import commands

class rolereac(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.reaction_author = None
        self.message_author = None

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        channel_id = payload.channel_id
        channel = self.client.get_channel(channel_id)
        self.reaction_author = payload.user_id
        if message_id == 790159697213784094:
            if payload.emoji.name == 'getrole':
                print(self.reaction_author)
                await channel.send('Press number for random')
            elif payload.emoji.name == 'getrole2':
                print('nice two')

    @commands.Cog.listener()
    async def on_message(self, message):
        self.message_content = message.content
        self.message_userid = message.author.id
        self.message_author = message.author
        if self.reaction_author == self.message_userid:
            await message.channel.send(random.randint(1, int(message.content)))
            self.reaction_author = None
            
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        pass               

    @commands.command()
    async def set_reaction(self, ctx, msg: discord.Message=None, emoji=None):
        if msg != None and emoji != None:
            await msg.add_reaction(emoji)
            self.client.reaction_roles.append((msg, emoji))

        else:
            await ctx.send("Invalid arguments.")


def setup(client):
    client.add_cog(rolereac(client))