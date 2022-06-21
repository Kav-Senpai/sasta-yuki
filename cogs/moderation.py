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
collectionr = database["Reasons"]

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
        if collectionr.count_documents({"memberid":id}) == 0:
            collectionr.insert_one({"moderator":ctx.author.id, "memberid":id, "reason": reason})

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
            warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Warned!**", color= nextcord.Color.red())
            warnEmbed.add_field(name="Reason", value=f"```{reason}```\n\nYou have a total of `{new_count}` warning(s).", inline= False)
            warnEmbed.set_thumbnail(url=ctx.guild.icon)
            warnEmbed.set_footer(f"Moderator: {ctx.author.name}", icon_url=ctx.author.avatar)
            warnEmbed.timestamp=ctx.message.created_at 
            await member.send(embed=warnEmbed)             
            await ctx.message.delete()
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} were successfully warned via DMs!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await ctx.send(embed=em) 
            return

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to warn members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.channel.purge(limit=1)
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
            em = nextcord.Embed(color=nextcord.Color.red(), title=f"Displaying warnings for {member.name}")
            em.add_field(name="Warnings", value= count) 
            em.add_field(name="Latest Reason", value=reasons)   
            await ctx.send(embed=em)    

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

    @commands.command(aliases=["Kick","KICK"])
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:nextcord.Member, *, reason=None):
        """Kick a member"""
        em=nextcord.Embed(color=nextcord.Color.red())
        em.set_author(name=f"You cannot kick yourself!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
        if member == ctx.author:
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
        elif member.bot == True:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot kick a bot!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)    
            return
        elif member == None:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please mention a member to be kicked!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return            
        else:
            kickEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Kicked!**", color= nextcord.Color.red())
            kickEmbed.add_field(name="Moderator", value=f"{ctx.author.mention}", inline= False)
            kickEmbed.add_field(name="Reason", value=reason, inline= False)
            kickEmbed.set_thumbnail(url=ctx.guild.icon)
            kickEmbed.timestamp=ctx.message.created_at 
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} was successfully kicked!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await member.kick(reason=reason)            
            await member.send(embed=kickEmbed)
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to kick members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=em)
            return 

    @commands.command(aliases=["Ban","BAN"])
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:nextcord.Member, *, reason=None):
        """Ban a member"""
        em=nextcord.Embed(color=nextcord.Color.red())
        em.set_author(name=f"You cannot ban yourself!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
        if member == ctx.author:
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
        elif member.bot == True:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"You cannot ban a bot!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)    
            return
        elif member == None:
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"Please mention a member to be banned!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.message.delete()
            await ctx.send(embed=em)
            return            
        else:
            kickEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Banned!**", color= nextcord.Color.red())
            kickEmbed.add_field(name="Moderator", value=f"{ctx.author.mention}", inline= False)
            kickEmbed.add_field(name="Reason", value=reason, inline= False)
            kickEmbed.set_thumbnail(url=ctx.guild.icon)
            kickEmbed.timestamp=ctx.message.created_at 
            em = nextcord.Embed(color=nextcord.Color.green())
            em.set_author(name=f"{member.name} was successfully banned!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
            await member.ban(reason=reason)            
            await member.send(embed=kickEmbed)
            await ctx.message.delete()
            await ctx.send(embed=em)
            return
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name} you don't have the permission to ban members!", icon_url="https://cdn.discordapp.com/emojis/963039895922814996.gif?v=1")
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=em)
            return 

def setup(client):
    client.add_cog(Moderation(client))        
    print("✅ | Moderation cog ready!")
    print("---------------------------")