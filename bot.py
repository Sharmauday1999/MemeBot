# bot.py
import os
from db import addUser
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents = intents)


@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )



@client.event
async def on_member_join(member):
    addUser(member.id)

@client.event
async def on_message(message):
    up = '\N{THUMBS UP SIGN}'
    down = '\N{THUMBS DOWN SIGN}'

    print(message.channel.id)
    
    if message.channel.id == 836009066911629312 and len(message.attachments) > 0:
        await message.add_reaction(up)
        await message.add_reaction(down)
        await message.channel.send("JUDGEMENT TIME " + str(message.author.name))


client.run(TOKEN)

