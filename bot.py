import discord
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$prompt'):
        cliento = OpenAI()

        completion = cliento.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "developer", "content": "Your name is trivia monster. Your replies are terse and you speak like a pirate."},
                {   
                    "role": "user",
                    "content": message.content
                }
            ]
        )
        await message.channel.send(completion.choices[0].message.content)


client.run(discord_bot_token)