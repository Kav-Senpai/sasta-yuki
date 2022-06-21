import nextcord
from nextcord.ext import commands
from nextcord import File, ButtonStyle
import datetime
from datetime import datetime
import asyncio
from nextcord.ui import Button, View
from nextcord.utils import get

class Utility(commands.Cog):
    """Utility Commands"""
    def __init__(self,client):
        self.client = client

    @commands.command(aliases=['Suggest','SUGGEST'])
    @commands.guild_only()
    async def suggest(self, ctx, *,suggestion):
        
        await ctx.message.delete()
        channel = self.client.get_channel(988729252528652308)
        log = self.client.get_channel(988719562402963456)

        Embed = nextcord.Embed(colour = nextcord.Color.blue(), title=f'{ctx.author.name} posted a suggestion!')
        Embed.set_author(name= ctx.guild.name, icon_url= ctx.guild.icon)
        Embed.add_field(name = 'Suggested in', value = ctx.message.channel.mention, inline=True)
        Embed.add_field(name = 'Suggestion', value= suggestion, inline=True)
        Embed.add_field(name = 'Suggester', value = ctx.author.mention, inline=True)
        Embed.set_thumbnail(url=ctx.author.avatar)
        Embed.timestamp = ctx.message.created_at      

        suggestEmbed = nextcord.Embed(colour = nextcord.Color.blue())
        suggestEmbed.set_author(name=f'Anonymous', icon_url = 'https://cdn.discordapp.com/attachments/961610704060829696/988710382484992080/y43mMnP.png')
        suggestEmbed.add_field(name = 'New suggestion!', value = f'{suggestion}')
        suggestEmbed.timestamp = ctx.message.created_at

        await log.send(embed=Embed)        
        msg = await channel.send(embed=suggestEmbed)
        await msg.add_reaction('<:Tick_yuki:981140827579502632>')
        await msg.add_reaction('<:Cross_yuki:981141014016307310>')    

    @commands.command(aliases = ["Reminder","REMINDER"])
    async def reminder(self, ctx, time=None, *, reminder=None):
        user = ctx.message.author
        embed = nextcord.Embed(color=nextcord.Color.red())
        seconds = 0
        if time.lower().endswith("d"or"D"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24}d"
        if time.lower().endswith("h"or"H"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60}m"
        elif time.lower().endswith("m"or"M"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60}m"
        elif time.lower().endswith("s"or"S"):
            seconds += int(time[:-1])
            counter = f"{seconds}s"
        if seconds <= 0:
            await ctx.message.delete()
            embed.set_author(name=f"{ctx.author.name} Please mention a proper duration!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
        elif seconds > 7776000:
            await ctx.message.delete()
            embed.set_author(name=f"{ctx.author.name} You have specified a too long duration!\nMaximum duration is 90 days!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
        else:
            await ctx.reply(f"Alright, I've successfully set your reminder.\nI will remind you in `{counter}`")
            await asyncio.sleep(seconds)
            await ctx.author.send(f"Heii {ctx.author.mention}, you asked me to remind you about **{reminder}** `{counter}` ago!")
            return
        await ctx.send(embed=embed)            

def setup(client):
    client.add_cog(Utility(client))        
    print("✅ | Utility cog ready!")
    print("---------------------------")        