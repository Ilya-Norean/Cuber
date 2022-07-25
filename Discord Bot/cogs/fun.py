#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp

import string


from nextcord.ext import commands
from nextcord import Interaction

#-----Commands-----  
class fun(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	#Spam
	@nextcord.slash_command(name = 'spam', description = '📨Spam messages. (Exaple: /spam @everyone 100)')
	async def spam(self, ctx: Interaction, message: str, amount: int):

		embed = nextcord.Embed(
			title = '📨 Spam',
			description = 'Have a good day)',
			color = nextcord.Color.random()
			)

		await ctx.send(embed = embed)

		for x in range(amount):
			await ctx.user.send(f'{message}')


	#Emojify
	@nextcord.slash_command(name = 'emojify', description = '🎃Sends your message as emoji (Exaple: /emojify Hello World)')
	async def emojify(self, ctx: Interaction, text):

		emojis = []

		for s in text.lower():
			if s.isdecimal():
				num2emo = {'0':'zero', '1':'one', '2':'two',
				'3':'three', '4':'four', '5':'five', '6':'six',
				'7':'seven', '8':'eight', '9':'nine'}

				emojis.append(f':{num2emo.get(s)}')

			elif s.isalpha():
				emojis.append(f':regional_indicator_{s}:')
			else:
				emojis.append(s)

		await ctx.send(''.join(emojis))

	#Press F  
	@nextcord.slash_command(name = 'f', description = '💜Press F ro paid your respect')
	async def f(self, ctx: Interaction, user: nextcord.Member):
		hearts = ['❤', '💛', '💚', '💙', '💜']

		embed = nextcord.Embed(
			title = f'<:press_f:1000080953462493194>  Press **F**',
			description = f'{ctx.user.mention} has paid their respect {user.mention} {random.choice(hearts)}',
			color = 0x8c70b8
			)


		await ctx.send(embed = embed)

	#Eightball
	@nextcord.slash_command(name = 'ball8', description = '🎱Magic ball will answer on your question (Exaple: /ball8 Cuber is human?)')
	async def ball8(self, ctx: Interaction, question):

		ballresponse = [
		"Yes", "No", "It is certain", "It is decidedly so", "Without a doubt",
		"Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely",
		"Outlook good", "Yes", "Signs point to yes", "Without a doubt... yes.",
		"Without a doubt... no.", "HAHAHAHAHAHA no.", "Who knows! I don't!",
		"Are you for real?", "Most definitely not.", "I'll think about it"
		]

		answer = random.choice(ballresponse)

		embed = nextcord.Embed(
			title = 'EightBall🎱',
			description = f'**Question:** {question}\n**Answer:** {answer}',
			color = 0x886ce4
			)

		await ctx.send(embed = embed)

	#Avatar 
	@nextcord.slash_command(name = 'avatar', description = '🎃Send user avatar (Exaple: /avatar @Cuber#1168)')
	async def avatar(self, ctx:	Interaction, user: nextcord.Member):

		embed = nextcord.Embed(
			title = f'Avatar of **{user.name}**',
			color = 0x4a8cf5
			).set_image(url = user.avatar.url)
		await ctx.send(embed = embed)

	#Gayrate
	@nextcord.slash_command(name = 'gayrate', description = '🌈How much gay you are gay? (Exaple: /gayrate @Cuber#1168)')
	async def gayrate(self, ctx: Interaction, user: nextcord.Member):
		user = user.name + ' is'

		embed = nextcord.Embed(
			title = 'Gay rate machine',
			description = f'{user} **{random.randint(0, 101)}%** gay🌈',
			color = nextcord.Color.random()
			)
		await ctx.send(embed = embed)

	#Hotcalc
	@nextcord.slash_command(name = 'hotcalc', description = '💖How much you are hot? (Exaple: /hotcalc @Cuber#1168)')
	async def hotcalc(self, ctx: Interaction, user: nextcord.Member):
		user = user.name

		r = random.randint(1, 101)
		hot = r / 1.17

		if hot > 80:
			emoji = '💞'
		elif hot > 50:
			emoji = '💖'
		elif hot > 30:
			emoji = '❤'
		else:
			emoji = '💔'

		embed = nextcord.Embed(
			title = 'Hotcalc',
			description = f'**{user}** is **{hot:.2f}%** hot {emoji}',
			color = 0xff0000
			)

		await ctx.send(embed = embed)

	#Answer
	@nextcord.slash_command(name = 'answer', description = '💡Cuber will answer on your question (Exaple: /answe Cuber is the beast discord bot?)')
	async def answer(self, ctx: Interaction, question):
		answer = [' **Yes**', ' **No**']
		await ctx.send(f'"{question}" - i think {random.choice(answer)}')

	#Random Fact
	@nextcord.slash_command(name = 'fact', description = '📚Send a Random Fact (Exaple: /fact )')
	async def facts(self, ctx: Interaction):

		start = 'Did you know that:'
		emoji = ['📚', '💡', '📕', '📖', '📗', '📘', '📝', '📙']


		async with aiohttp.ClientSession() as session:
			request = await session.get('https://api.popcat.xyz/fact')
			factjson = await request.json()

		embed = nextcord.Embed(
			title = start,
			description = factjson['fact'],
			color = 0x49FF2C
			)

		await ctx.send(embed = embed)

	#Joke
	@nextcord.slash_command(name = 'joke', description = '😜Send a Random Joke (Exaple: /jok)')
	async def joke(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://api.popcat.xyz/joke')
			jokejson = await request.json()

		embed = nextcord.Embed(
			title = '😜Random Joke',
			description = jokejson['joke'],
			color = 0x49FF2C
			)

		await ctx.send(embed = embed)

	#Passwor generator
	@nextcord.slash_command(name = 'password', description = '🔒Send a Random Password (Exaple: /password 20)')
	async def password(self, ctx: Interaction, amount):

		characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

		
		length = int(amount)

		random.shuffle(characters)

		password = []
		for i in range(length):
			password.append(random.choice(characters))

		random.shuffle(password)

		embed_main = nextcord.Embed(
			title = '🔒 Your Password',
			description = 'Your password has been sent successfully!',
			color = 0x282a36
			)

		await ctx.send(embed = embed_main, ephemeral=True)

		embed_user = nextcord.Embed(
			title = '🔒 Your Password',
			description = f'||{"".join(password)}||',
			color = 0x8c70b8
			)

		await ctx.user.send(embed = embed_user)
	
	#Quote
	@nextcord.slash_command(name = 'quote', description = '💭Random Quote (Exaple: /quote)')
	async def quote(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://api.popcat.xyz/quote')
			quote = await request.json()

		embed = nextcord.Embed(
			title = '💭Random Quote',
			description = quote['quote'],
			color = nextcord.Color.blue()
			)

		await ctx.send(embed = embed)	

	#Coin 
	@nextcord.slash_command(name = 'coin', description = '💲Flip a coin (Exaple: /coin)')
	async def coin(self, ctx: Interaction, ):

		coin = ['heads', 'tails']

		embed = nextcord.Embed(
			title = ':coin: Coin!',
			description = f'{ctx.user.mention} was flipped a Coin , it was **{random.choice(coin)}**!',
			color = 0xf2f2f2
			)

		embed.set_thumbnail(url = 'https://i.gifer.com/origin/e0/e02ce86bcfd6d1d6c2f775afb3ec8c01_w200.gif')

		await ctx.send(embed = embed)

	#Translator
	@nextcord.slash_command(name = 'translate', description = '🔠Translator (Exaple: /transalte en buenos+dias)')
	async def translate(self, ctx: Interaction, *, to:str, text:str):

		async with aiohttp.ClientSession() as session:
			request = await session.get(f'https://api.popcat.xyz/translate?to={to}&text={text}')
			translate = await request.json()

		embed = nextcord.Embed(
			title = '🔠 Your Translate:',
			description = translate['translated'],
			color = nextcord.Color.blue()
			)

		await ctx.send(embed = embed)		


	#Kaomoji
	@nextcord.slash_command(name = 'kaomoji', description = '🥰Send a Kaomoji (Exaple: /kaomoji)')
	async def kaomoji(self, ctx: Interaction):

		kaomoji = ['(* ^ ω ^)','(＠＾◡＾)','٩(｡•́‿•̀｡)۶','(￢‿￢ )','(.❛ ᴗ ❛.)'
		'(„• ֊ •„)','(๑˘︶˘๑)','(≧◡≦)','(⌒ω⌒)','(＾▽＾)','(´• ω •`)','٩(｡•́‿•̀｡)۶',
		'(〃＾▽＾〃)','｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡','｡ﾟ(TヮT)ﾟ｡','ヽ(・∀・)ﾉ','(o･ω･o)','	(￣ω￣)']

		embed = nextcord.Embed(
			title = random.choice(kaomoji),
			color = 0x8c70b8
			)

		await ctx.send(embed = embed)

	#Cuber
	@nextcord.slash_command(name = 'cuber', description = '😻Will send you a Cuber (Exaple: /cuber)')
	async def cuber(self, ctx: Interaction):
		await ctx.send('<:kittydark:992031413287268373> ')

	#Afk
	@nextcord.slash_command(name = 'afk', description = '🌜Afk (Exaple: /afk)')
	async def afk(self, ctx: Interaction):
		await ctx.send(f':wave: | See you later!')

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
	bot.add_cog(fun(bot))
