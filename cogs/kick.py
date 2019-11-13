import os
import random
import discord
from discord.ext import commands

class Kick(commands.Cog):

	def _init_(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Cog : kick, loaded')

	@commands.command(name='kick')
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		await member.kick(reason=reason)

def setup(client):
	client.add_cog(Kick(client))