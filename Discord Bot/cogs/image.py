#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp
import time
import os


from nextcord.ext import commands
from nextcord import Interaction


#-----Commands----- 
class images(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	#Dog
	@nextcord.slash_command(name = 'dog', description = '🐶Random Dog image (Exaple: /dog)')
	async def dog(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/dog')
			dogjson = await request.json()

		embed = nextcord.Embed(
			title = '🐶 Pictures | Dog',
			color = 0x49FF2C
			).set_image(url=dogjson['link'])

		await ctx.send(embed = embed)

	#Cat
	@nextcord.slash_command(name = 'cat', description = '🐱Random Cat image (Exaple: /cat)')
	async def cat(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/cat')
			catjson = await request.json()

		embed = nextcord.Embed(
			title = '🐱 Pictures | Cat', 
			color=0x49FF2c 
			).set_image(url = catjson['link'])
		await ctx.send(embed = embed)

	#Bird
	@nextcord.slash_command(name = 'bird', description = '🦜Random Bird image (Exaple: /bird)')
	async def bird(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animal/birb')
			birdjson = await request.json()

		embed = nextcord.Embed(
			title = '🦜 Pictures | Bird',
			color = 0x49FF2c
			).set_image(url = birdjson['image'])

		await ctx.send(embed = embed)

	#Fox
	@nextcord.slash_command(name = 'fox', description = '🦊Random Fox image (Exaple: /fox)')
	async def bird(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animal/fox')
			foxjson = await request.json()

		embed = nextcord.Embed(
			title = '🦊 Pictures | Fox',
			color = 0x49FF2c
			).set_image(url = foxjson['image'])

		await ctx.send(embed = embed)	

	#Koala
	@nextcord.slash_command(name = 'koala', description = '🐨Random Koala image (Exaple: /koala)')
	async def koala(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animal/koala')
			koalajson = await request.json()

		embed = nextcord.Embed(
			title = '🐨 Pictures | Koala',
			color = 0x49FF2c
			).set_image(url = koalajson['image'])

		await ctx.send(embed = embed)

	#Panda
	@nextcord.slash_command(name = 'panda', description = '🐼Random Panda image (Exaple: /panda)')
	async def panda(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animal/panda')
			pandajson = await request.json()

		embed = nextcord.Embed(
			title = '🐼 Pictures | Panda',
			color = 0x49FF2c
			).set_image(url = pandajson['image'])

		await ctx.send(embed = embed)		


	#Random Color
	@nextcord.slash_command(name = 'rcolor', description = '🌈Random Color (Exaple: /rcolor)')
	async def rcolor(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://api.popcat.xyz/randomcolor')
			rcolor = await request.json()

		embed = nextcord.Embed(
			title = '🌈Random Color',
			color = nextcord.Color.random()
			).set_image(url = rcolor['image'])


		embed.add_field(name='Color Name', value=f"{rcolor['name']}")
		embed.add_field(name='Hex Code', value=f"#{rcolor['hex']}")


		await ctx.send(embed = embed)	

	#Coffe
	@nextcord.slash_command(name = 'coffe', description = '☕Random Coffe (Exaple: /coffe)')
	async def coffe(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://coffee.alexflipnote.dev/random.json')
			coffe = await request.json()

		embed = nextcord.Embed(
			title = '☕Random Coffe',
			color = nextcord.Color.random()
			).set_image(url = coffe['file'])

		await ctx.send(embed = embed)		

	#Car
	@nextcord.slash_command(name = 'car', description = '🚗Random Car (Exaple: /car)')
	async def car(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://api.popcat.xyz/car')
			car = await request.json()

		embed = nextcord.Embed(
			title = '🚗Random Car',
			description = car['title'],
			color = nextcord.Color.red()
			).set_image(url = car['image'])

		await ctx.send(embed = embed)


	#Web Screen
	@nextcord.slash_command(name = 'webscreen', description = '🖼Send a Web site screenshot (Exaple: /webscreen https://google.com/)')
	async def webscreen(self, ctx: Interaction, url):

		embed = nextcord.Embed(
			title = f'🖼Web Site Screenshot',
			url = url,
			color = 0xcebb04
			).set_image(url = f'https://api.popcat.xyz/screenshot?url={url}')

		await ctx.send(embed = embed)	


	#Wasted
	@nextcord.slash_command(name = 'wasted', description = '❌Make Waste to your friend (Exaple: /wasted @Cuber)')
	async def wasted(self, ctx: Interaction, user: nextcord.Member):

		url = f'https://some-random-api.ml/canvas/wasted?avatar={user.avatar.url}'

		embed = nextcord.Embed(color = user.color)
		embed.set_image(url = url)
		embed.set_author(name = user.name, icon_url = user.avatar.url)

		await ctx.send(embed = embed)

	#Gay
	@nextcord.slash_command(name = 'gay', description = '🏳️‍🌈Make your friend gay (Exaple: /gay @Cuber)')
	async def gay(self, ctx: Interaction, user: nextcord.Member):

		url = f"https://some-random-api.ml/canvas/gay?avatar={user.avatar.url}"

		embed = nextcord.Embed(color = user.color)
		embed.set_image(url = url)
		embed.set_author(name = user.name, icon_url = user.avatar.url)

		await ctx.send(embed = embed)

	#Pixel art
	@nextcord.slash_command(name = 'pixelart', description = '🎮Make your friend avatar pixel(Exaple: /pixelart @Cuber)')
	async def pixelart(self, ctx: Interaction, user: nextcord.Member):

		url = f"https://some-random-api.ml/canvas/pixelate?avatar={user.avatar.url}"

		embed = nextcord.Embed(color = user.color)
		embed.set_image(url = url)
		embed.set_author(name = user.name, icon_url = user.avatar.url)

		await ctx.send(embed = embed)

	#Captcha
	@nextcord.slash_command(name = 'captcha', description = '♻Generate captcha (Exaple: /captcha @Cuber')
	async def captcha(self, ctx: Interaction, user: nextcord.Member):

		async with aiohttp.ClientSession() as session:
			request = await session.get(f'https://nekobot.xyz/api/imagegen?type=captcha&url={user.avatar.url}&username={user.name}')
			captcha = await request.json()

		url = captcha['message']

		embed = nextcord.Embed(color = ctx.user.color)
		embed.set_image(url = url)
		embed.set_author(name = user.name, icon_url = user.avatar.url)

		asyncio.sleep(20)
			

		await ctx.send(embed = embed)

	#Who would win
	@nextcord.slash_command(name = 'whowouldwin', description = '🏆Who would win? (Exaple: /whowouldwin @Cuber @Mee6)')
	async def  whowouldwin(self, ctx: Interaction, user1: nextcord.Member, user2: nextcord.Member):

		async with aiohttp.ClientSession() as session:
			request = await session.get(f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={user1.avatar.url}&user2={user2.avatar.url}")
			www = await request.json()

		embed = nextcord.Embed(
			title = f'Who Would Win?? {user1.name} or {user2.name}',
			color = ctx.user.color
			)

		embed.set_image(url = www['message'])

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

		await vote.add_reaction('1️⃣')
		await vote.add_reaction('2️⃣')

	#Tweet
	@nextcord.slash_command(name = 'tweet', description = '🗨Tweet something (Exaple: /tweet Cuber is the beast bot!)')
	async def tweet(self, ctx: Interaction, *, text: str):

		async with aiohttp.ClientSession() as session:
			request = await session.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={ctx.user.name}&text={text}")
			tweet = await request.json()

		img = tweet['message']

		embed = nextcord.Embed(title = f"{ctx.user.name} Just Tweeted",color = ctx.user.color)		
		embed.set_image(url = img)

		await ctx.send(embed = embed)

	#Biden
	@nextcord.slash_command(name = 'biden', description = '💬Biden tweet (Exaple: /biden Cuber is a beast discord bot!)')
	async def biden(self, ctx: Interaction, *, text: str):
		embed = nextcord.Embed(
			title = 'Biden tweet',
			color = 0xecbc3e
			).set_image(url = f'https://api.popcat.xyz/biden?text={text}')

		await ctx.send(embed = embed)	

	#Trump
	@nextcord.slash_command(name = 'trump', description = '💬Biden trump (Exaple: /trump Cuber is a beast discord bot!)')
	async def trump(self, ctx: Interaction, *, text: str):

		async with aiohttp.ClientSession() as session:
			request = await session.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}")
			tweet = await request.json()	

		url = tweet['message']

		embed = nextcord.Embed(
			title = 'Trump tweet',
			color = 0xecbc3e
			)
		embed.set_image(url = url)

		await ctx.send(embed = embed)	

	#PH comment
	@nextcord.slash_command(name = 'phcomment', description = '🟧⬛PH comment (Exaple: /phcomment nice video)')
	async def phcomment(self, ctx: Interaction, *, text):

		async with aiohttp.ClientSession() as session:
			request = await session.get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={ctx.user.avatar.url}&text={text}&username={ctx.user.name}")
			comment = await request.json()

		url = comment['message']

		embed = nextcord.Embed(title=f"{ctx.user.name} just Commented On P*** Hub", color=ctx.user.color)
		embed.set_image(url = url)

		await ctx.send(embed = embed)

	#Hug
	@nextcord.slash_command(name = 'hug', description = '💛Hug someone (Exaple: /hug @Cuber)')
	async def hug(self, ctx: Interaction, user: nextcord.Member):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animu/hug')
			hugjson = await request.json()

		hearts = ['❤', '💛', '💚', '💙', '💜']

		embed = nextcord.Embed(
			description = f'{ctx.user.mention} **hug** {user.mention}**!**{random.choice(hearts)}',
			color = 0x8c70b8
			)

		embed.set_image(url = hugjson['link'])

		await ctx.send(embed = embed)

	#Pat
	@nextcord.slash_command(name = 'pat', description = '💚Pat someone (Exaple: /pat @Cuber)')
	async def pat(self, ctx: Interaction, user: nextcord.Member):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animu/pat')
			patjson = await request.json()

		hearts = ['❤', '💛', '💚', '💙', '💜']

		embed = nextcord.Embed(
			description = f'{ctx.user.mention} **has pat** {user.mention}**!**{random.choice(hearts)}',
			color = 0x8c70b8
			)

		embed.set_image(url = patjson['link'])

		await ctx.send(embed = embed)

	#Wink
	@nextcord.slash_command(name = 'wink', description = '💚Wink to someone (Exaple: /wink @Cuber)')
	async def wink(self, ctx: Interaction, user: nextcord.Member):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animu/wink')
			winkjson = await request.json()


		embed = nextcord.Embed(
			description = f'{ctx.user.mention} **has wink** {user.mention}**!**',
			color = 0x8c70b8
			)

		embed.set_image(url = winkjson['link'])

		await ctx.send(embed = embed)




#-----Run-----
def setup(bot):
	bot.add_cog(images(bot))