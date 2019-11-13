import discord
from discord.ext import commands

class Clear(commands.Cog):

	def _init_(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Cog : clear, loaded')

	@commands.command(name='clear')
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=10):
		await ctx.channel.purge(limit=amount)

def setup(client):
	client.add_cog(Clear(client))