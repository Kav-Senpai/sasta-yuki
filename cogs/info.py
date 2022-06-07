import nextcord
from nextcord.ext import commands
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View, Select
import time
import datetime
from datetime import datetime

class Information(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases=['av','AV','AVATAR','Avatar','Av'])
    async def avatar(self, ctx:commands.Context, *, member: nextcord.Member = None):
        if member==None:
            member = ctx.author

        button=Button(label="Avatar",url=member.display_avatar.url,style=ButtonStyle.link)
        view = View()
        view.add_item(button)

        icon_url = member.display_avatar
        avatarEmbed=nextcord.Embed(color=member.color)
        avatarEmbed.set_image(url=f"{icon_url}")
        avatarEmbed.set_author(name=f"{member.name}\'s Avatar", icon_url= member.display_avatar)
        avatarEmbed.timestamp=ctx.message.created_at 
       
        await ctx.send(embed=avatarEmbed,view=view) 

    @commands.command(aliases=["bn","BN","Bn","Banner","BANNER"])
    async def banner(self, ctx, user:nextcord.Member=None):
        if user == None:
            user = ctx.author
        req = await self.client.http.request(nextcord.http.Route("GET", "/users/{uid}", uid=user.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            button=Button(label="Banner",url=banner_url,style=ButtonStyle.link)
            view = View()
            view.add_item(button)            
            em = nextcord.Embed(color=user.color) 
            em.set_image(url=banner_url) 
            em.set_author(name=f"{user.name}\'s Banner", icon_url=user.display_avatar)  
            em.timestamp=ctx.message.created_at
            await ctx.send(embed=em, view=view)
            
    @commands.command(aliases=["PING","Ping"])
    async def ping(self,ctx):
        message = await ctx.send(f'Pinging..')
        await message.edit(f"🏓 **| Pong!**",embed= nextcord.Embed(description=f"```yaml\nLatency: {round(self.client.latency*1000)}ms\n```", color=nextcord.Color.blurple()))

    @commands.command(aliases=["UI","ui","Ui","Whois","WHOIS"])
    async def whois(self, ctx, *, user: nextcord.Member = None): # b'\xfc'
        if user is None:
            user = ctx.author
                
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = nextcord.Embed(color=user.color, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar.url)
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Join position", value=str(members.index(user)+1))
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.add_field(name='Top role', value=user.top_role.mention)
        embed.set_footer(text='ID: ' + str(user.id))
        embed.timestamp=ctx.message.created_at
        return await ctx.send(embed=embed)

    @commands.command()
    async def hmm(self,ctx):
        select = Select(
            options=[
                nextcord.SelectOption(label="hi",
                emoji="🏓",
                description="abba dabba jhappa",
                default=True),
                nextcord.SelectOption(label="bye",
                emoji="😀",
                description="hui hui")
            ]
        )        

        async def select_callback(self,interaction):
            await interaction.response.edit_message("hello")
        view = View()
        view.add_item(select)

        await ctx.send("Choose a Catgory",view=view)


def setup(client):
    client.add_cog(Information(client))        
    print("✅ | Info cog ready!")  
    print("---------------------------")          