import discord

from discord.ext import commands
from discord_components import DiscordComponents

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!",intents=intents)
DiscordComponents(client)

client.load_extension("cogs.maincog")
client.run('OTYzMDg3MTQ2NzI0NTA3NzUw.YlQ-zQ.YrR1s8gnExurS_8A1TGQgRlBuaU')

