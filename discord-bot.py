import asyncio
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))

@bot.command(name="start", help="Start a pomodoro timer")
async def start_timer(ctx):
    work_em = discord.Embed(title="Time to start working", color=10181046)
    await ctx.send(embed = work_em)
    await asyncio.sleep(3)
    break_em = discord.Embed(title="Time for a break", color=3066993)
    await ctx.send(embed=break_em)

@bot.command(name="stop", help="Stop the timer")
async def stop_timer(ctx):
    stop_em = discord.Embed(title="Timer stopped", color=15158332)
    await ctx.send(embed = stop_em)

bot.run(os.environ['BOT_TOKEN'])