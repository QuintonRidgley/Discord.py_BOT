# Minimal.py
# Quinton Ridgley
import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['Commands | .help', 'Try | .clear', 'Try | .ban', 'Try | .kick'])

@client.event
async def on_ready():
	change_status.start()

@tasks.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

#@client.event
#async def on_ready():
#	print ('has connected to Discord!')

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjQzMTQ0NjIwNDYwNzM2NTEy.Xct1sA.qduSaqf3vSRPCdavNxuVzLliJ0I')
