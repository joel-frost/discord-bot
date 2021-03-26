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
    await ctx.send("Time to work!")

bot.run(os.environ['BOT_TOKEN'])