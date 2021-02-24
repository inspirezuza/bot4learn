import discord
from discord.ext import commands

from cogs.gsheet import *


class sheet(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.sheet = gsheet()

    

    @commands.Cog.listener()
    async def on_message(self, message):

        # Restrict the command to a role
        # Change REQUIREDROLE to a role id or None
        REQUIREDROLE = None
        if REQUIREDROLE is not None and discord.utils.get(message.author.roles, id=str(REQUIREDROLE)) is None:
            await message.channel.send('You don\'t have the required role!')
            return

        # Command to insert data to excel
        if message.content.startswith('!s '):
            SPREADSHEET_ID = '1QsFYP5Xf_8PXgkcJOSVLde1hZ1xedOrNpB1MUfwopNY' # Add ID here
            RANGE_NAME = 'A1'
            FIELDS = 2 # Amount of fields/cells

            # Code
            msg = message.content[3:]
            result = [x.strip() for x in msg.split(',')]
            if len(result) == FIELDS:
                # Add
                print(message.created_at)
                DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + result
                self.sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
                await message.channel.send('Your data has been successfully submitted!')
            else:
                # Needs more/less fields
                await message.channel.send('Error: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS,FIELDS-1))

        if message.content.startswith('.create '):
            msg = message.content[8:]
            self.sheet.create(msg)
            print("go on")
            await message.channel.send('go on')

def setup(client):
    client.add_cog(sheet(client))