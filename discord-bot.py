import asyncio
import discord
import os
from timer import Timer
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='!', help_command=None)

timer = Timer()


@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))


@bot.command(name="start", help="Start a pomodoro timer")
async def start_timer(ctx):
    work_em = discord.Embed(title="Time to start working", color=10181046)
    await ctx.send(embed=work_em)
    timer.start()
    while timer.is_running():
        await asyncio.sleep(1)
        timer.tick()
        if timer.get_ticks() >= timer.get_max_ticks():
            timer.stop()
    break_em = discord.Embed(title="Time for a break", color=3066993)
    await ctx.send(embed=break_em)


@bot.command(name="stop", help="Stop the timer")
async def stop_timer(ctx):
    stop_em = discord.Embed(title="Timer stopped", color=15158332)
    await ctx.send(embed=stop_em)
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
        title="A simple Pomodoro timer bot", description=description, color=15158332)
    await ctx.send(embed=show_help_em)


bot.run(os.environ['BOT_TOKEN'])
