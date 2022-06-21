import nextcord
from nextcord.ext import commands
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View
from nextcord.utils import get

class Roles(commands.Cog):
    """Self Roles"""
    def __init__(self,client):
        self.client = client
        self.persistent_views_added = False      

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.persistent_views_added:
            self.client.add_view(Pronouns())
            self.client.add_view(DM())
            self.client.add_view(Region())
            self.client.persistent_views_added = True         
   
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()    
    async def roles(self, ctx):
        
        Pembed=nextcord.Embed(color=0xE0BBE4)
        Pembed.add_field(name='Pronouns*!*', value="Select which pronouns you'd like to use! \n \n ♂️・`He/Him` \n ♀️・`She/Her` \n :transgender_symbol:・`They/Them`", inline=False)
        Pembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/953997251871658014/unknown.png")
        Pembed.set_footer(text="Select a role by clicking the buttons!")
        
        Dembed=nextcord.Embed(color=0xE0BBE4)
        Dembed.add_field(name="DM Preferences*!*", value="Select the preference for your DMs! \n \n 📭・`Dms Open` \n 📪・`Dms Closed` \n ❔・`Ask to dm` \n \n Please respect others' preferences! If you are DMed without consent please let a staff member know!")
        Dembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954608496727429120/mail.png")
        Dembed.set_footer(text="Select a role by clicking the buttons!")

        Rembed=nextcord.Embed(color=0xE0BBE4)
        Rembed.add_field(name='Region*!*', value="Select the continent you live in! \n \n <:S_asia:953989155363360818>・`Asia` \n <:S_europe:953989155271106560>・`Europe` \n <:S_north_america:953989155178811462>・`North America` \n <:S_south_america:953989154453209159>・`South America` \n <:S_oceania:953989154805534761>・`Oceania` \n <:S_africa:953989155388542976>・`Africa`")
        Rembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954415551269175376/region.png")
        Rembed.set_footer(text="Select a role by clicking the buttons!")

        Aembed=nextcord.Embed(color=0xE0BBE4)
        Aembed.add_field(name='Age*!*', value="Select the category for your age! \n \n <:S_Zenitsucry:954697294417133648>・`13-15` \n <:S_Kannalove:949974767627288626>・`16-18` \n <:S_uwusip:954697266621468682>・`18+`")
        Aembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954614570700382248/age.png")
        Aembed.set_footer(text="Select a role by clicking the buttons!")

        Gembed=nextcord.Embed(color=0xE0BBE4)
        Gembed.add_field(name="Games*!*", value="Select the games you play! \n \n <:S_genshin_impact:953989155858309130>・`Genshin Impact` \n <:S_fortnite:953989155350790175>・`Fortnite` \n <:S_minecraft:953989155183013909>・`Minecraft` \n <:S_warzone:953989154885222462>・`COD Warzone` \n <:S_CODM:953989155602460702>・`CODM` \n <:S_roblox:953989155409526814>・`Roblox` \n <:S_valorant:953989155040424036>・`Valorant` \n <:S_apex_legends:953989154994278430>・`Apex Legends` \n <:S_league_of_legends:953989156533583872>・`League of Leagends` \n <:S_osu:953989155371761664>・`Osu!` \n <:S_among_us:953989155296256001>・`Among Us` \n <:S_CSGO:953989155493380096>・`Counter Strike`")
        Gembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954631928449994752/games.png")
        Gembed.set_footer(text="Select a role by clicking the buttons!")

        APembed=nextcord.Embed(color=0xE0BBE4)
        APembed.add_field(name="Anime Preferences*!*", value="Select your preferences! \n \n <:S_Cutestare:951457328023101480>・`Anime Watcher` \n <:S_BlushWOW:949974767056859206>・`Manga Reader` \n <:S_Nezukopeek:949974767614709760>・`Light Novel Reader` \n <:S_Hugz:949974767417561158>・`Prefers Sub` \n <:S_Zerotwohug:954697266336251934>・`Prefers Dub` \n <:S_CatWTH:949693188044623922>・`Non Anime Watcher`")
        APembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954643077165879306/anime.png")
        APembed.set_footer(text="Select a role by clicking the buttons!")

        PGembed=nextcord.Embed(color=0xE0BBE4)
        PGembed.add_field(name="Pings and Notifications*!*", value="Select your ping and notification roles! \n \n <:Aannouncement_yuki:986523423033421894>・`Announcement Pings` \n <:Lewd_yuki:986523259514269757>・`Pings make me meow` \n 📰・`Server Updates` \n 🎉・`Event Pings` \n 🎁・`Giveaway Pings`")
        PGembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954663716979368036/ping.png")
        PGembed.set_footer(text="Select a role by clicking the buttons!")

        #await ctx.send("https://cdn.discordapp.com/attachments/916959952080343060/954681334956179486/Roles_snowy.png")
        await ctx.send(embed=Pembed, view=Pronouns())
        await ctx.send(embed=Dembed, view=DM())
        await ctx.send(embed=Rembed, view=Region())
        #await ctx.send(embed=Aembed)
        #await ctx.send(embed=Gembed)
        #await ctx.send(embed=APembed)
        #await ctx.send(embed=PGembed)

