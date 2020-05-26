import discord
from config import TOKEN

client = discord.Client()

@client.event
async def on_ready(self):
    print('Logged on as', self.user)

@client.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

client.run(TOKEN)