#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp
import time

from nextcord.ext import commands
from nextcord import Interaction


#-----Commands----- 
class memes(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	#Random Meme
	@nextcord.slash_command(name = 'meme', description = '🤣Random Meme (Exaple: /meme')
	async def meme(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://api.popcat.xyz/meme')
			memejson = await request.json()

		embed = nextcord.Embed(
			title = '🤣 Random Meme',
			description = memejson['title'],
			color = nextcord.Color.random()
			).set_image(url = memejson['image'])

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

		await vote.add_reaction('❤')

	#Drake meme
	@nextcord.slash_command(name = 'drake', description = '😎Drake meme (Exaple: /pooh Mee6 Cuber)')
	async def drake(self, ctx: Interaction,  *, text1: str, text2: str):
		embed = nextcord.Embed(
			title = 'Drake meme',
			color = 0xcebb04
			).set_image(url = f'https://api.popcat.xyz/drake?text1={text1}&text2={text2}')

		await ctx.send(embed = embed)

	#Pooh meme
	@nextcord.slash_command(name = 'pooh', description = '🍯Pooh meme (Exaple: /pooh Mee6 Cuber)')
	async def pooh(self, ctx: Interaction, *, text1: str, text2: str):
		embed = nextcord.Embed(
			title = 'Pooh meme',
			color = 0xf2f2f2
			).set_image(url = f'https://api.popcat.xyz/pooh?text1={text1}&text2={text2}')

		await ctx.send(embed = embed)

	#Oogway meme !
	@nextcord.slash_command(name = 'oogway', description = '🐢Oogway meme (Exaple: /oogway Go forth on your path, as it exists only through your walking')
	async def oogway(self, ctx: Interaction, *, text: str):
		embed = nextcord.Embed(
			title = 'Oogway meme',
			color = 0x376183
			).set_image(url = f'https://api.popcat.xyz/oogway?text={text}')

		await ctx.send(embed = embed)

	#Sad cat
	@nextcord.slash_command(name = 'sadcat', description = '😿Sad Cat meme (Exaple: /sadcat you)')
	async def sadcat(self, ctx: Interaction, *, text: str):
		embed = nextcord.Embed(
			title = 'Sad Cat meme',
			color = 0x376183
			).set_image(url = f'https://api.popcat.xyz/sadcat?text={text}')

		await ctx.send(embed = embed)

	#Pikachu
	@nextcord.slash_command(name = 'pikachu', description = '⚡Pikachu meme (Exaple: /pikachu Cuber is a beast discord bot)')
	async def pikachu(self, ctx: Interaction, *, text: str):
		embed = nextcord.Embed(
			title = 'Pikachu meme',
			color = 0xecbc3e
			).set_image(url = f'https://api.popcat.xyz/pikachu?text={text}')

		await ctx.send(embed = embed)



#-----Run-----
def setup(bot):
	bot.add_cog(memes(bot))
