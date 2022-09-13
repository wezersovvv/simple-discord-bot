import discord
from discord.ext import commands
import os
import json
import random
import configparser


Token = ("token")

intents = discord.Intents.all()
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command("help")

# admin commands

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Помощь", description="Все команды бота", color=0xeee657)

    embed.add_field(name="!ping", value="Returns Pong!", inline=False)
    embed.add_field(name="!help", value="Returns this message", inline=False)
    embed.add_field(name="!userinfo", value="Удалена из-за ошибок, верну после фикса", inline=False)
    embed.add_field(name="!serverinfo", value="Info about server", inline=False)
    embed.add_field(name="!info", value="Info about developer", inline=False)
    embed.add_field(name="!clear", value="Clears the chat", inline=False)
    embed.add_field(name="!kick", value="Kicks a member", inline=False)
    embed.add_field(name="!ban", value="Bans a member", inline=False)
    embed.add_field(name="!unban", value="Unbans a member", inline=False)
    embed.add_field(name="!mute", value="Mutes a member", inline=False)
    embed.add_field(name="!unmute", value="Unmutes a member", inline=False)
    embed.add_field(name="!slowmode", value="Set slowmode in specific channel", inline=False)
    embed.add_field(name="!dm", value="Send message in dm for specific user", inline=False)
    embed.add_field(name="!say", value="Send message in chat", inline=False)
    embed.add_field(name="!addrole", value="Add role to the user", inline=False)
    embed.add_field(name="!removerole", value="Remove role from the user", inline=False)


    await ctx.send(embed=embed)

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
    embed = discord.Embed(title="Объявление", description=message, color=0x00ff00)
    await ctx.send(embed=embed)





@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title="Информация о сервере", description=ctx.guild.name, color=0x00ff00)
    embed.add_field(name="ID", value=ctx.guild.id, inline=False)
    embed.add_field(name="Участников", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Создатель", value=ctx.guild.owner, inline=False)
    embed.add_field(name="Дата создания", value=ctx.guild.created_at, inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def about(ctx):
    embed = discord.Embed(title="Информация о боте", description="Бот создан для удобства администрации сервера", color=0x00ff00)
    embed.add_field(name="Создатель бота", value="wezersovvv#9439", inline=False)
    embed.add_field(name="Telegram создателя", value="https://t.me/wezersovvv", inline=False)
    embed.add_field(name="Версия бота", value="1.1", inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f'Пользователю {member} была выдана роль {role}')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f'У пользователя {member} была снята роль {role}')



@bot.event
async def on_ready():
    print('1')

bot.run(Token)


