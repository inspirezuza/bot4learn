import discord
import datetime
from discord.ext import commands

class modmail(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        empty_array = []
        modmail_channel = discord.utils.get(self.client.get_all_channels(), name="mod-mail")
        if message.author == self.client.user:
            return
        if str(message.channel.type) == "private":
            if message.attachments != empty_array:
                files = message.attachments
                mbed = discord.Embed(
                    colour = (discord.Colour.green()),
                    title = f'Message from student',
                    description = f'`{message.content}`'
                )
                mbed.timestamp = datetime.datetime.utcnow()
                for file in files:
                    mbed.set_thumbnail(url=file.url)
                await modmail_channel.send(embed=mbed)
                
                
                    # await modmail_channel.send(file.url)
            else:
                mbed = discord.Embed(
                    colour = (discord.Colour.green()),
                    title = f'Message from student',
                    description = f'`{message.content}`'
                )
                mbed.timestamp = datetime.datetime.utcnow()
                await modmail_channel.send(embed=mbed)
            mbed = discord.Embed(
                    colour = (discord.Colour.green()),
                    title = f'Your message has been sent',
                    description = f'`{message.content}`'
                )
            mbed.timestamp = datetime.datetime.utcnow()
            await message.author.send(embed=mbed)
        # elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        #     member_object = message.mentions[0]
        #     if message.attachments != empty_array:
        #         files = message.attachments
        #         await modmail_channel.send("[" + message.author.display_name + "]")

        #         for file in files:
        #             await member_object.send(file.url)
        #     else:
        #         index = message.content.index(" ")
        #         string = message.content
        #         mod_message = string[index:]
        #         await member_object.send("[" + message.author.display_name + "]" + mod_message)
        
def setup(client):
    client.add_cog(modmail(client))