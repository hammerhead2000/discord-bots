import discord
import os

TOKEN = os.environ['DISCORDBOTTOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print('Message: {0.content}.  Room: {0.channel}'.format(message))
    if message.author == client.user:
        return

    await message.channel.send('I read you loud and clear')

client.run(TOKEN)
