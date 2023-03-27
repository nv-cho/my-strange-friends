import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)
desired_channel_id = os.getenv('CHANNEL_ID')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    # Ignore messags sent by the bot itself
    if message.author == client.user:
        return

    if message.channel.id == desired_channel_id:
        await message.channel.send('Hello!')

client.run(TOKEN)
