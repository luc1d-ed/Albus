# smartbot.py
# added changes to remember the chat history
import os
import discord
import openai
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

# Set up the OpenAI API client
openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='`', intents=intents)

bot = commands.Bot(command_prefix="`", intents=intents)

chat_history = []
logged_in_user = None

# Add the previous message to the chat history
def add_chat_history(chat_history, message):
    chat_history.append(message)

    # Limit the chat history to the last 10 messages
    # You can make this longer but the prompt can only get so big until you get an error
    chat_history = chat_history[-10:]


# Formats the chat history for a prompt
def format_chat_history(chat_history):
    # Join the list of messages into a string
    formatted_chat_history = "\n".join(
        [f"{message.author}: {message.content}" for message in chat_history])

    return formatted_chat_history

# Formats a prompt for the response
# Use the chat history + the logged in history to set it up so it's easy to respond to. The
# Bot will have access to the previous 10 messages for context
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
    # Set the logged in user - I'm not sure the exact syntax here but copilot wrote it for me and it works
    global logged_in_user
    logged_in_user = client.user
    print('We have logged in as {0.user} in main \nReady to Rock and Roll!'.format(client))
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='for pings, I just wanna talk'))


@client.event
async def on_message(message):
    print("Message Received")

    add_chat_history(chat_history, message)

    # Only respond to messages from other users, not from the bot itself
    if message.author == client.user:
        return

    # Check if the bot is mentioned in the message
    if message.content.startswith(bot.command_prefix) or client.user in message.mentions:
        print(f"Responding to message: {message.content}")

        # Remove the bot prefix from the message content
        content = message.content.removeprefix(bot.command_prefix)

        # Generate Prompt
        prompt = generate_prompt(logged_in_user, chat_history)

        # Use the OpenAI API to generate a response to the message
        r = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            temperature=0.5,
        )
        print(r)


        # Clean up response and remove the bot prefix if it was added
        response = r.choices[0].text.strip() 
        if response.startswith(bot.command_prefix):
            response = response.removeprefix(bot.command_prefix)

        # Send the response as a message
        await message.channel.send(response)


# Start the bot
client.run(TOKEN)
