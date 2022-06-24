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
            self.client.add_view(Age())
            self.client.add_view(Games())
            self.client.add_view(Pings())
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
        Rembed.add_field(name='Region*!*', value="Select the continent you live in! \n \n <:Asia_yuki:986530978078007356>・`Asia` \n <:Europe_yuki:986530975766954014>・`Europe` \n <:NorthAmerica_yuki:986530980682690661>・`North America` \n <:SouthAmerica_yuki:986530983505448980>・`South America` \n <:Oceania_yuki:986530985707462656>・`Oceania` \n <:Africa_yuki:986530987917848636>・`Africa`")
        Rembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954415551269175376/region.png")
        Rembed.set_footer(text="Select a role by clicking the buttons!")

        Aembed=nextcord.Embed(color=0xE0BBE4)
        Aembed.add_field(name='Age*!*', value="Select the category for your age! \n \n <:ZenitsuSleepy_yuki:954704367385198592>・`13-15` \n <:Wavey_yuki:951014468366766150>・`16-18` \n <:UwUSip_yuki:955379637356200016>・`18+`")
        Aembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954614570700382248/age.png")
        Aembed.set_footer(text="Select a role by clicking the buttons!")

        Gembed=nextcord.Embed(color=0xE0BBE4)
        Gembed.add_field(name="Games*!*", value="Select the games you play! \n \n <:Genshin_yuki:986530946062888992>・`Genshin Impact` \n <:Fortnight_yuki:986530948185206814>・`Fortnite` \n <:Minecraft_yuki:986530950227849267>・`Minecraft` \n <:COD_yuki:986530952656330792>・`COD Warzone` \n <:CODM_yuki:986530954845749258>・`CODM` \n <:Roblox_yuki:986530957253292062>・`Roblox` \n <:Valorant_yuki:986530959237210183>・`Valorant` \n <:ApexLegends_yuki:986530961766367232>・`Apex Legends` \n <:LeagueOfLegends_yuki:986530964035489862>・`League of Leagends` \n <:Osu_yuki:986530966258479124>・`Osu!` \n <:AmongUs_yuki:986530968619860028>・`Among Us` \n <:CSGO_yuki:986530970691833899>・`Counter Strike`")
        Gembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954631928449994752/games.png")
        Gembed.set_footer(text="Select a role by clicking the buttons!")

        APembed=nextcord.Embed(color=0xE0BBE4)
        APembed.add_field(name="Anime Preferences*!*", value="Select your preferences! \n \n <:S_Cutestare:951457328023101480>・`Anime Watcher` \n <:S_BlushWOW:949974767056859206>・`Manga Reader` \n <:S_Nezukopeek:949974767614709760>・`Light Novel Reader` \n <:S_Hugz:949974767417561158>・`Prefers Sub` \n <:02Hug_yuki:955379637763072000>・`Prefers Dub` \n <:S_CatWTH:949693188044623922>・`Non Anime Watcher`")
        APembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954643077165879306/anime.png")
        APembed.set_footer(text="Select a role by clicking the buttons!")

        PGembed=nextcord.Embed(color=0xE0BBE4)
        PGembed.add_field(name="Pings and Notifications*!*", value="Select your ping and notification roles! \n \n <:Aannouncement_yuki:986523423033421894>・`Announcement Pings` \n <:Lewd_yuki:986523259514269757>・`Pings make me meow` \n 🎉・`Event Pings` \n 🎁・`Giveaway Pings`")
        PGembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954663716979368036/ping.png")
        PGembed.set_footer(text="Select a role by clicking the buttons!")

        #await ctx.send("https://cdn.discordapp.com/attachments/916959952080343060/954681334956179486/Roles_snowy.png")
        await ctx.send(embed=Pembed, view=Pronouns())
        await ctx.send(embed=Dembed, view=DM())
        await ctx.send(embed=Rembed, view=Region())
        await ctx.send(embed=Aembed, view=Age())
        await ctx.send(embed=Gembed, view=Games())
        await ctx.send(embed=APembed, view= Anime())
        await ctx.send(embed=PGembed, view=Pings())

