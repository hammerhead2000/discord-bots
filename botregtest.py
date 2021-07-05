from unittest import TestCase
import discord
import os

class TryTesting(TestCase):
    def test_bot_post(self):
            TOKEN = os.environ['DISCORDBOTTOKEN']
            client = discord.Client()

            @client.event
            async def on_ready():
                print('We have logged in as {0.user}'.format(client))
