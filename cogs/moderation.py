import nextcord
from nextcord.ext import commands
import aiofiles
import datetime
import humanfriendly

class Moderation(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.client.warnings = {}

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.client.guilds:
            async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
                pass

            self.client.warnings[guild.id] = {}

        for guild in self.client.guilds:
            async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
                lines = await file.readlines()

                for line in lines:
                    data = line.split(" ")
                    member_id = int(data[0])
                    admin_id = int(data[1])
                    reason = " ".join(data[2:]).strip("\n")

                    try:
                        self.client.warnings[guild.id][member_id][0] += 1
                        self.client.warnings[guild.id][member_id][1].append(admin_id, reason)
                    except KeyError:
                        self.client.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]             
      
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        self.client.warnings[guild.id] = {}

    @commands.command(aliases=["WARN","Warn"]) 
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()    
    async def warn(self,ctx, member:nextcord.Member=None, *, reason=None):
        """Warns a member via dms"""
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
        try:
            first_warning = False
            self.client.warnings[ctx.guild.id][member.id][0] += 1
            self.client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

        except KeyError:
            first_warning = True
            self.client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]               

        count = self.client.warnings[ctx.guild.id][member.id][0]

        async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
            await file.write(f"{member.id} {ctx.author.id} {reason} \n")

        warnEmbed=nextcord.Embed(title=ctx.guild.name, description="<a:S_warn:951397930961633291> **You got Warned!**", color= nextcord.Color.red())
        warnEmbed.add_field(name="Moderator", value=f"{ctx.author.mention}", inline= False)
        warnEmbed.add_field(name="Reason", value=reason, inline= False)
        warnEmbed.add_field(name="Total Warnings", value=count, inline= False)        
        warnEmbed.set_thumbnail(url=ctx.guild.icon)
        warnEmbed.timestamp=ctx.message.created_at 
        await member.send(embed=warnEmbed)             
        await ctx.message.delete()
        em = nextcord.Embed(color=nextcord.Color.green())
        em.set_author(name=f"{member.name} was successfully warned via DMs!", icon_url="https://cdn.discordapp.com/emojis/963039878373842965.gif?v=1")
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
        if member is None:
            await ctx.send("Please mention a member!")
            return
        em = nextcord.Embed(title=f"Displaying Warnings for {member.name}", description="", color=nextcord.Color.red())
        try:
            i = 1
            for admin_id, reason in self.client.warnings[ctx.guild.id][member.id][1]:
                admin = ctx.guild.get_member(admin_id) 
                em.description += f"**Warnings {i}** given by {admin.mention} for: *`{reason}`*.\n"
                i += 1

            await ctx.send(embed=em)
        except KeyError:
            await ctx.send("This user has no warnings!")                  

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