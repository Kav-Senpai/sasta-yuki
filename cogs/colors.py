import nextcord
from nextcord.ext import commands
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View

class Color(commands.Cog):
    """Roles"""
    def __init__(self,client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def colors(self, ctx):

        Iembed = nextcord.Embed(title="Pick your shades*!*", description="You are allowed to take just one color at a time. \n `To change your color don't forget to remove the previous reaction before reacting to a new color`", color= 0x313131)
        Bembed = nextcord.Embed(description= "<:Blue:955095612238479380> ➺ <@&951818465361166397> \n <:LightBlue:955095612397854790> ➺ <@&951818574270459924> \n <:Crystal:955095612016169011> ➺ <@&951818617283018773>", color=0xAEC6CF)
        Gembed = nextcord.Embed(description= "<:Green:955095612284624976> ➺ <@&951819847904407582> \n <:LightGreen:955095612150403092> ➺ <@&951819913222295582> \n <:AppleMint:955095612192354364> ➺ <@&951820052418691133>", color=0x77DD77)
        Rembed = nextcord.Embed(description= "<:Red:955095612158775326> ➺ <@&951820397584711710> \n <:LightRed:955095612263637002> ➺ <@&951820501628649492> \n <:Melon:955095612284604436> ➺ <@&951820571874824242>", color=0xff6961)
        Yembed = nextcord.Embed(description= "<:Yellow:955095612183961680> ➺ <@&951821056837038131> \n <:LightYellow:955095612158800002> ➺ <@&951821138441437234> \n <:LemonChiffon:955095612146217040> ➺ <@&951821192094949396>", color=0xFDFD96)
        Pembed = nextcord.Embed(description= "<:Purple:955095612288815164> ➺ <@&951821433829466193> \n <:LightPurple:955095612095877181> ➺ <@&951821498224635954> \n <:Amethyst:955095612158783530> ➺ <@&951821583004074035>", color=0xC3B1E1)
        Piembed = nextcord.Embed(description= "<:Pink:955095612020359229> ➺ <@&951821970079645756> \n <:LightPink:955095611793874995> ➺ <@&951822022290329640> \n <:PalePink:955095612129415228> ➺ <@&951822322409541662>", color=0xF8C8DC)
        Blembed = nextcord.Embed(description= "<:Black:955095611852599297> ➺ <@&951837472764100691> \n <:Gray:955095612100075540> ➺ <@&951837699264901120> \n <:White:955095047446085653> ➺ <@&951837833927225404>", color=0xffffff)


        black = Button(label="Black", style=ButtonStyle.blurple, emoji="⚫")
        gray = Button(label="Gray", style=ButtonStyle.blurple, emoji="🛒")
        white = Button(label="White", style=ButtonStyle.blurple, emoji="⚪")    
        
        async def black_callback(interaction):
            black = nextcord.utils.get(ctx.guild.roles, id=951837472764100691)
            white = nextcord.utils.get(ctx.guild.roles, id=951837833927225404)
            gray = nextcord.utils.get(ctx.guild.roles, id=951837699264901120)
            if black in interaction.user.roles:
                await interaction.user.remove_roles(black)                  
                await interaction.response.send_message(f"{black.mention} removed", ephemeral=True) 
            elif white in interaction.user.roles:
                await interaction.response.send_message(f"Please remove the previous color before choosing a new color", ephemeral=True)     
            elif gray in interaction.user.roles:
                await interaction.response.send_message(f"Please remove the previous color before choosing a new color", ephemeral=True)                                    
            else:
                await interaction.user.add_roles(black)                
                await interaction.response.send_message(f"{black.mention} given", ephemeral=True) 
        async def gray_callback(interaction):
            black = nextcord.utils.get(ctx.guild.roles, id=951837472764100691)
            white = nextcord.utils.get(ctx.guild.roles, id=951837833927225404)
            gray = nextcord.utils.get(ctx.guild.roles, id=951837699264901120)
            if gray in interaction.user.roles:
                await interaction.user.remove_roles(gray)                 
                await interaction.response.send_message(f"{gray.mention} removed", ephemeral=True)  
            elif white in interaction.user.roles:
                await interaction.response.send_message(f"Please remove the previous color before choosing a new color", ephemeral=True)     
            elif black in interaction.user.roles:
                await interaction.response.send_message(f"Please remove the previous color before choosing a new color", ephemeral=True)                                    
            else:
                await interaction.user.add_roles(gray)                 
                await interaction.response.send_message(f"{gray.mention} given", ephemeral=True)                
        async def white_callback(interaction):
            black = nextcord.utils.get(ctx.guild.roles, id=951837472764100691)
            white = nextcord.utils.get(ctx.guild.roles, id=951837833927225404)
            gray = nextcord.utils.get(ctx.guild.roles, id=951837699264901120)
            if white in interaction.user.roles:
                await interaction.user.remove_roles(white)                
                await interaction.response.send_message(f"{white.mention} removed", ephemeral=True)
            elif black in interaction.user.roles:
                await interaction.response.send_message(f"Please remove the previous color before choosing a new color", ephemeral=True)                    
            elif gray in interaction.user.roles:
                await interaction.response.send_message(f"Please remove the previous color before choosing a new color", ephemeral=True)                                    
            else:
                await interaction.user.add_roles(white)                   
                await interaction.response.send_message(f"{white.mention} given", ephemeral=True) 

        black.callback = black_callback
        gray.callback = gray_callback
        white.callback = white_callback
            
        bl = View(timeout=None)
        bl.add_item(black) 
        bl.add_item(gray)
        bl.add_item(white)

        #await ctx.send("https://cdn.discordapp.com/attachments/916959952080343060/955346696240517140/colours_snowy.png")
        #await ctx.send(embed=Iembed)
        #await ctx.send(embed=Bembed)
        #await ctx.send(embed=Gembed)
        #await ctx.send(embed=Rembed)
        #await ctx.send(embed=Yembed)
        #await ctx.send(embed=Pembed)
        #await ctx.send(embed=Piembed)
        await ctx.send(embed=Blembed, view=bl)

def setup(client):
    client.add_cog(Color(client))        
    print("✅ | Color cog ready!")
    print("---------------------------")                