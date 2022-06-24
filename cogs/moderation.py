import nextcord
from nextcord.ext import commands
import aiofiles
import datetime
import humanfriendly
import pymongo
from pymongo import MongoClient
import os

URL = os.environ.get('WARN_DATABASE_URL')
cluster = MongoClient(URL)
database = cluster["Miku"]
collection = database["Warns"]

class Moderation(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases=["WARN","Warn"]) 
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()    
    async def warn(self,ctx, member:nextcord.Member=None, *, reason=None):
        """Warns a member via dms"""
        id = member.id
        if collection.count_documents({"memberid":id}) == 0:
            collection.insert_one({"memberid":id,"warns": 0})

        warn_count = collection.find_one({"memberid":id})
        count = warn_count["warns"]
        new_count = count + 1 
        collection.update_one({"memberid":id},{"$set":{"warns": new_count}})
        if member == None:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please mention a member to be warned!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
        elif member == ctx.author:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot warn yourself!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return        
        elif member.bot == True:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot warn a bot!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return                
        else:
            channel = self.client.get_channel(989460111984590848)
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"**ID:** {member.id}\n**Mention:** {member.mention}")
            em.set_author(name=f"{member.name} | Warn", icon_url= ctx.author.avatar)
            em.set_thumbnail(url=member.avatar.url)
            em.add_field(name=f"Moderator",value=ctx.author.mention, inline=False)
            em.add_field(name=f"Reason",value=reason, inline=False)
            em.timestamp=ctx.message.created_at

            warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Warned!**", color= nextcord.Color.red())
            warnEmbed.add_field(name="Reason", value=f"```{reason}```\n\nYou have a total of `{new_count}` warning(s).", inline= False)
            warnEmbed.set_thumbnail(url=ctx.guild.icon)
            warnEmbed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar)
            warnEmbed.timestamp=ctx.message.created_at 
            await member.send(embed=warnEmbed)             
            await ctx.message.delete()
            await channel.send(embed=em)
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} were successfully warned via DMs!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await ctx.send(embed=em) 
            return
    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to warn members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return         

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def warnings(self,ctx, member:nextcord.Member):
        """Checks number of warnings for a member"""
        id = member.id
        warn_count = collection.find_one({"memberid":id})
        count = warn_count["warns"]
        moderator = collection.find_one({"moderator":ctx.author.id})
        reason_all = collectionr.find_one({"memberid":id})
        reasons = reason_all["reason"]

        if member is None:
            await ctx.send("Please mention a member!")
            return
        elif member.bot == True:
            await ctx.send("It's a bot!")
            return
        else:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.add_field(name="Warnings", value= count) 
            await ctx.send(embed=em)    

    @commands.command(aliases=["KICK","Kick"]) 
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()    
    async def kick(self,ctx, member:nextcord.Member=None, *, reason=None):
        """Kicks a member"""
        id = member.id
        if collection.count_documents({"memberid":id}) == 0:
            collection.insert_one({"memberid":id,"warns": 0})

        warn_count = collection.find_one({"memberid":id})
        count = warn_count["warns"]        

        if member == None:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please mention a member to be kicked!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
        elif member == ctx.author:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot kick yourself!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return        
        elif member.bot == True:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot kick a bot!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return                
        else:
            channel = self.client.get_channel(989460111984590848)
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"**ID:** {member.id}\n**Mention:** {member.mention}")
            em.set_author(name=f"{member.name} | Kick", icon_url= ctx.author.avatar)
            em.set_thumbnail(url=member.avatar.url)
            em.add_field(name=f"Moderator",value=ctx.author.mention, inline=False)
            em.add_field(name=f"Reason",value=reason, inline=False)
            em.timestamp=ctx.message.created_at

            warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Kicked!**", color= nextcord.Color.red())
            warnEmbed.add_field(name="Reason", value=f"```{reason}```\n\nYou have a total of `{count}` warning(s).", inline= False)
            warnEmbed.set_thumbnail(url=ctx.guild.icon)
            warnEmbed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar)
            warnEmbed.timestamp=ctx.message.created_at 
            await member.send(embed=warnEmbed)             
            await ctx.message.delete()
            await member.kick(reason=reason)
            await channel.send(embed=em)
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} were successfully kicked!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await ctx.send(embed=em) 
            return
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to kick members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return                 

    @commands.command(aliases=["purge", "PURGE", "Purge", "CLEAR", "Clear"])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def clear(self, ctx, amount:int):
        """Deletes messages in bulk"""
        if amount <= 0:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please enter a positive number to clear messages!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)           
            return                      
        else:
            await ctx.channel.purge(limit = amount + 1) 
            return                 

    @commands.command(aliases=["BAN","Ban"]) 
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()    
    async def ban(self,ctx, member:nextcord.Member=None, *, reason=None):
        """Bans a member"""
        id = member.id
        if collection.count_documents({"memberid":id}) == 0:
            collection.insert_one({"memberid":id,"warns": 0})

        warn_count = collection.find_one({"memberid":id})
        count = warn_count["warns"]        

        if member == None:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please mention a member to be banned!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
        elif member == ctx.author:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot ban yourself!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return        
        elif member.bot == True:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot ban a bot!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return                
        else:
            channel = self.client.get_channel(989460111984590848)
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"**ID:** {member.id}\n**Mention:** {member.mention}")
            em.set_author(name=f"{member.name} | Ban", icon_url= ctx.author.avatar)
            em.set_thumbnail(url=member.avatar.url)
            em.add_field(name=f"Moderator",value=ctx.author.mention, inline=False)
            em.add_field(name=f"Reason",value=reason, inline=False)
            em.timestamp=ctx.message.created_at

            warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Banned!**", color= nextcord.Color.red())
            warnEmbed.add_field(name="Reason", value=f"```{reason}```\n\nYou have a total of `{count}` warning(s).", inline= False)
            warnEmbed.set_thumbnail(url=ctx.guild.icon)
            warnEmbed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar)
            warnEmbed.timestamp=ctx.message.created_at 
            await member.send(embed=warnEmbed)             
            await ctx.message.delete()
            await member.ban(reason=reason)
            await channel.send(embed=em)
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} were successfully Banned!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await ctx.send(embed=em) 
            return
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to ban members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return  
            
    @commands.command(aliases=["Unban", "UNBAN"])
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def unban(self, ctx, id:int, *, reason=None):
        """Unbans a banned member"""
        member = await self.client.fetch_user(id)        
        if member == None:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please mention a member to be unbanned!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
        elif member == ctx.author:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot unban yourself!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return        
        elif member.bot == True:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot unban a bot!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return                
        else:
            channel = self.client.get_channel(989460111984590848)
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"**ID:** {member.id}\n**Mention:** {member.mention}")
            em.set_author(name=f"{member.name} | Unban", icon_url= ctx.author.avatar)
            em.set_thumbnail(url=member.avatar.url)
            em.add_field(name=f"Moderator",value=ctx.author.mention, inline=False)
            em.add_field(name=f"Reason",value=reason, inline=False)
            em.timestamp=ctx.message.created_at

            warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Unbanned!**", color= nextcord.Color.green())
            warnEmbed.add_field(name="Reason", value=f"```{reason}```", inline= False)
            warnEmbed.set_thumbnail(url=ctx.guild.icon)
            warnEmbed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar)
            warnEmbed.timestamp=ctx.message.created_at 
            await member.send(embed=warnEmbed)             
            await ctx.message.delete()
            await ctx.guild.unban(member, reason=reason)
            await channel.send(embed=em)
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} were successfully Unbanned!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await ctx.send(embed=em) 
            return                    
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to unban members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return  

    @commands.command(aliases=["MUTE","Mute"]) 
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()    
    async def mute(self,ctx, member:nextcord.Member=None, time=None, *, reason=None):
        """Mutes a member"""
        id = member.id
        if collection.count_documents({"memberid":id}) == 0:
            collection.insert_one({"memberid":id,"warns": 0})

        warn_count = collection.find_one({"memberid":id})
        count = warn_count["warns"]     
        seconds = 0

        if time.lower().endswith("d"or"D"or"Days"or"DAYS"or"days"or"Day"or"day"or"DAY"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} days"
        if time.lower().endswith("h"or"H"or"Hours"or"hours"or"HOURS"or"hour"or"HOUR"or"Hour"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} hours"
        elif time.lower().endswith("m"or"M"or"Minutes"or"minutes"or"MINUTES"or"minute"or"Minute"or"MINUTE"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minutes"
        elif time.lower().endswith("s"or"S"or"Seconds"or"SECONDS"or"seconds"or"second"or"Second"or"SECOND"):
            seconds += int(time[:-1])
            counter = f"{seconds} seconds"
        if seconds <= 0:
            await ctx.message.delete()
            embed = nextcord.Embed(color=nextcord.Color.red())            
            embed.set_author(name=f"{ctx.author.name} Please mention a proper duration!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.send(embed=embed)
            return
        elif seconds > 7776000:
            await ctx.message.delete()
            embed = nextcord.Embed(color=nextcord.Color.red())            
            embed.set_author(name=f"{ctx.author.name} You have specified a too long duration!\nMaximum duration is 90 days!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")  
            await ctx.send(embed=embed)
            return 

        if member == None:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please mention a member to be muted!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
        elif member == ctx.author:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot mute yourself!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return        
        elif member.bot == True:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot mute a bot!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return                
        else:
            channel = self.client.get_channel(989460111984590848)
            em = nextcord.Embed(color=nextcord.Color.yellow(), description=f"**ID:** {member.id}\n**Mention:** {member.mention}")
            em.set_author(name=f"{member.name} | Mute", icon_url= ctx.author.avatar)
            em.set_thumbnail(url=member.avatar.url)
            em.add_field(name=f"Moderator",value=ctx.author.mention, inline=False)
            em.add_field(name=f"Reason",value=reason, inline=False)
            em.add_field(name=f"Duration",value=counter, inline=False)
            em.timestamp=ctx.message.created_at

            warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Muted!**", color= nextcord.Color.red())
            warnEmbed.add_field(name="Reason", value=f"```{reason}```", inline= False)
            warnEmbed.add_field(name="Duration", value=f"```{counter}```\n\nYou have a total of `{count}` warning(s).", inline= False)
            warnEmbed.set_thumbnail(url=ctx.guild.icon)
            warnEmbed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar)
            warnEmbed.timestamp=ctx.message.created_at 
            time = humanfriendly.parse_timespan(time)
            await member.send(embed=warnEmbed)             
            await ctx.message.delete()
            await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=seconds))
            await channel.send(embed=em)
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} were successfully Muted!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await ctx.send(embed=em) 
            return
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to mute members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return  

    @commands.command(aliases=["UNMUTE","Unmute"]) 
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()    
    async def unmute(self,ctx, member:nextcord.Member=None, *, reason=None):
        """Unmutes a member"""
        id = member.id
        if collection.count_documents({"memberid":id}) == 0:
            collection.insert_one({"memberid":id,"warns": 0})

        warn_count = collection.find_one({"memberid":id})
        count = warn_count["warns"]     

        if member == None:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please mention a member to be unmuted!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
        elif member == ctx.author:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot unmute yourself!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return        
        elif member.bot == True:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot unmute a bot!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return                
        else:
            channel = self.client.get_channel(989460111984590848)
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"**ID:** {member.id}\n**Mention:** {member.mention}")
            em.set_author(name=f"{member.name} | Unmute", icon_url= ctx.author.avatar)
            em.set_thumbnail(url=member.avatar.url)
            em.add_field(name=f"Moderator",value=ctx.author.mention, inline=False)
            em.add_field(name=f"Reason",value=reason, inline=False)
            em.timestamp=ctx.message.created_at

            warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Unmuted!**", color= nextcord.Color.green())
            warnEmbed.add_field(name="Reason", value=f"```{reason}```\n\nYou have a total of `{count}` warning(s).", inline= False)
            warnEmbed.set_thumbnail(url=ctx.guild.icon)
            warnEmbed.set_footer(text=f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar)
            warnEmbed.timestamp=ctx.message.created_at 
            await member.send(embed=warnEmbed)             
            await ctx.message.delete()
            await member.edit(timeout=None)
            await channel.send(embed=em)
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} were successfully Unmuted!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await ctx.send(embed=em) 
            return
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to unmute members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return  

def setup(client):
    client.add_cog(Moderation(client))        
    print("✅ | Moderation cog ready!")
    print("---------------------------")