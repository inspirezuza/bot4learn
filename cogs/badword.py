import discord
import datetime
import os
from discord.ext import commands
from datetime import timezone,tzinfo,timedelta

with open("bad-words.txt") as file: # bad-words.txt contains one blacklisted phrase per line
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

class badword(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_message(self, message):
        for bad_word in bad_words:
            if bad_word in message.content:
                if not message.author.bot:
                    mbed = discord.Embed(
                    colour = (discord.Colour.red()),
                    title = 'Oops!',
                    description = f"{message.author.mention}, your message has been censored."
                    )
                    await message.channel.send(embed=mbed)
                    await message.delete()
                    break
                else:
                    break

def setup(client):
    client.add_cog(badword(client))