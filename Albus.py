import os
import discord
import openai
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='`', intents=intents)

bot = commands.Bot(command_prefix="`", intents=intents)

chat_history = []
logged_in_user = None

def add_chat_history(chat_history, message):
    chat_history.append(message)

    chat_history = chat_history[-10:]


def format_chat_history(chat_history):
    formatted_chat_history = "\n".join(
        [f"{message.author}: {message.content}" for message in chat_history])

    return formatted_chat_history

def generate_prompt(logged_in_user, chat_history):
    prompt = f"""
    # Instructions
    You are a chatbot on Discord. Your username is '{logged_in_user}'. Respond to the following conversation in the most helpful way possible. You are funny and irreverant and you like to make people laugh. Use the vocabulary and writing style of a high schooler.

    # Converations
    {format_chat_history(chat_history)}
    {logged_in_user}:"""

    return prompt

@client.event
async def on_ready():
    global logged_in_user
    logged_in_user = client.user
    print('We have logged in as {0.user} in main \nReady to Rock and Roll!'.format(client))
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='for pings, I just wanna talk'))


@client.event
async def on_message(message):
    print("Message Received")

    add_chat_history(chat_history, message)

    if message.author == client.user:
        return

    if message.content.startswith(bot.command_prefix) or client.user in message.mentions:
        print(f"Responding to message: {message.content}")

        content = message.content.removeprefix(bot.command_prefix)

        prompt = generate_prompt(logged_in_user, chat_history)

        r = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            temperature=0.5,
        )
        print(r)


        response = r.choices[0].text.strip() 
        if response.startswith(bot.command_prefix):
            response = response.removeprefix(bot.command_prefix)

        await message.channel.send(response)


client.run(TOKEN)
