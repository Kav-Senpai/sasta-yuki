import nextcord
from nextcord.ext import commands
import random
import os
import traceback
import asyncio
from nextcord.utils import get
import schedule
import sys
import time
import requests
import datetime
import humanfriendly
import asyncpg
from random import choice
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View
from dotenv import load_dotenv

load_dotenv()
intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
prefix = ['. ','.']
client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=f".help | Snowy"))
    print("Miku is online!")     

for fn in os.listdir("./cogs"):
    if fn.endswith('.py'):
        client.load_extension(f"cogs.{fn[:-3]}")

    #await ctx.send("This is a message", delete_after=5) # deletes message after 5 seconds

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Successfully loaded {extension}!")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Successfully unloaded {extension}!")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Successfully reloaded {extension}!")    

#TEST
@client.event
async def on_member_join(member):
    await client.get_channel(944570768363245571).send(f"{member.mention} has joined the server!")                           

@client.command()
@commands.has_permissions(administrator=True)
async def toggle(ctx, *, command):
    command = client.get_command(command)
    if command == None:
        await ctx.send("Couldn't find that command!")
    elif ctx.command == command:
        await ctx.send("You cannot disable this command!")
    else:
        command.enabled = not command.enabled
        ternary = "enabled" if command.enabled else "disabled"
        await ctx.send(f"command {command.qualified_name} has been {ternary}!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.DisabledCommand):
        await ctx.send("Command is disabled ._.")
        return          

client.run(os.getenv("TOKEN"))