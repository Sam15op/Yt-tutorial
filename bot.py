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


client.run('ODQxNjg0Nzg4ODU5MzcxNTQw.YJqWCw.2w9F_OPLo-Dx_MZavnz-d2PTJio')