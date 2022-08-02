#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp

import datetime
import time

from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext import application_checks



#-----Commands----- 
class welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):

        print(f'New Member! {member.name}#{member.discriminator}')

        guild = self.bot.get_guild(980529126828015636)
        intro_channel = guild.get_channel(988409640779935764)
        rules_channel = guild.get_channel(984047053376213032)

        if member.bot or guild != member.guild:
            return


        embed = nextcord.Embed(
            title = 'Welcome To The Server!',
            description = f'{member.mention} has joined the server <:wumpus:999949414284136508>',
            color = 0xc6c6f5
            )

        embed.set_thumbnail(url=f"{member.avatar.url}")

        await intro_channel.send(embed = embed)

        await member.add_roles(guild.get_role(988495877788291072))


#-----Run-----
def setup(bot):
    bot.add_cog(welcome(bot))
