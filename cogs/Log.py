import discord
import datetime
from datetime import timezone,tzinfo,timedelta
from discord.ext import commands

class Log(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Log(client))