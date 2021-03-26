import asyncio
import discord
import os
from timer import Timer
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='!')

timer = Timer()

@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))

@bot.command(name="start", help="Start a pomodoro timer")
async def start_timer(ctx):
    work_em = discord.Embed(title="Time to start working", color=10181046)
    await ctx.send(embed = work_em)
    
    timer.start()
    while timer.get_status():
        await asyncio.sleep(1)
        timer.tick()
        if timer.get_ticks() >= timer.get_max_ticks():
            timer.stop()

    break_em = discord.Embed(title="Time for a break", color=3066993)
    await ctx.send(embed=break_em)

@bot.command(name="stop", help="Stop the timer")
async def stop_timer(ctx):
    stop_em = discord.Embed(title="Timer stopped", color=15158332)
    await ctx.send(embed = stop_em)
    timer.stop()

bot.run(os.environ['BOT_TOKEN'])