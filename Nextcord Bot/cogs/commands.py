#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp
import time
import os

from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext import application_checks




#-----Commands----- 
class cmd(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot


	#Poll 
	@nextcord.slash_command(name = 'poll', description = '🥑Create simple poll (Exaple: /poll Cuber is Human?)')
	@application_checks.has_permissions(administrator=True)
	async def poll(self, ctx: Interaction, message):

		rm_emoji_v = ['🎉','🎃','🎁','🎈','💣','⚡','🔥','💧',
		'🌈','🪐','🌌','🧁','🍧','🎂','☕','🍺','🍒','🍓',
		'🧊','🥑','❄','🧨','⚽','🎱','🪁','🎯','🏆','🎮',
		'🔮','🎲','🎶','💡','❄','⛄','🌊','🎨','🎊','❤',]
		

		rm_emoji = random.choice(rm_emoji_v)

		embed = nextcord.Embed(
			title = 'Poll!' + rm_emoji,
			description = f'{message}',
			color = 0xc6c6f5
			)

		await ctx.send(embed = embed)

		message : nextcord.Message
		async for message in ctx.channel.history():
			if not message.embeds:
				continue
			elif message.embeds[0].title == embed.title:
				vote = message
				break
			else:
				return

		await vote.add_reaction('👍')
		await vote.add_reaction('👎')
		
	#Ping 
	@nextcord.slash_command(name = 'ping', description = '🏓Ping of the bot (Exaple: /ping)')
	async def ping(self, ctx: Interaction):

		embed = nextcord.Embed(
			title = '🏓 Pong!',
			description = f'`Ping: {round(self.bot.latency * 1000)}ms`',
			color = 0xdb2e44
			)

		await ctx.send(embed = embed)

	#Source code
	@nextcord.slash_command(name = 'source', description = '🤖Bot Source code (Exaple: /source)')
	async def source(self, ctx: Interaction):

		embed = nextcord.Embed(
			title = '🤖 Bot Source code',
			description = f"Here's the github link for the Bot: **https://github.com/Ilya-Norean/Cuber**",
			color = 0xc6c6f5
			)

		await ctx.send(embed = embed)

	#Say
	@nextcord.slash_command(name = 'say', description = '🗨 Say something')
	@application_checks.has_permissions(administrator=True)
	async def say(self, ctx: Interaction, text):
		await ctx.send(text)

	#Invite
	@nextcord.slash_command(name = 'invite', description = '🔗Create invite on the server (Exaple: /invite)')
	async def invite(self, ctx: Interaction):
		link = await ctx.channel.create_invite(max_age=10)

		embed = nextcord.Embed(
			title = '🔗 Your Link',
			description = f'{link}',
			color = 0xc6c6f5
			)

		await ctx.send(embed = embed)


#-----Run-----
def setup(bot):
	bot.add_cog(cmd(bot))
