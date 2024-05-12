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
            



client.run("MTIzODUzMTY5MDI4MDc3OTgxNg.GwF24M.0AjdD6RAa_e8559uzMqz1JqU6X7-IA3M3u1rfs")
  
