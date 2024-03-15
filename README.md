# Albus
Discord Chat bot using Open AI API

This repository contains code for a Discord chat bot that utilizes the OpenAI API for generating responses. The bot is built using Python and can be integrated into your Discord server to provide automated responses based on the conversations happening in the server.

## Setup Instructions

To get the bot up and running, follow these steps:

### 1. Get Discord Bot Token

You'll need to create a Discord application and generate a bot token. Here's how:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give your application a name.
3. Go to the "Bot" tab and click "Add Bot".
4. Click on "Copy" under the token section to copy your bot token.

### 2. Get OpenAI API Key

You'll also need an API key from OpenAI to use their API. Follow these steps:

1. Sign up or log in to your OpenAI account on the [OpenAI website](https://openai.com/).
2. Once logged in, navigate to the API section.
3. Create a new API key if you haven't already.
4. Copy your API key.

### 3. Configure the Bot

1. Clone this repository to your local machine.
2. Navigate to the directory where the repository is cloned.
3. Create a file named `.env` in the root directory of the project.
4. Add the following lines to the `.env` file:

```
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

Replace `YOUR_DISCORD_BOT_TOKEN` with the token you obtained from the Discord Developer Portal, and `YOUR_OPENAI_API_KEY` with the API key you obtained from OpenAI.

### 4. Install Dependencies

Before running the bot, you'll need to install the necessary dependencies. Run the following command in your terminal (In the working directory):

```
pip install -r requirements.txt
```


### 5. Run the Bot

Once you've completed the above steps, you can start the bot by running the following command:

```
python bot.py
```


Your bot should now be up and running, and you can invite it to your Discord server using the bot invite link provided in the Discord Developer Portal.

## Usage

Once the bot is added to your Discord server and running, you can interact with it using a fixed prefix followed by your message. The prefix is set to '`', and you can use it to invoke the bot.

For example, to interact with the bot, type the following in any text channel where the bot is present:

```
`[your question]
```
(Remember to not add any space after the prefix.)


Replace `<your question>` with the actual question you want to ask the bot.

The bot will then process your question using the OpenAI API and respond accordingly based on the conversation context.

Enjoy chatting with your new Discord bot powered by OpenAI! If you have any questions or encounter any issues, feel free to open an issue in this repository.
