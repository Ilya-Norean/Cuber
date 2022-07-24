#==========Import==========

import nextcord, random

from nextcord.ext import commands

#==========Commands==========
class facts(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	#50 facts
	@commands.command()
	async def fact(self, ctx):

		start = 'Did you know that: '
		facts = ['More human twins are being born now than ever before.', "A narwhal's tusk reveals its past living conditions.",
		"The first person convicted of speeding was going eight mph.", '"New car smell" is the scent of dozens of chemicals.',
		"The world wastes about 1 billion metric tons of food each year.", "The severed head of a sea slug can grow a whole new body.",
		"Hair and nails grow faster during pregnancy.", "The world's smallest reptile was first reported in 2021.",
		"Many feet bones don't harden until you're an adult.", "Some sea snakes can breathe through their skin.",
		"The heads on Easter Island have bodies.", "The moon has moonquakes.", "Goosebumps are meant to ward off predators.",
		"There's no such thing as 'pear cider.'", "Pineapple works as a natural meat tenderizer.", "Humans are the only animals that blush.",
		"The feeling of getting lost inside a mall is known as the Gruen transfer.", "The wood frog can hold its pee for up to eight months.",
		"The hottest spot on the planet is in Libya.", "You lose up to 30 percent of your taste buds during flight.", "Your nostrils work one at a time.",
		"Only two mammals like spicy food: humans and the tree shrew.", "A chef's toque contains 100 folds.", "Rabbits can't puke.", 'The "M`s" in M&Ms stand for "Mars" and "Murrie."',
		"The human body literally glows.", 'Copper door knobs are self-disinfecting.', "Cotton candy was invented by a dentist.", "Marie Curie is the only person to earn a Nobel prize in two different sciences.",
		"Fingernails don't grow after you die.", 'The English word with the most definitions is "set."', 'Pigeons can tell the difference between a painting by Monet and Picasso.',
		'The dot over the lower case "i" or "j" is known as a "tittle."', 'Chewing gum boosts concentration.', "Superman didn't always fly.", "The first computer was invented in the 1940s.",
		"Space smells like seared steak.", "The longest wedding veil was the same length as 63.5 football fields.", "The unicorn is the national animal of Scotland.", "Bees sometimes sting other bees.",
		"Kids ask 300 questions a day.", 'The total weight of ants on earth once equaled the total weight of people.', '"E" is the most common letter and appears in 11 percent of all english words.', 'A dozen bodies were once found in Benjamin Franklin`s basement.',
		'The healthiest place in the world is in Panama.', 'A pharaoh once lathered his slaves in honey to keep bugs away from him.', "Some people have an extra bone in their knee (and it's getting more common).",
		"Pringles aren't actually potato chips.", "There's a giant fish with a transparent head."]
		emoji = ['📚', '💡', '📕', '📖', '📗', '📘', '📝', '📙'] 

		await ctx.send(start + random.choice(facts) + random.choice(emoji))

#==========Run==========
def setup(bot):
	bot.add_cog(facts(bot))