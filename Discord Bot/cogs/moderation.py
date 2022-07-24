#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp
import time
import os
import datetime

from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext import application_checks

from datetime import datetime
from datetime import timedelta




#-----Commands----- 
class moderation(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot


	#Clear
	@nextcord.slash_command(name = 'clear', description = '❌Clear messages (Exaple: /clear 10) (Only for admins)')
	@application_checks.has_permissions(administrator=True)
	async def clear(self, ctx: Interaction, amount: int):

		if amount > 1000:
			embed = nextcord.Embed(
				title = '❌Error',
				description = "I'm sorry, but that's too big for me. Try something smaller.",
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

		else:
			 
			await ctx.channel.purge(limit = amount)

			embed = nextcord.Embed(
				title = '❌Clear',
				description = f'Successfully deleted {amount} messages',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

	#Ban
	@nextcord.slash_command(name = 'ban', description = '❌Ban the user (Exaple: /ban @Mee6')
	@application_checks.has_permissions(administrator=True)
	async def ban(self, ctx: Interaction, user: nextcord.Member, reason: str = None):

		if reason is None:

			await user.ban()

			embed = nextcord.Embed(
				title = '❌Ban',
				description = f'{user.name} has been banned from {ctx.guild.name}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

		else:

			await user.ban(reason = reason)

			embed = nextcord.Embed(
				title = '❌Ban',
				description = f'{user.name} has been banned from {ctx.guild.name}. Reason: {reason}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

	#Kick
	@nextcord.slash_command(name = 'kick', description = '❌Kick the user (Exaple: /kick @Mee6')
	@application_checks.has_permissions(administrator=True)
	async def kick(self, ctx: Interaction, user: nextcord.Member, reason: str = None):

		if reason is None:

			await user.kick()

			embed = nextcord.Embed(
				title = '❌Kick',
				description = f'{user.name} has kicked from {ctx.guild.name}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

		else:

			await user.kick(reason = reason)

			embed = nextcord.Embed(
				title = '❌Kick',
				description = f'{user.name} has been kicked from {ctx.guild.name}. Reason: {reason}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)


	#Report
	@nextcord.slash_command(name = 'report', description = '❗Report (Exaple: /report)')
	async def report(self, ctx: Interaction, user: nextcord.Member, problem, description):
		

		channel = self.bot.get_channel(998875470047232081)  # <= report channel id

		staff = nextcord.utils.get(ctx.guild.roles, id = 984366923586351115)  # <= admin role id

		embed = nextcord.Embed(
			title = '**❗ Report:**',
			description = f'**Filed a complaint by**: {ctx.user.mention}\n**Complaint filed against:** {user.mention}\n**Complaint:** {problem}\n**Description:** {description}',
			colour = nextcord.Color.red()
			)
		

		 #­

		await channel.send(staff.mention, embed = embed)
		


#-----Run-----
def setup(bot):
	bot.add_cog(moderation(bot))