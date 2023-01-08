import random
import discord
import os
from megahal import *
from dotenv import load_dotenv


def connect():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        reply = await chat(str(message))
        await message.channel.send(reply)

    client.run(TOKEN)


def count_lines():
    with open('pegida_korpus.txt', encoding='UTF-8', errors='ignore') as trainingfile:
        for count, line in enumerate(trainingfile):
            pass
        print('Number of lines in your file:', count + 1)


def learn():
    megahal = MegaHAL()
    with open('pegida_korpus_small.txt', encoding='UTF-8', errors='ignore') as trainingfile:
        current_line = 0
        while True:
            current_line += 1
            line_content = trainingfile.readline()
            print(current_line, line_content)
            megahal.learn(line_content)
            megahal.close()
            megahal = MegaHAL()
            if not line_content:
                break
        trainingfile.close()


async def chat(message):
    megahal = MegaHAL()
    while True:
        reply = megahal.get_reply(message)
        print(reply)
        return reply


async def train():
    megahal = MegaHAL()
    megahal.train('')  # make sure your file doesn't include "'", as that breaks it


if __name__ == '__main__':
    connect()
    # count_lines()
    # chat()
    # learn()
    # train()
