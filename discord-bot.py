import asyncio
import discord
import os
from timer import Timer
from dotenv import load_dotenv
from discord.ext import commands

PURPLE = 10181046
GREEN = 3066993
RED = 15158332

load_dotenv()

bot = commands.Bot(command_prefix='!', help_command=None)
timer = Timer()

async def show_message(ctx, title, color):
    em = discord.Embed(title=title, color=color)
    await ctx.send(embed=em)

@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))


@bot.command(name="start", help="Start a Pomodoro timer")
async def start_timer(ctx):
    await show_message(ctx, "Time to start working", PURPLE)
    timer.start()
    while timer.is_running():
        await asyncio.sleep(1)
        timer.tick()
    await show_message(ctx, "Time for a break", GREEN)


@bot.command(name="stop", help="Stop the timer")
async def stop_timer(ctx):
    await show_message(ctx, "Timer Stopped", RED)
    timer.stop()


@bot.command(name="time", help="Show remaining time")
async def show_time(ctx):
    await ctx.send(f"Current time is: {timer.get_ticks()}")
    await ctx.send(f"Current timer status is: {timer.is_running()}")


@bot.command(name="help", help="Show help text")
async def show_help(ctx):
    help_commands = dict()
    for command in bot.commands:
        help_commands[command.name] = command.help
    description = "Bot commands are: {}".format(help_commands)
    show_help_em = discord.Embed(
        title="A simple Pomodoro timer bot", description=description, color=PURPLE)
    await ctx.send(embed=show_help_em)


bot.run(os.environ['BOT_TOKEN'])