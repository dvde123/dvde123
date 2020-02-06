import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '.' )
client.remove_command('help')
@client.event

async def on_ready():
	print( 'Bot connected' )

@client.command( pass_context = True)

async def hello(ctx):
	await ctx.channel.purge(limit=1)
	author=ctx.message.author
	await ctx.send(f' {author.mention} hello. I am Bot')

@client.command( pass_context = True)
@commands.has_permissions(administrator=True)

async def clear(ctx, amount=100):
	await ctx.channel.purge(limit = amount+1)

@client.command( pass_context = True)
@commands.has_permissions(administrator=True)

async def kick(ctx,member: discord.Member, *, reason=None):
	await ctx.channel.purge(limit=1 )
	await ctx.send(f'kick user {member.name}')
	await member.kick(reason=reason)

@client.command( pass_context = True)
@commands.has_permissions(administrator=True)

async def ban(ctx,member: discord.Member, *, reason=None):
	await ctx.channel.purge(limit=1 )
	await ctx.send(f'ban user {member.name}')
	await member.ban(reason=reason)

@client.command( pass_context = True)
@commands.has_permissions(administrator=True)

async def unban(ctx, *, member):
	await ctx.channel.purge(limit=1 )
	banned = await ctx.guild.bans()
	for ban_entry in banned:
		user = ban_entry.user
		await ctx.guild.unban(user)
		await ctx.send(f'unbanned user {user.mention}')
		return

@client.command( pass_context = True)

async def help(ctx):
	await ctx.channel.purge(limit=1 )
	emb=discord.Embed(title='навигация по каммандам')
	emb.add_field(name='{}clear'.format('.'),value='очистка чата')
	emb.add_field(name='{}kick'.format('.'),value='кикает игрока')
	emb.add_field(name='{}ban'.format('.'),value='банит игрока')
	emb.add_field(name='{}mute'.format('.'),value='не даёт иму разговаривать')
	emb.add_field(name='{}unmute'.format('.'),value='даёт иму разговаривать')
	emb.add_field(name='{}addrole'.format('.'),value='даёт игроку роль')
	emb.add_field(name='{}unrole'.format('.'),value='отнимает у игрока роль')
	await ctx.send(embed = emb)

@client.command( pass_context = True)
@commands.has_permissions(administrator=True)

async def mute(ctx, member: discord.Member):
	await ctx.channel.purge(limit=1 )
	mute_role=discord.utils.get(ctx.message.guild.roles, name = 'MUTE')
	await member.add_roles(mute_role)
	await ctx.send(f'mute {member.mention}')

@client.command( pass_context = True)
@commands.has_permissions(administrator=True)

async def unmute(ctx, member: discord.Member):
	await ctx.channel.purge(limit=1 )
	unmute_role=discord.utils.get(ctx.message.guild.roles, name = 'MUTE')
	await member.remove_roles(unmute_role)
	await ctx.send(f'unmute {member.mention}')

@client.command( pass_context = True)
@commands.has_permissions(administrator=True)

async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    await member.add_roles(role)
    await ctx.channel.purge(limit=1 )
    await ctx.send(f'role {role} add {member.mention}')

@client.command( pass_context = True)
@commands.has_permissions(administrator=True)

async def unrole(ctx, role: discord.Role, member: discord.Member=None):
    await member.remove_roles(role)
    await ctx.channel.purge(limit=1 )
    await ctx.send(f'unrole {role} : {member.mention}')





client.run("Njc0NjQ0NjAwMjA3NDQxOTQx.Xjv92A.rWUEDKuBbdl_f00rzMjNHehbuZY")
