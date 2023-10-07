import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def boszen(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}bosen?liburan dong,ko malah les')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def laper(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}laper?? ya tinggal makan')

bot.run("MTE1NTA2NDQ1OTYwNjM4MDU0NA.GR5wbJ.GNdXhv3Dle0lY2CPHn6IRZuXyQh_PzIWNf6G70")
