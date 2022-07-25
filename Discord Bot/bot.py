#-----Imports-----
import nextcord

from nextcord.ext import commands
from nextcord import Interaction

import os


#-----Var-----
intents = nextcord.Intents.default()

bot = commands.Bot(intents = intents)

bot.remove_command('help')

token = 'Your Token'

#-----Ready?-----
@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game('Cuber Love ❤'))

    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))


#-----Cogs-----
initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append('cogs.' + filename[:-3])

if __name__ == '__main__':
    for extention in initial_extensions:
        bot.load_extension(extention)

#-----Run-----
bot.run(token)
