# Minimal.py
# Quinton Ridgley
import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['Commands | .help', 'Try | .clear'])

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

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

#Commands

#@client.command(name='kick')
#@commands.has_permissons(kick_members=True)
#async def kick(ctx, member : discord.Member, *, reason=None):
#	await member.kick(reason=reason)

#@client.command(name='ban')
#@commands.has_permissons(ban_members=True)
#async def ban(ctx, member : discord.Member, *, reason=None):
#	await member.ban(reason=reason)


client.run('MY_TOKEN')
