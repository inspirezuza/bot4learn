import discord
from discord.ext import commands

class rolereac(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 790159697213784094:
            # channel = self.client.get_channel('role-react')
            # guild_id = payload.guild_id
            # guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'getrole':
                print('nice one')
                # await ctx.send('เห้อ')

            elif payload.emoji.name == 'getrole2':
                print('nice two')

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