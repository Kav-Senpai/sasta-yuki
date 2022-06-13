import nextcord
from nextcord.ext import commands
import random
import time
import datetime
import json
from datetime import date, timedelta
from datetime import datetime
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View

class Logs(commands.Cog):

    def __init__(self,client):
        self.client = client
  
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.client.get_channel(966222814564741170)
        em = nextcord.Embed(color=nextcord.Color.red())
        em.set_author(name="Message Deleted!",icon_url=message.author.avatar)
        em.add_field(name="User Info", value=f"**Name:** {message.author.name}#{message.author.discriminator} \n **Mention:** {message.author.mention} \n **ID:** {message.author.id}", inline=True)
        em.add_field(name="Channel Info", value=f"**Name:** #{message.channel.name} \n **Mention:** {message.channel.mention} \n **ID:** {message.channel.id}", inline=True)
        em.add_field(name=f"Timestamp", value=f"<t:{int(time.time())}>",inline=False    )
        em.add_field(name="Message", value=f"{message.content}", inline=False)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/961610704060829696/966283755847319582/deleted.png")
        em.timestamp=message.created_at 
        await channel.send(embed=em)   

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        channel = self.client.get_channel(966222814564741170)
        em = nextcord.Embed(color=nextcord.Color.blue())
        em.set_author(name="Message Edited!",icon_url=message_before.author.avatar)
        em.add_field(name="User Info", value=f"**Name:** {message_after.author.name}#{message_after.author.discriminator} \n **Mention:** {message_after.author.mention} \n **ID:** {message_after.author.id}", inline=True)
        em.add_field(name="Channel Info", value=f"**Name:** #{message_after.channel.name} \n **Mention:** {message_after.channel.mention} \n **ID:** {message_after.channel.id}", inline=True)
        em.add_field(name="Before", value=f"{message_before.content}", inline=False)
        em.add_field(name="After", value=f"{message_after.content}", inline=False)        
        em.add_field(name=f"Edited at", value=f"<t:{int(time.time())}>", inline=False)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/961610704060829696/976017387071631380/pencil.png")
        em.timestamp=message_after.created_at 
        button = Button(label="Jump to Message", style=ButtonStyle.link, url=f'https://discordapp.com/channels/{message_before.guild.id}/{message_before.channel.id}/{message_after.id}')
        view = View()
        view.add_item(button)
        await channel.send(embed=em,view=view)           

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = self.client.get_channel(947771959926747146)
        colors = self.client.get_channel(955357785053360128)
        rules = self.client.get_channel(947512003969314857)
        cmap = self.client.get_channel(947771959087861760)
        info = self.client.get_channel(955447455971938314)
        await info.send(f"{member.mention}", delete_after=0.10)        
        await rules.send(f"{member.mention}", delete_after=0.10)
        await cmap.send(f"{member.mention}", delete_after=0.10)        
        await role.send(f"{member.mention}", delete_after=0.10)
        await colors.send(f"{member.mention}", delete_after=0.10)
         

def setup(client):
    client.add_cog(Logs(client))        
    print("✅ | Logs cog ready!")  
    print("---------------------------")      