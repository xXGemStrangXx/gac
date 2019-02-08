import discord
import os
import sys
import datetime

from discord.ext import commands

token = os.getenv('TOKEN')
dev = 484555504241082379
prefix = "//"

bot = commands.Bot(commands_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_guild_join(guild):
	msg = "Yo, What's up. I'm the server bot. Amazing I know. I have been raised by `@Jaxorus#4786` as he knows how to code me.\n",
	"I am built for random art pictures, random gifs, what ever.\n\nIf you have any suggestions feel free to do <prefix>suggest so Jax can see it."

@bot.event
async def on_ready():
	# await bot.change_presence(
	# status = discord.Status.online,
	# activity = discord.Activity(
	# 	name = "g!help",
	# 	type = discord.ActivityType.watching
	# 	)
	# )
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print(bot.user.name + 'is ready to go')
	print('------')

bot.run(token)
