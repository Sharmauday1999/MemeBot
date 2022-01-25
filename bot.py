# bot.py
import os
import db
import discord
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_CHANNEL_ID')

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
    db.addUser(member.id)

@client.event
async def on_message(message):
    up = '\N{THUMBS UP SIGN}'
    down = '\N{THUMBS DOWN SIGN}'

    if str(message.channel.id) == CHANNEL and len(message.attachments) > 0:
        db.createNewImage(message)
        await message.add_reaction(up)
        await message.add_reaction(down)
        await message.channel.send("JUDGEMENT TIME " + str(message.author.name))

    if message.content == "!MEME score":
        currScores = db.getCurrentScores()

        table = [['Name', 'Score']]
        results = []        


        for each in currScores:
            user = await client.fetch_user(int(each['discord_id']))
            results.append([user.display_name, each['score']])
        
        results.sort(key = lambda x:x[1], reverse = True)

        table = table + results

        await message.channel.send("```" + tabulate(table, headers = 'firstrow') + "```")

@client.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == '👍':
        db.addScore(payload.message_id)
    elif str(payload.emoji) == '👎':
        db.removeScore(payload.message_id)

@client.event
async def on_raw_reaction_remove(payload):
    if str(payload.emoji) == '👍':
        db.removeScore(payload.message_id)
    elif str(payload.emoji) == '👎':
        db.addScore(payload.message_id)

    
client.run(TOKEN)

