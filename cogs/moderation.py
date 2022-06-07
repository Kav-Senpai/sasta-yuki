import nextcord
from nextcord.ext import commands
import aiofiles
import datetime
import humanfriendly

class Moderation(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases=["purge", "PURGE", "Purge", "CLEAR", "Clear"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount:int):
        if amount <= 0:
            em=nextcord.Embed(description=f"<a:S_Cross:963039895922814996> | {ctx.author.mention} Please enter a positive number!", color=0xFF6961)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=em, delete_after=5)       
            return          
        else:
            await ctx.channel.purge(limit = amount + 1) 
            return
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em=nextcord.Embed(description="**Usage** \n `s!clear <amount>`", color=0xFF6961)
            em.set_author(name="clear",icon_url=ctx.author.avatar)
            em.set_footer(text="Delete messages in bulk!")            
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=em)
            return
        if isinstance(error, commands.MissingPermissions):
            em=nextcord.Embed(description=f"<a:S_Cross:963039895922814996> | {ctx.author.mention} You don't have the permission to clear messages!", color=0xFF6961)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=em)
            return  

    @commands.command(aliases=["Warn", "WARN"])
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member:nextcord.Member=None, *, reason=None):

        if reason == None:
            return await ctx.send("please mention a reason!")
        if member == None:
            return await ctx.send("please mention a user!")        

        warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Warned!**", color= 0xff6961)
        warnEmbed.add_field(name="Moderator", value=f"{ctx.author.mention}", inline= False)
        warnEmbed.add_field(name="Reason", value=reason, inline= False)
        warnEmbed.set_thumbnail(url=ctx.guild.icon)
        warnEmbed.timestamp=ctx.message.created_at 
        await ctx.send(embed=warnEmbed)           



def setup(client):
    client.add_cog(Moderation(client))        
    print("✅ | Moderation cog ready!")
    print("---------------------------")