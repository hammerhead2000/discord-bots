import discord

TOKEN = "ODYxNjMyMDk3Nzk3MDEzNTM0.YOMnbA.r43o6DilWqEFRlwZd8-rsY6OGAU"

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
