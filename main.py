import discord
from discord.ext import commands
import os
import json


intents = discord.Intents.default()
intents.members = True

TOKEN = ("TOKEN")
bot = commands.Bot(command_prefix='!', intents=intents)


# admin commands

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Пользователь {member} был забанен')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Пользователь {member} был кикнут')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f'Пользователь {member} был замучен')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f'Пользователь {member} был размучен')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Удалено {amount} сообщений')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def dm(ctx, member: discord.Member, *, message):
    await member.send(message)
    await ctx.send(f'Сообщение отправлено пользователю {member}')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f'Словомод включен на {seconds} секунд')

#default commands

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def embed(ctx, *, message):
    embed = discord.Embed(title="Embed", description=message, color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx):
    embed = discord.Embed(title="Информация о пользователе", description=ctx.author.mention, color=0x00ff00)
    embed.add_field(name="Имя", value=ctx.author.name, inline=True)
    embed.add_field(name="ID", value=ctx.author.id, inline=True)
    embed.add_field(name="Статус", value=ctx.author.status, inline=True)
    embed.add_field(name="Наивысшая роль", value=ctx.author.top_role, inline=True)
    embed.add_field(name="Присоединился", value=ctx.author.joined_at, inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title="Информация о сервере", description=ctx.guild.name, color=0x00ff00)
    embed.add_field(name="ID", value=ctx.guild.id, inline=True)
    embed.add_field(name="Регион", value=ctx.guild.region, inline=True)
    embed.add_field(name="Участников", value=ctx.guild.member_count, inline=True)
    embed.add_field(name="Создатель", value=ctx.guild.owner, inline=True)
    embed.add_field(name="Дата создания", value=ctx.guild.created_at, inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Информация о боте", description="Бот создан для удобства администрации сервера", color=0x00ff00)
    embed.add_field(name="Создатель бота", value="wezersovvv#9439", inline=False)
    embed.add_field(name="Telegram создатиеля", value="https://t.me/wezersovvv", inline=False)
    embed.add_field(name="Версия бота", value="1.1", inline=False)
    await ctx.send(embed=embed)


    


@bot.event
async def on_ready():
    print('Bot logged in as: {0.user.name} - {0.user.id}'.format(bot))

bot.run(TOKEN)
