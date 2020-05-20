import os
import random

import discord
from dotenv import load_dotenv

from roll import roll

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[0]+message.content[1] == '/r':
        amount, side, bonus = roll(message.content[3:])
        results = []
        for dice in range(amount):
            results.append(random.randint(1, side))
        response = "```@{} rolou {} com total {} ```".format(message.author.name, results, sum(results)+bonus)
        await message.channel.send(response)

client.run(TOKEN)
