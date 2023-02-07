# GPT Discord Bot

This is not a ChatGPT. This bot uses the **text-davinci-003** library. 
* `!ask [message]` - interact with bot

# Setup

* [Install](#install)
  * [Create a Discord bot](#create-a-discord-bot)
  * [Create a OpenAI API key](#create-a-openai-api-key)

## Install

``` bash
git clone https://github.com/hurtnd/gpt-discord-bot
cd gpt-discord-bot
pip install -r requirements.txt
```
In `config.json` change the lines **PUT_HERE_YOUR_DISCORD_BOT_TOKEN** and **PUT_HERE_YOUR_OPENAI_KEY**

If you do not have a Discord bot and an OpenAI key, then I advise you to read the information about obtaining them below.

### Create a Discord bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications), sign in and click the **New Application** button
2. Enter a name for the bot, agree with terms and click **Create**
3. In the left column click on **Bot** and turn on **Message Content Intent**
4. Copy token and paste it into the `config.json` file
5. Go to the **OAuth2** tab, select **URL Generator** and select the parameters you need
6. Follow the generated link and select the server where the bot will be located

### Create a OpenAI API key

1. Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys) log in or sign up
2. Click **Create new secret key** and copy it
3. Paste the secret key into the `config.json` file
