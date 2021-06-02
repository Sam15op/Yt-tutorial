#import discord!
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="#")

@client.event
async def on_ready():
	print('Bot is ready to go!')

@client.command()
async def hello(ctx):
	await ctx.send('Hello there!')


client.run('your token!')
