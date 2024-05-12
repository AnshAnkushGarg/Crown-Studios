import json
import discord
import os
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
from web_server import keep_alive
import random



keep_alive()


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = commands.Bot(command_prefix="!",intents=intents)

@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def gameban(ctx, id: int):
    with open("banned.json", "r+") as file:
        data = json.load(file)
        data["banned_users"].append(id)
        file.seek(0)
        json.dump(data, file, indent=4)

@client.command()
async def listbanned():
    with open("banned.json", "r+") as file:
        data = json.load(file)
        await ctx.channel.send(data["banned_users"])
            


token = os.environ.get("TOKEN")
client.run(token)

