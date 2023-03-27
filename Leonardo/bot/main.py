import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TARGET_CHANNEL_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(command_prefix='!', intents=intents)
openai.api_key = OPENAI_API_KEY


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    # Ignore messags sent by the bot itself
    if message.author == client.user:
        return

    prompt = os.getenv("PROMPT")

    if message.channel.id == int(TARGET_CHANNEL_ID):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "system", "content": prompt}, {"role": "user", "content": message.content}], temperature=0.2, max_tokens=400)

        await message.channel.send(gpt_response.choices[0].message.content)


client.run(TOKEN)