class Pronouns(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="♂️",label="He/Him", custom_id="male")    
    async def male(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        male = interaction.guild.get_role(947771914137514054)
        female = interaction.guild.get_role(947771913067974657)
        trans = interaction.guild.get_role(947771914926035014)

        assert isinstance(male, nextcord.Role)
        assert isinstance(female, nextcord.Role)
        assert isinstance(trans, nextcord.Role)    

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")            

        if male in interaction.user.roles:
            await interaction.user.remove_roles(male)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{male.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif female in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif trans in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(male)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{male.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="♀️",label="She/Her", custom_id="female")    
    async def female(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        male = interaction.guild.get_role(947771914137514054)
        female = interaction.guild.get_role(947771913067974657)
        trans = interaction.guild.get_role(947771914926035014)

        assert isinstance(male, nextcord.Role)
        assert isinstance(female, nextcord.Role)
        assert isinstance(trans, nextcord.Role)        

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if female in interaction.user.roles:
            await interaction.user.remove_roles(female)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{female.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif male in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif trans in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(female)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{female.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="⚧",label="They/Them", custom_id="trans")    
    async def trans(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        male = interaction.guild.get_role(947771914137514054)
        female = interaction.guild.get_role(947771913067974657)
        trans = interaction.guild.get_role(947771914926035014)

        assert isinstance(male, nextcord.Role)
        assert isinstance(female, nextcord.Role)
        assert isinstance(trans, nextcord.Role)        

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if trans in interaction.user.roles:
            await interaction.user.remove_roles(trans)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{trans.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif female in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif male in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(trans)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{trans.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                   

class DM(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="📭",label="Open", custom_id="openn")    
    async def openn(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        openn = interaction.guild.get_role(947771917169999873)
        close = interaction.guild.get_role(947771918340218890)
        ask = interaction.guild.get_role(947771918675767307)

        assert isinstance(openn, nextcord.Role)
        assert isinstance(close, nextcord.Role)
        assert isinstance(ask, nextcord.Role)        

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if openn in interaction.user.roles:
            await interaction.user.remove_roles(openn)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{openn.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif close in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif ask in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(openn)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{openn.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="📪",label="Closed", custom_id="closed")    
    async def close(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        openn = interaction.guild.get_role(947771917169999873)
        close = interaction.guild.get_role(947771918340218890)
        ask = interaction.guild.get_role(947771918675767307)

        assert isinstance(openn, nextcord.Role)
        assert isinstance(close, nextcord.Role)
        assert isinstance(ask, nextcord.Role)        

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if close in interaction.user.roles:
            await interaction.user.remove_roles(close)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{close.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif openn in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif ask in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(close)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{close.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="❔",label="Ask", custom_id="ask")    
    async def ask(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        openn = interaction.guild.get_role(947771917169999873)
        close = interaction.guild.get_role(947771918340218890)
        ask = interaction.guild.get_role(947771918675767307)

        assert isinstance(openn, nextcord.Role)
        assert isinstance(close, nextcord.Role)
        assert isinstance(ask, nextcord.Role)        

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")        

        if ask in interaction.user.roles:
            await interaction.user.remove_roles(ask)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{ask.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif close in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif openn in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(ask)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{openn.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)              

class Region(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Asia_yuki:986530978078007356>",label="Asia", custom_id="asia", row=0)    
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

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if asia in interaction.user.roles:
            await interaction.user.remove_roles(asia)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{asia.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif europe in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif NA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True) 
        elif SA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif ociana in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)    
        elif africa in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                                                  
        else:
            await interaction.user.add_roles(asia)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{asia.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Europe_yuki:986530975766954014>",label="Europe", custom_id="europe", row=0)    
    async def europe(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
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

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if europe in interaction.user.roles:
            await interaction.user.remove_roles(europe)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{europe.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif asia in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif NA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True) 
        elif SA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif ociana in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)    
        elif africa in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                                                  
        else:
            await interaction.user.add_roles(europe)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{europe.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:NorthAmerica_yuki:986530980682690661>",label="North America", custom_id="NA", row=0)    
    async def NA(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
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

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if NA in interaction.user.roles:
            await interaction.user.remove_roles(NA)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{NA.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif europe in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif asia in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True) 
        elif SA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif ociana in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)    
        elif africa in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                                                  
        else:
            await interaction.user.add_roles(NA)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{NA.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:SouthAmerica_yuki:986530983505448980>",label="South America", custom_id="SA", row=1)    
    async def SA(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
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

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if SA in interaction.user.roles:
            await interaction.user.remove_roles(SA)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{SA.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif europe in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif NA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True) 
        elif asia in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif ociana in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)    
        elif africa in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                                                  
        else:
            await interaction.user.add_roles(SA)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{SA.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)             

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Oceania_yuki:986530985707462656>",label="Ociana", custom_id="ociana", row=1)    
    async def ociana(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
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

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if ociana in interaction.user.roles:
            await interaction.user.remove_roles(ociana)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{ociana.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif europe in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif NA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True) 
        elif SA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif asia in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)    
        elif africa in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                                                  
        else:
            await interaction.user.add_roles(ociana)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{ociana.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Africa_yuki:986530987917848636>",label="Africa", custom_id="africa", row=1)    
    async def africa(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
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

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if africa in interaction.user.roles:
            await interaction.user.remove_roles(africa)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{africa.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif europe in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif NA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True) 
        elif SA in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif ociana in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)    
        elif asia in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                                                  
        else:
            await interaction.user.add_roles(africa)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{africa.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

class Age(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:ZenitsuSleepy_yuki:954704367385198592>",label="13-15", custom_id="_13")    
    async def _13(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        _13 = interaction.guild.get_role(947771924082221076)
        _16 = interaction.guild.get_role(947771924853964810)
        _18 = interaction.guild.get_role(947771925625704458)

        assert isinstance(_13, nextcord.Role)
        assert isinstance(_16, nextcord.Role)
        assert isinstance(_18, nextcord.Role)        

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if _13 in interaction.user.roles:
            await interaction.user.remove_roles(_13)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{_13.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif _16 in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif _18 in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(_13)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{_13.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Wavey_yuki:951014468366766150>",label="16-18", custom_id="_16")    
    async def _16(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        _13 = interaction.guild.get_role(947771924082221076)
        _16 = interaction.guild.get_role(947771924853964810)
        _18 = interaction.guild.get_role(947771925625704458)

        assert isinstance(_13, nextcord.Role)
        assert isinstance(_16, nextcord.Role)
        assert isinstance(_18, nextcord.Role)        

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if _16 in interaction.user.roles:
            await interaction.user.remove_roles(_16)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{_16.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif _13 in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif _18 in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(_16)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{_16.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:UwUSip_yuki:955379637356200016>",label="18+", custom_id="_18")    
    async def _18(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        _13 = interaction.guild.get_role(947771924082221076)
        _16 = interaction.guild.get_role(947771924853964810)
        _18 = interaction.guild.get_role(947771925625704458)

        assert isinstance(_13, nextcord.Role)
        assert isinstance(_16, nextcord.Role)
        assert isinstance(_18, nextcord.Role)        

        uwu = nextcord.Embed(color=nextcord.Color.red())
        uwu.set_footer(text="If you think you chose the wrong role, please remove the current role and choose the right role!")
        uwu.set_author(name=f"You are allowed to take only 1 role!", icon_url="https://cdn.discordapp.com/emojis/951397930961633291.gif?v=1")

        if _18 in interaction.user.roles:
            await interaction.user.remove_roles(_18)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{_18.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 
        elif _16 in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)             
        elif _18 in interaction.user.roles:
            await interaction.response.send_message(embed=uwu, ephemeral=True)                                                                          
        else:
            await interaction.user.add_roles(_18)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{_18.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                         

class Games(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Genshin_yuki:986530946062888992>", label="Genshin Impact", custom_id="genshin", row=0)
    async def genshin(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771927320227860)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Fortnight_yuki:986530948185206814>", label="Fortnite", custom_id="fortnite", row=0)
    async def fortnite(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951799457291317289)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Minecraft_yuki:986530950227849267>", label="Minecraft", custom_id="minecraft", row=0)
    async def minecraft(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771927806742570)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:COD_yuki:986530952656330792>", label="COD Warzone", custom_id="warzone", row=0)
    async def warzone(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951799188159594516)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)              

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:CODM_yuki:986530954845749258>", label="CODM", custom_id="CODM", row=1)
    async def CODM(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951799339754348564)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)    

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Roblox_yuki:986530957253292062>", label="Roblox", custom_id="roblox", row=1)
    async def roblox(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771928997945364)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Valorant_yuki:986530959237210183>", label="Valorant", custom_id="valo", row=1)
    async def valorant(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771929652244501)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:ApexLegends_yuki:986530961766367232>", label="Apex Legends", custom_id="apex", row=1)
    async def apex(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951799231121879060)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:LeagueOfLegends_yuki:986530964035489862>", label="League of Leagends", custom_id="LoL", row=2)
    async def league(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951799385942011904)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Osu_yuki:986530966258479124>", label="Osu!", custom_id="osu", row=2)
    async def osu(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951811226256691200)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:AmongUs_yuki:986530968619860028>", label="Among Us", custom_id="sus", row=2)
    async def us(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951811346939387914)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:CSGO_yuki:986530970691833899>", label="Counter Strike", custom_id="csgo", row=2)
    async def csgo(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951811264152240138)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True) 

class Anime(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:CuteStare_yuki:951457328023101480>", label="Anime Watcher", custom_id="anime", row=0)
    async def anime(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771944017747968)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:BlushWOW_yuki:949974767056859206>", label="Manga Reader", custom_id="manga", row=0)
    async def manga(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771944797884436)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:NezukoPeek_yuki:949974767614709760>", label="Light Novel Reader", custom_id="novel", row=0)
    async def novel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951801444942626886)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Hugz_yuki:949974767417561158>", label="Prefers Sub", custom_id="sub", row=1)
    async def sub(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951801628388900876)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)  

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:02Hug_yuki:955379637763072000>", label="Prefers Dub", custom_id="dub", row=1)
    async def dub(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951801546570600509)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:CatWTH_yuki:949693188044623922>", label="Non Anime Watcher", custom_id="non", row=1)
    async def non(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(951801686199001108)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

class Pings(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Aannouncement_yuki:986523423033421894>", label="Announcement Pings", custom_id="announce")
    async def announce(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771931296419872)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="<:Lewd_yuki:986523259514269757>", label="Pings turn me on*", custom_id="lewd")
    async def shit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(954655409015234570)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="🎉", label="Event Pings", custom_id="event")
    async def event(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771934983225344)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   

    @nextcord.ui.button(style=nextcord.ButtonStyle.gray, emoji="🎁", label="Giveaway Pings", custom_id="gws")
    async def gws(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        role = interaction.guild.get_role(947771933972398151)
        assert isinstance(role, nextcord.Role)      

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)   
            em = nextcord.Embed(color=nextcord.Color.red(), description=f"{role.mention} **was successfully removed!**")
            await interaction.response.send_message(embed=em, ephemeral=True)                                                                     
        else:
            await interaction.user.add_roles(role)                
            em = nextcord.Embed(color=nextcord.Color.green(), description=f"{role.mention} **was successfully given!**")
            await interaction.response.send_message(embed=em, ephemeral=True)   
            
def setup(client):
    client.add_cog(Roles(client))        
    print("✅ | Roles cog ready!")
    print("---------------------------")