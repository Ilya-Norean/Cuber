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
class help(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot


	#Help
	@nextcord.slash_command(name = 'help', description = '❕Show you command list (Exaple: /help)')
	async def help(self, ctx: Interaction, module: str=None):

		if module == None:

			embed = nextcord.Embed(
				title = 'Command list',
				description = 'Learn more about specific command module: **/help <Module>**',
				color = 0xbdda45
				)

			embed.set_author(
				name = ctx.user.name,
				icon_url = ctx.user.avatar.url
				)

			#Modules

			embed.add_field(
				name = '🛡️ Moderation',
				value = '/help moderation'
				)

			embed.add_field(
				name = '📋 Information',
				value = '/help info'
				)	

			embed.add_field(
				name = '😆 Fun',
				value = '/help fun'
				)			

			embed.add_field(
				name = '🖼️ Images',
				value = '/help images'
				)

			embed.add_field(
				name = '⚡ Memes',
				value = '/help memes'
				)

			embed.add_field(
				name = '🔥 Other',
				value = '/help other'
				)

			await ctx.send(embed = embed, ephemeral=True)

		elif module == 'moderation':

			embed = nextcord.Embed(
				title = '🛡️ Moderation',
				description = '<:green:1000729796919173220>   ban    : Ban the member\n<:green:1000729796919173220>   kick    : Kick the member\n<:green:1000729796919173220>   clear    : Clear messages\n<:green:1000729796919173220>   report    : Report to the problem\n',
				color = 0xbdda45
				)

			await ctx.send(embed = embed, ephemeral=True)

		elif module == 'info':

			embed = nextcord.Embed(
				title = '📋 Information',
				description = '<:green:1000729796919173220>   user    : Shows information about User\n<:green:1000729796919173220>   server    : Shows information about Server\n<:red:1000730250344411216> bot : In developing',
				color = 0xbdda45
				)

			await ctx.send(embed = embed, ephemeral=True)

		elif module == 'fun':

			embed = nextcord.Embed(
				title = '😆 Fun',
				description = '<:green:1000729796919173220> answer : Cuber will answer on your question\n<:green:1000729796919173220> avatar : Send user avatar\n<:green:1000729796919173220> ball8 : Magic ball will answer on your question\n<:green:1000729796919173220> coin : You can flip a coinr\n<:green:1000729796919173220> cuber : Will send a Cuber for you\n<:green:1000729796919173220> emojify : Send your message as emoji\n<:green:1000729796919173220> f : Press F to paid your respect\n<:green:1000729796919173220> fact : Send a random fact\n<:green:1000729796919173220> gayrate : Find out how match you are gay\n<:green:1000729796919173220> hotcalc : Find out how match you are hot\n<:green:1000729796919173220> joke : Random Joke\n<:green:1000729796919173220> kaomoji : Send a kaomoji\n<:green:1000729796919173220> nightskye : Send a nightskye for you\n<:green:1000729796919173220> password : Generate a password for you\n<:green:1000729796919173220> quote : Random Quote\n<:green:1000729796919173220> rcolor : Random color\n<:green:1000729796919173220> spam : Spam messages\n',
				color = 0xbdda45
				)

			await ctx.send(embed = embed, ephemeral=True)

		elif module == 'images':

			embed = nextcord.Embed(
				title = '🖼️ Images',
				description = '<:green:1000729796919173220> biden : Biden tweet\n<:green:1000729796919173220> captcha : Generate captcha\n<:green:1000729796919173220> car : Random car image\n<:green:1000729796919173220> cat : Random cat image\n<:green:1000729796919173220> coffe : Random coffe image\n<:green:1000729796919173220> dog : Random dog image\n<:green:1000729796919173220> fox : Random fox image\n<:green:1000729796919173220> gay : Make your friend gay\n<:green:1000729796919173220> hug : Hug someone\n<:green:1000729796919173220> koala : Random koala image\n<:green:1000729796919173220> panda : Random panda image\n<:green:1000729796919173220> pat : Pat someone\n<:green:1000729796919173220> phcomment : PH comment\n<:green:1000729796919173220> pixelart : Make your friend avatar pixel\n<:green:1000729796919173220> trump : Trump tweet\n<:green:1000729796919173220> tweet : Tweet something\n<:green:1000729796919173220> wasted : Make Wasted to your friend\n<:green:1000729796919173220> webscreen : Send a web site screenshot\n<:green:1000729796919173220> whowouldwin : Who would win?\n<:green:1000729796919173220> wink : Wink to someone\n',
				color = 0xbdda45
				)

			await ctx.send(embed = embed, ephemeral=True)

		elif module == 'memes':

			embed = nextcord.Embed(
				title = '⚡ Memes',
				description = '<:green:1000729796919173220> drake : Make a Drake meme\n<:green:1000729796919173220> meme : Send a random meme\n<:green:1000729796919173220> oogway : Make a Oogway meme\n<:green:1000729796919173220> pikachu : Make a Pikachu meme\n<:green:1000729796919173220> pooh : Make a Pooh meme\n<:green:1000729796919173220> sadcat : Make a Sad Cat meme\n',
				color = 0xbdda45
				)

			await ctx.send(embed = embed, ephemeral=True)

		elif module == 'other':

			embed = nextcord.Embed(
				title = '🔥 Other',
				description = '<:green:1000729796919173220> afk : Will notify other participants of his absence in the near future\n<:green:1000729796919173220> invite : Create invite on the server\n<:green:1000729796919173220> ping : Ping of the bot\n<:green:1000729796919173220> poll : Create a simple poll\n<:green:1000729796919173220> say : Say something\n<:green:1000729796919173220> translate : Translator\n<:green:1000729796919173220> ping : Ping of the bot',
				color = 0xbdda45
				)

			await ctx.send(embed = embed, ephemeral=True)


#-----Run-----
def setup(bot):
	bot.add_cog(help(bot))
