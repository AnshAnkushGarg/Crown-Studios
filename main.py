import json
import discord
import os
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
from web_server import keep_alive
import random
import time


data_api = "https://ap-south-1.aws.data.mongodb-api.com/app/data-mahzb/endpoint/data/v1/action/updateOne"
api_key = os.environ.get("MONGO_KEY")
bans_id = "6640dd7a8e1d44b6e1654de4"
header = header = {"Content-Type": "application/ejson", "Accept": "application/json", "apiKey": api_key}

keep_alive()


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = commands.Bot(command_prefix="!",intents=intents)

def give_roles(players, disc_users):
    allotted_rolls = []
    if players < 5:
        raise Exception("Cannot have less than 5 players for mafia!")
        return
    elif players >= 7:
        mafias = 2
        villagers = players-5
    elif players >= 10:
        mafias = 3
        villagers = players-6
    else:
        mafias = 1
        villagers = players-4

    doctor_player = random.choice(disc_users)
    disc_users.remove(doctor_player)
    allotted_rolls.append([doctor_player, "Doctor"])

    detective_player = random.choice(disc_users)
    disc_users.remove(detective_player)
    allotted_rolls.append([detective_player], "Detective")
    
    jester_player = random.choice(disc_users)
    disc_users.remove(jester_player)
    allotted_rolls.append(jester_player, "Jester")

    mafias = random.sample(disc_users, mafias)
    for i in mafias:
        disc_users.remove(i)

    

    
    
    
        
        
@client.event()
async def on_ready():
    print("Bot is ready")


"""@client.command()
async def gameban(ctx, id: int):
    if id == 2959339599:
        await ctx.channel.send(f"Cannot ban {id} as he is the owner!")
        return
    data = {"dataSource": "Cluster0", "database": "CrownStudios", "collection": "BANS", "filter": {"_id": {"$oid": bans_id}}, "update": {"$push": {"bans": id}}}
    r = requests.post(data_api, json=data, headers=header)
    await ctx.channel.send(f"Sent Ban Request For {id}!")"""

"""@client.command()
async def unban(ctx, id: int):
    data = {"dataSource": "Cluster0", "database": "CrownStudios", "collection": "BANS", "filter": {}, "update": {"$pull": {"bans": id}}}

    try:
        r = requests.post(data_api, json=data, headers=header)
        await ctx.channel.send(f"Unbanned {id}!")
    except Exception as e:
        await ctx.channel.send(f"An error occured while unbanning {id}", e)"""


@client.command()
async def mafia(ctx):
    no_of_players = 0
    users = []
    button1 = discord.Ui.Button(label="Join!", style=discord.ButtonStyle.green)

    async def join_game(interaction):
        user = interaction.user
        no_of_players += 1
        if isinstance(user, discord.Member):
            users.append(user)

    button1.callback = join_game

    await ctx.channel.send(embed=discord.Embed(title=f"A game of Mafia is being hosted, Join Up Now!", description=f"Hosted by {ctx.author}"))
    time.sleep(20)
    await ctx.channel.delete(1)
    await ctx.channel.send(embed=discord.Embed(title=f"Check your DMS for the Roles!", description=f"Don't tell your role!"))
    give_roles(no_of_players, users)

@client.event
async def on_command_error(ctx, error):
    await ctx.channel.send(f"An error occured: {error}")


    
                                




token = os.environ.get("TOKEN")
client.run(token)

