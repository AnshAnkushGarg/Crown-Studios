import json
import discord
import os
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
from web_server import keep_alive
import random


data_api = "https://ap-south-1.aws.data.mongodb-api.com/app/data-mahzb/endpoint/data/v1/action/updateOne"
api_key = os.environ.get("MONGO_KEY")
bans_id = "6640dd7a8e1d44b6e1654de4"
header = header = {"Content-Type": "application/ejson", "Accept": "application/json", "apiKey": api_key}

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
    if id == 2959339599:
        await ctx.channel.send(f"Cannot ban {id} as he is the owner!")
        return
    data = {"dataSource": "Cluster0", "database": "CrownStudios", "collection": "BANS", "filter": {"_id": {"$oid": bans_id}}, "update": {"$push": {"bans": id}}}
    r = requests.post(data_api, json=data, headers=header)
    await ctx.channel.send(f"Sent Ban Request For {id}!")

@client.command()
async def unban(ctx, id: int):
    data = {"dataSource": "Cluster0", "database": "CrownStudios", "collection": "BANS", "filter": {}, "update": {"$pull": {"bans": id}}}

    try:
        r = requests.post(data_api, json=data, headers=header)
        await ctx.channel.send(f"Unbanned {id}!")
    except Exception as e:
        await ctx.channel.send(f"An error occured while unbanning {id}", e)




token = os.environ.get("TOKEN")
client.run(token)

