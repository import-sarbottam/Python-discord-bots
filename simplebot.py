import os
import discord
import asyncio

token = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Succesfully logged in as {client.user}')

@client.event
async def on_member_join(member):
    guild = client.get_guild(873587798895124491) #add your guild id integer
    channel = guild.get_channel(873816838893600870) #add your guild channel integer where you want to make the bot say welcome
    await channel.send(f'Hello {member.mention} Welcome to {guild.name}')
    role = discord.utils.get(member.guild.roles, id=873766899215921183) #add your guild role integer
    await member.add_roles(role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('\hello'):
        await message.channel.send(f"Hello! {message.author.mention}") #returns this when someone says hello

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if payload.channel_id == 873862796469751818 and payload.message_id == 873868485359456266: #channel and message id in which the role assignment message is
        if str(payload.emoji) == '<:Valo:873865945351847967>':
            role = discord.utils.get(payload.member.guild.roles, id=873866385095270400)
            await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if payload.channel_id == 873862796469751818 and payload.message_id == 873868485359456266:
        if str(payload.emoji) == '<:Valo:873865945351847967>':
            role = discord.utils.get(guild.roles, id=873866385095270400)
            await member.remove_roles(role)

@client.event
async def on_member_remove(member):
    guild = client.get_guild(873587798895124491)
    channel = guild.get_channel(873816838893600870) #add your guild channel integer where you want to make the bot say goodbye
    await channel.send(f'{member.mention} has left {guild.name}')

client.run(token)