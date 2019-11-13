import os
import random
import discord
from discord.ext import commands

class Ban(commands.Cog):

	def _init_(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Cog : ban, loaded')

	@commands.command(name='ban')
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		await member.ban(reason=reason)

def setup(client):
	client.add_cog(Ban(client))