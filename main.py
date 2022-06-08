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
import datetime
import humanfriendly
from random import choice
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View
from dotenv import load_dotenv

load_dotenv()
intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
prefix = [".",". "]
client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=f".help | Snowy"))
    print("Miku is online!")     

    #await ctx.send("This is a message", delete_after=5) # deletes message after 5 seconds

@client.event
async def on_member_join(member):
    await client.get_channel(944570768363245571).send(f"{member.mention} has joined the server!")

#Moderation Commands                   

@client.command(aliases=["MUTE","Mute"])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member:nextcord.Member, time, *, reason=None):
    time= humanfriendly.parse_timespan(time)
    muteEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Muted!**", color= 0xff6961)
    muteEmbed.add_field(name="Moderator", value=f"{ctx.author.mention}", inline= False)
    muteEmbed.add_field(name="Reason", value=reason, inline= False)
    muteEmbed.add_field(name="Time", value=f"{time}secs", inline= False)
    muteEmbed.set_thumbnail(url=ctx.guild.icon)
    muteEmbed.timestamp=ctx.message.created_at 
    embed=nextcord.Embed(description=f"<a:S_Tick:963039878373842965> | {member.mention} has been muted!", color=0x77DD77)
    if member.bot == True:
        em=nextcord.Embed(description=f"<a:S_Cross:963039895922814996> | {ctx.author.mention} You cannot mute a bot!", color=0xFF6961)
        await ctx.send(embed=em)
        return
    if member == ctx.author:
        em=nextcord.Embed(description=f"<a:S_Cross:963039895922814996> | {ctx.author.mention} You cannot mute yourself!", color=0xFF6961)
        await ctx.send("You cannot mute yourself!")
        return
    else:        
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        await ctx.channel.purge(limit=1)
        await member.send(embed=muteEmbed)
        await ctx.send(embed=embed)
        return
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        em=nextcord.Embed(title="Usage",description="`s!mute <mention/id> <time> [reason]`", color=0xFF6961)
        em.set_author(name="mute", icon_url=ctx.author.avatar)
        em.set_footer(text="Mute someone from the server!")
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=em)
        return           
    if isinstance(error, commands.MissingPermissions):
        em=nextcord.Embed(description=f"<a:S_Cross:963039895922814996> | {ctx.author.mention} You don't have the permission to mute members!", color=0xFF6961)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=em)
        return     


@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member:nextcord.Member, *, reason=None):
    unmuteEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_Tick:963039878373842965> **You got Unmuted!**", color= 0x77DD77)
    unmuteEmbed.add_field(name="Moderator", value=f"{ctx.author.mention}", inline= False)
    unmuteEmbed.add_field(name="Reason", value=reason, inline= False)
    unmuteEmbed.set_thumbnail(url=ctx.guild.icon)
    unmuteEmbed.timestamp=ctx.message.created_at 
    embed=nextcord.Embed(description=f"<a:S_Tick:963039878373842965> | {member.mention} has been unmuted!", color=0x77DD77)
    if member.bot == True:
        em=nextcord.Embed(description=f"<a:S_Cross:963039895922814996> | {ctx.author.mention} You cannot unmute a bot!", color=0xFF6961)
        await ctx.send(embed=em)
        return
    if member == ctx.author:
        em=nextcord.Embed(description=f"<a:S_Cross:963039895922814996> | {ctx.author.mention} You cannot unmute yourself!", color=0xFF6961)
        await ctx.send("You cannot mute yourself!")
        return
    if member.timeout == None:
        await ctx.send("member is not muted")   
    else:        
        await member.edit(timeout=None)
        await member.send(embed=unmuteEmbed)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)   
  

@client.command()
async def timer(ctx, seconds):
        secondint = int(seconds)
        if secondint > 86400:
            await ctx.channel.purge(limit=1)
            await ctx.send(f"<a:S_CrossTimer:963025312961134642> | My limit is 24 hours!", delete_after=5)
            raise BaseException
        if secondint <= 0:
            await ctx.channel.purge(limit=1)
            await ctx.send(f"<a:S_CrossTimer:963025312961134642> | Please enter a positive number!", delete_after=5)
            raise BaseException
        em = nextcord.Embed(color=ctx.author.color)
        em.set_author(name=f"{ctx.author.name}'s timer: {seconds}secs", icon_url="https://cdn.discordapp.com/emojis/771644894149607424.gif?v=1")
        message = await ctx.send(embed=em)

        while True:
            secondint -= 1
            if secondint == 0:
                em = nextcord.Embed(title="Ended!", color=ctx.author.color)
                em.set_footer(text=f"Time ended after {seconds}secs")
                await message.edit(embed=em)
                break
            em = nextcord.Embed(color=ctx.author.color)
            em.set_author(name=f"{ctx.author.name}'s timer: {secondint}secs", icon_url="https://cdn.discordapp.com/emojis/771644894149607424.gif?v=1")    
            await message.edit(embed=em)
            await asyncio.sleep(1) 
        await message.reply(f"<a:S_TickTimer:963025090365255720> | {ctx.author.mention} Your timer has ended!")
@timer.error
async def timer_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"<a:S_CrossTimer:963025312961134642> | Please enter a number!", delete_after=5)                               

@client.command()
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

#=============================================================================================================================
                                                         #EVENTS
#=============================================================================================================================
                                           

extensions = [
    'cogs.logs',
    'cogs.anime',
    'cogs.vc',
    'cogs.moderation',
    'cogs.fun',
    'cogs.info',
    'cogs.admin',
    'cogs.buttontest',
    'cogs.economy',
    'cogs.errors',
    'cogs.embed',
    'cogs.colors'
    
    ]
if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f"Error loading {extension}", file=sys.stderr)
            traceback.print_exc()  

client.run(os.getenv("TOKEN"))
