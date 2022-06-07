import nextcord
from nextcord.ext import commands
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View

class ButtonRoles(commands.Cog):
    """Roles"""
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def hi(self,ctx):
        button1 = Button(label="Black", style=ButtonStyle.blurple, emoji="⚫")
        button2 = Button(label="White", style=ButtonStyle.blurple, emoji="⚪")    
        async def button1_callback(interaction):
            role = nextcord.utils.get(ctx.guild.roles, id=972318238274879528)
            mrole = nextcord.utils.get(ctx.guild.roles, id=972318240044883978)
            if role in interaction.user.roles:
                await interaction.response.send_message(f"{role.mention} removed", ephemeral=True)
                await interaction.user.remove_roles(role)   
            elif mrole in interaction.user.roles:
                await interaction.response.send_message(f"Please remove the previous color before choosing a new color", ephemeral=True)     
            else:
                await interaction.response.send_message(f"{role.mention} given", ephemeral=True) 
                await interaction.user.add_roles(role)
        async def button2_callback(interaction):
            mrole = nextcord.utils.get(ctx.guild.roles, id=972318238274879528)
            role = nextcord.utils.get(ctx.guild.roles, id=972318240044883978)
            if role in interaction.user.roles:
                await interaction.response.send_message(f"{role.mention} removed", ephemeral=True)
                await interaction.user.remove_roles(role)
            elif mrole in interaction.user.roles:
                await interaction.response.send_message(f"Please remove the previous color before choosing a new color", ephemeral=True)                    
            else:
                await interaction.response.send_message(f"{role.mention} given", ephemeral=True) 
                await interaction.user.add_roles(role)   

        button1.callback = button1_callback
        button2.callback = button2_callback
            
        view = View(timeout=None)
        view.add_item(button1) 
        view.add_item(button2)

        await ctx.send(f"Take a color!",view=view)

def setup(client):
    client.add_cog(ButtonRoles(client))        
    print("✅ | ButtonRoles cog ready!")
    print("---------------------------")