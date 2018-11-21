import discord
from discord.ext import commands

token = open("clientToken.txt","r").read()

client = commands.Bot(command_prefix = "--") #change the prefix according to your needs
min_req = 10     #mimimum number of reactions required to pin message

@client.event  # event decorator/wrapper
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    channel = message.channel
    print(f"{message.author}: {message.author.name}: {message.content}")
    if len(message.attachments) != 0:
        print("attachment found!")
        await client.add_reaction(message, '\U0001F493')

    if message.content.lower() == "zzz":
        await client.send_message(channel, "off to sleep :sleeping:")
        await client.logout()
    
    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    if reaction.emoji == "💓":
        emoji_users = await client.get_reaction_users(reaction, limit = min_req)
        if len(emoji_users) >= min_req:
            print("Ready to pin")
            await client.pin_message(reaction.message)

client.run(token)