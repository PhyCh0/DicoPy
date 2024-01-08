import discord
from discord.ext import commands

token = 'MTE5MzkxMTE2NzQwMDI5NjUzMA.GiwDWz.61B__0LBCeneaYq7mkUgNa-uPhlvGY9fFrykA8'

bot = commands.Bot(command_prefix='1', intents = discord.Intents.all())

@bot.event
async def on_ready():
	print("Bot Is Online")

bot.run(token)