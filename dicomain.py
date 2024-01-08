import discord
import os

client = discord.Client()

bot = commands.Bot(command_prefix='1', intents = discord.Intents.all())

@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("------------------------")
	await client.change_presence(game=discord.Game(name='', type1))

@client.event
async def on_message(message):
	if message.content.startswith("hi"):
		await bot.send_message(message.channel, "Hi")

access_token = os.inviron["BOT_TOKEN"]
client.run(access_token)