class Pronouns(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, emoji="♂️",label="He/Him", custom_id="male")    
    async def male(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        male = interaction.guild.get_role(947771914137514054)
        female = interaction.guild.get_role(947771913067974657)
        trans = interaction.guild.get_role(947771914926035014)

        assert isinstance(male, nextcord.Role)
        assert isinstance(female, nextcord.Role)
        assert isinstance(trans, nextcord.Role)        

        if male in interaction.user.roles:
            await interaction.user.remove_roles(male)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{male.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif female in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)             
        elif trans in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(male)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{male.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, emoji="♀️",label="She/Her", custom_id="female")    
    async def female(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        male = interaction.guild.get_role(947771914137514054)
        female = interaction.guild.get_role(947771913067974657)
        trans = interaction.guild.get_role(947771914926035014)

        assert isinstance(male, nextcord.Role)
        assert isinstance(female, nextcord.Role)
        assert isinstance(trans, nextcord.Role)        

        if female in interaction.user.roles:
            await interaction.user.remove_roles(female)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{female.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif male in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)             
        elif trans in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(female)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{female.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, emoji="⚧",label="They/Them", custom_id="trans")    
    async def trans(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        male = interaction.guild.get_role(947771914137514054)
        female = interaction.guild.get_role(947771913067974657)
        trans = interaction.guild.get_role(947771914926035014)

        assert isinstance(male, nextcord.Role)
        assert isinstance(female, nextcord.Role)
        assert isinstance(trans, nextcord.Role)        

        if trans in interaction.user.roles:
            await interaction.user.remove_roles(trans)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{trans.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif female in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)             
        elif male in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(trans)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{trans.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                   

class DM(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, emoji="📭",label="Open", custom_id="openn")    
    async def openn(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        openn = interaction.guild.get_role(947771917169999873)
        close = interaction.guild.get_role(947771918340218890)
        ask = interaction.guild.get_role(947771918675767307)

        assert isinstance(openn, nextcord.Role)
        assert isinstance(close, nextcord.Role)
        assert isinstance(ask, nextcord.Role)        

        if openn in interaction.user.roles:
            await interaction.user.remove_roles(openn)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{openn.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif close in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)             
        elif ask in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(openn)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{openn.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, emoji="📪",label="Closed", custom_id="closed")    
    async def close(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        openn = interaction.guild.get_role(947771917169999873)
        close = interaction.guild.get_role(947771918340218890)
        ask = interaction.guild.get_role(947771918675767307)

        assert isinstance(openn, nextcord.Role)
        assert isinstance(close, nextcord.Role)
        assert isinstance(ask, nextcord.Role)        

        if close in interaction.user.roles:
            await interaction.user.remove_roles(close)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{close.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif openn in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)             
        elif ask in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(close)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{close.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, emoji="❔",label="Ask", custom_id="ask")    
    async def ask(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        openn = interaction.guild.get_role(947771917169999873)
        close = interaction.guild.get_role(947771918340218890)
        ask = interaction.guild.get_role(947771918675767307)

        assert isinstance(openn, nextcord.Role)
        assert isinstance(close, nextcord.Role)
        assert isinstance(ask, nextcord.Role)        

        if ask in interaction.user.roles:
            await interaction.user.remove_roles(ask)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{ask.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif close in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)             
        elif openn in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(ask)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{openn.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)              

class Region(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, emoji="🌏",label="Asia", custom_id="asia")    
    async def asia(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        asia = interaction.guild.get_role(948809519104933888)
        europe = interaction.guild.get_role(948809708934926356)
        NA = interaction.guild.get_role(948809799456391179)
        SA = interaction.guild.get_role(948809872026247169)
        ociana = interaction.guild.get_role(948809979270410311)
        africa = interaction.guild.get_role(948810129531355146)

        assert isinstance(asia, nextcord.Role)
        assert isinstance(europe, nextcord.Role)
        assert isinstance(NA, nextcord.Role)        
        assert isinstance(SA, nextcord.Role)
        assert isinstance(ociana, nextcord.Role)
        assert isinstance(africa, nextcord.Role)

        if asia in interaction.user.roles:
            await interaction.user.remove_roles(asia)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{asia.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif europe in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)             
        elif NA in interaction.user.roles:
            em = nextcord.Embed(color=nextcord.Color.red())
            em.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
            em.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(asia)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{asia.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

def setup(client):
    client.add_cog(Roles(client))        
    print("✅ | Roles cog ready!")
    print("---------------------------")