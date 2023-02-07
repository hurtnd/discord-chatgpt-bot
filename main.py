import json
import openai
import discord

intents = discord.Intents.all()

file = open('config.json', 'r')
config = json.load(file)

openai.api_key = config['openai_key']


class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!ask"):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=message.content,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            ).choices[0].text

            await message.channel.send(response)


client = MyBot(intents=intents)
client.run(config['discord_bot_token'])
