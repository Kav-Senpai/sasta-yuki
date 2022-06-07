import nextcord
from nextcord.ext import commands
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View

class Embeds(commands.Cog):
    """Some fun commands!"""
    def __init__(self,client):
        self.client=client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx):
        
        Pembed=nextcord.Embed(color=0xE0BBE4)
        Pembed.add_field(name='Pronouns*!*', value="Select which pronouns you'd like to use! \n \n ♂️・`He/Him` \n ♀️・`She/Her` \n :transgender_symbol:・`They/Them`", inline=False)
        Pembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/953997251871658014/unknown.png")
        Pembed.set_footer(text="Select a role by reacting!")
        
        Dembed=nextcord.Embed(color=0xE0BBE4)
        Dembed.add_field(name="DM Preferences*!*", value="Select the preference for your DMs! \n \n 📭・`Dms Open` \n 📪・`Dms Closed` \n ❔・`Ask to dm` \n \n Please respect others' preferences! If you are DMed without consent please let a staff member know!")
        Dembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954608496727429120/mail.png")
        Dembed.set_footer(text="Select a role by reacting!")

        Rembed=nextcord.Embed(color=0xE0BBE4)
        Rembed.add_field(name='Region*!*', value="Select the continent you live in! \n \n <:S_asia:953989155363360818>・`Asia` \n <:S_europe:953989155271106560>・`Europe` \n <:S_north_america:953989155178811462>・`North America` \n <:S_south_america:953989154453209159>・`South America` \n <:S_oceania:953989154805534761>・`Oceania` \n <:S_africa:953989155388542976>・`Africa`")
        Rembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954415551269175376/region.png")
        Rembed.set_footer(text="Select a role by reacting!")

        Aembed=nextcord.Embed(color=0xE0BBE4)
        Aembed.add_field(name='Age*!*', value="Select the category for your age! \n \n <:S_Zenitsucry:954697294417133648>・`13-15` \n <:S_Kannalove:949974767627288626>・`16-18` \n <:S_uwusip:954697266621468682>・`18+`")
        Aembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954614570700382248/age.png")
        Aembed.set_footer(text="Select a role by reacting!")

        Gembed=nextcord.Embed(color=0xE0BBE4)
        Gembed.add_field(name="Games*!*", value="Select the games you play! \n \n <:S_genshin_impact:953989155858309130>・`Genshin Impact` \n <:S_fortnite:953989155350790175>・`Fortnite` \n <:S_minecraft:953989155183013909>・`Minecraft` \n <:S_warzone:953989154885222462>・`COD Warzone` \n <:S_CODM:953989155602460702>・`CODM` \n <:S_roblox:953989155409526814>・`Roblox` \n <:S_valorant:953989155040424036>・`Valorant` \n <:S_apex_legends:953989154994278430>・`Apex Legends` \n <:S_league_of_legends:953989156533583872>・`League of Leagends` \n <:S_osu:953989155371761664>・`Osu!` \n <:S_among_us:953989155296256001>・`Among Us` \n <:S_CSGO:953989155493380096>・`Counter Strike`")
        Gembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954631928449994752/games.png")
        Gembed.set_footer(text="Select a role by reacting!")

        APembed=nextcord.Embed(color=0xE0BBE4)
        APembed.add_field(name="Anime Preferences*!*", value="Select your preferences! \n \n <:S_Cutestare:951457328023101480>・`Anime Watcher` \n <:S_BlushWOW:949974767056859206>・`Manga Reader` \n <:S_Nezukopeek:949974767614709760>・`Light Novel Reader` \n <:S_Hugz:949974767417561158>・`Prefers Sub` \n <:S_Zerotwohug:954697266336251934>・`Prefers Dub` \n <:S_CatWTH:949693188044623922>・`Non Anime Watcher`")
        APembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954643077165879306/anime.png")
        APembed.set_footer(text="Select a role by reacting!")

        PGembed=nextcord.Embed(color=0xE0BBE4)
        PGembed.add_field(name="Pings and Notifications*!*", value="Select your ping and notification roles! \n \n <:S_announce:954663840442884116>・`Announcement Pings` \n <:S_pings_make_me_meow:954663840505802762>・`Pings make me meow` \n 📰・`Server Updates` \n <:S_event:954663840438710312>・`Event Pings` \n 🎁・`Giveaway Pings`")
        PGembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/916959952080343060/954663716979368036/ping.png")
        PGembed.set_footer(text="Select a role by reacting!")

        await ctx.send("https://cdn.discordapp.com/attachments/916959952080343060/954681334956179486/Roles_snowy.png")
        await ctx.send(embed=Pembed)
        await ctx.send(embed=Dembed)
        await ctx.send(embed=Rembed)
        await ctx.send(embed=Aembed)
        await ctx.send(embed=Gembed)
        await ctx.send(embed=APembed)
        await ctx.send(embed=PGembed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def info(self, ctx):

        welc = nextcord.Embed(color=0xF2D3BA, title="<a:SP_snowflake:951396520702410803> Welcome to Yuki Café! <a:SP_snowflake:951396520702410803>", description="Yuki Café is a community server where you can chat, make new friends and have fun. A committed Staff Team to assist you and keep the server a safe place for everyone. A great place to show your creativity, may it be arts, photography, writing, singing etc. Regular events and giveaways keep the server exciting for everyone. \n We hope to see you all within the server! ^-^ \n ˗ˏˋ Yuki ˎˊ˗ \n \n • Read the <#947512003969314857> \n • Grab some <#947771959926747146> \n • Come chat in <#947771966050418708> & <#947773050697416745>")
        welc.set_footer(text="By being in this server, you agree to your actions being logged for moderation purposes.")

        special = nextcord.Embed(color=0xF8C8DC, title="◦ ━ Special Roles ━ ◦", description="<:__:961842810162642974> <:S_Youtube:961844575314526220> <@&951744493810503710> \n <:__:961842809726464051> Must have a YouTube channel with 5K+ subscribers connected to Discord! \n \n <:__:961842810162642974> <:S_Twitch:961842810020040764> <@&951744705098579978> \n <:__:961842809726464051> Must have a Twitch channel with 2K+ followers connected to Discord! \n \n <:__:961842810162642974> <:S_Event_Manager:961842810477244476> <@&951744016049918003> \n <:__:961842809726464051> Members that help organize & host events! \n \n <:__:961842810162642974> <:S_Tiaga_Salute:961842809780977736> <@&951743864736186418> \n <:__:961842809726464051> Given to members that are here from the start! \n \n <:__:961842810162642974> <@&952137448257900544> \n <:__:961842809726464051> Given to members that consistently post good quality creations in <#947771980789190656> \n \n <:__:961842810162642974> <:S_Movie_Critic:961842811307716638> <@&951743468789694504> \n <:__:961842809726464051> Given to those who watch a movie with us! \n \n <:__:961842810162642974> <:S_Emilianya:949974767430148156> <@&951743742866513950> \n <:__:961842809726464051> Given to members who invite 5+ people to the server using their own invite link! \n \n <:__:961842810162642974> <:S_Pepebusiness:978570068990496778> <@&951743955903582238> \n <:__:961842809726464051> Given to members that consistently post good quality memes in <#947771966910246952> \n \n <:__:961842810162642974> <:S_Rengokuhandraise:949287664669057044> <@&951743710163533844> \n <:__:961842809726464051> Given to those who welcome new members and are active!")

        level = nextcord.Embed(color=0x98ddfc, title="◦ ━ Leveling Roles ━ ◦", description="Level roles are given to you as you level up on the server by gaining experience. You can gain experience by chatting on the server!")
        level.add_field(name='Here are the available roles and their rewards:', value='**Level 0** \n ➩ <@&947771911604146216> \n > Role obtained by joining the server')
        level.add_field(name='Level 1', value='➩ <@&947771910790451221> \n > Get access to colors in <#955357785053360128>', inline=False)
        level.add_field(name='Level 5', value='➩ <@&947771910064836618> \n > Get access to add reaction in all channels', inline= False)
        level.add_field(name='Level 10', value='➩ <@&947771909079203860> \n > Can apply for Server Staff', inline= False)
        level.add_field(name='Level 15', value='➩ <@&947771908122902559> \n > Get access to embeded links/GIF perms in most channels', inline= False)
        level.add_field(name='Level 20', value='➩ <@&947771907174957096> \n > Get access to picture perms in most channels', inline= False)
        level.add_field(name='Level 30', value='➩ <@&947771905853763594> \n > Get 3x entries in giveaways \n > 30k <a:S_SnowStone:976808329076678686>', inline= False)
        level.add_field(name='Level 50', value='➩ <@&947771903907614803> \n > Get 5x entries in giveaways \n > 50k <a:S_SnowStone:976808329076678686>', inline= False)
        level.set_thumbnail(url='https://cdn.discordapp.com/attachments/961610704060829696/961885653744893972/SeekPng.com_level-up-png_2687914.png')
        level.set_footer(text='To claim your perks, kindly open a ticket!', icon_url="https://cdn.discordapp.com/attachments/961610704060829696/978570642628706356/861308537736658944.gif")

        shop = nextcord.Embed(color=0xff6961, description="You can earn SnowStones by using the economy commands and participating in special events!\n\nYou can buy a role with the command `.buy <role>`", title="◦ ━ Economy & Shop ━ ◦")
        shop.set_thumbnail(url="https://cdn.discordapp.com/attachments/961610704060829696/979650967509291008/unknown.png")
        shop.set_footer(text="Type .shop to view the shop!")
        shop.add_field(name="> 5,000,000 <a:S_SnowStone:976808329076678686>", value="<@&978556685557833750>", inline= False)
        shop.add_field(name="> 2,000,000 <a:S_SnowStone:976808329076678686>", value="<@&978555585110872134> <@&978555580631367701> <@&978555589368086528>", inline= False)        
        shop.add_field(name="> 1,000,000 <a:S_SnowStone:976808329076678686>", value="<@&978554836863815751> <@&978554832698892308> <@&978554820535398470>", inline= False)
        shop.add_field(name="> 500,000 <a:S_SnowStone:976808329076678686>", value="<@&978308684318924830> <@&978553757518401587> <@&978308676131622992> <@&978308687888277576>", inline= False)
        shop.add_field(name="> 250,000 <a:S_SnowStone:976808329076678686>", value="<@&978551261936885860> <@&978551211454234624> <@&978551184543580211> <@&978551157070917642> <@&978551234346745887>", inline= False)
        shop.add_field(name="> 100,000 <a:S_SnowStone:976808329076678686>", value="<@&955395667575046176> <@&955395423802126377> <@&955395643428470814> <@&955395654371397643> <@&955395156171956228> <@&955396048258498580>", inline= False)
        shop.add_field(name="> 50,000 <a:S_SnowStone:976808329076678686>", value="<@&955395403271008256> <@&955395443393720370> <@&955395392076390410> <@&955395374716170291> <@&955395183145533500>", inline= False)
        shop.add_field(name="> 20,000 <a:S_SnowStone:976808329076678686>", value="<@&955395970995195954> <@&955395167521738812> <@&955395178930241547> <@&955395991006240798> <@&955396028285210624>", inline= False)
        shop.add_field(name="> 10,000 <a:S_SnowStone:976808329076678686>", value="<@&978549357009858571>", inline= False)                

        booster = nextcord.Embed(color=0xffa4ac, title="◦ ━ Booster Perks ━ ◦", description="<a:Tada_yuki:976697466634240011> 》 Booster role hoisted high in the member list <@&947517428043227238>"
                                                                                            "\n <a:Tada_yuki:976697466634240011> 》 5K server currency per week using `.booster`"
                                                                                            "\n<a:Tada_yuki:976697466634240011> 》 Access to the special booster only colors in <#955357785053360128>"
                                                                                            "\n<a:Tada_yuki:976697466634240011> 》 All leveled up permissions!"
                                                                                            "\n<a:Tada_yuki:976697466634240011> 》 Get 10x entries & bypass requirements in ALL giveaways!"
                                                                                            "\n<a:Tada_yuki:976697466634240011> 》 Get a free custom role while your boost is active!")
        booster.set_thumbnail(url="https://cdn.discordapp.com/attachments/961610704060829696/979690786536947722/boost.png")   
                                                                                                     

        await ctx.send("https://cdn.discordapp.com/attachments/961610704060829696/979642171495940126/welcome.png")
        await ctx.send(embed=welc)
        await ctx.send("https://cdn.discordapp.com/attachments/961610704060829696/979645083869650974/special_roles.png")
        await ctx.send(embed=special)
        await ctx.send("https://cdn.discordapp.com/attachments/961610704060829696/979647450858012672/leveling_roles.png")
        await ctx.send(embed=level)
        await ctx.send("https://cdn.discordapp.com/attachments/961610704060829696/979679575665692712/Economy.png")
        await ctx.send(embed=shop)
        await ctx.send("https://cdn.discordapp.com/attachments/961610704060829696/979696319985754112/Boosting.png")
        await ctx.send(embed=booster)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def u(self, ctx):
        embed = nextcord.Embed(color=0xaec6cf ,title="Table of Contents", description = "<a:Wave_yuki:979702424799428658> [Welcome to Yuki Café](https://discordapp.com/channels/947498180243767347/955447455971938314/979709646904385606)"
                                                                            "\n\n<a:Dance_yuki:979704651345707038> [Special Roles](https://discordapp.com/channels/947498180243767347/955447455971938314/979709652231147541)"
                                                                            "\n\n<a:Love_yuki:977929410214776893> [Leveling Roles](https://discordapp.com/channels/947498180243767347/955447455971938314/979709668131749978)"
                                                                            "\n\n<a:PaimonMoney_yuki:979705923071279125> [Economy & Shop](https://discordapp.com/channels/947498180243767347/955447455971938314/979709673081044992)"
                                                                            "\n\n<a:CatNod_yuki:979711338353917962> [Boosting](https://discordapp.com/channels/947498180243767347/955447455971938314/979709678055473162)")
        embed.set_footer(text="Click to jump to an info section!")                                                                        
        await ctx.send(embed=embed)            

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rules(self, ctx):

        button1=Button(label="Discord Terms of Service", style=ButtonStyle.url, url="https://discord.com/terms")
        button2=Button(label="Discord Community Guidlines", style=ButtonStyle.url, url="https://discord.com/guidelines")

        ruleEmbed=nextcord.Embed(title='<a:SP_warn:951397930961633291> SERVER RULES', description="By participating in chat, you agree to the rules. Failure to follow these will result in punishment. If someone is acting inappropriately, please ping an online Staff. You must abide by Discord's community guidelines on joining this server. Use common sense or simply ask someone incase you are not clear about any rules.", color=0xF8C8DC)
        advEmbed=nextcord.Embed(color=0xF8C8DC)
        advEmbed.add_field(name='<:SP_rules:948080441624248341> NO ADVERTISING', value='<a:SP_bluearrow:951398530671591474> People who message "DM for free stuff!" or any statements similar to that are likely to advertise after you DM them. We will mute the user for a minimum of 12 hours if they do so.\n \n <a:SP_pinkarrow:951398530625445888> DM advertising is prohibited. If you were reported for DM advertising, you will get banned on the first offense.\n \n <a:SP_bluearrow:951398530671591474> Attempting to publicly advertise a server by sending an invite link will get you SPblankbanned on the first offense.', inline=False)
        respectEmbed=nextcord.Embed(color=0xF8C8DC)
        respectEmbed.add_field(name='<:SP_rules:948080441624248341> BE RESPECTFUL TOWARDS OTHERS', value="<a:SP_pinkarrow:951398530625445888> Absolutely NO DRAMA/ARGUMENTS whatsoever. Instead of verbal skirmish, communicate with respect and consideration towards others and come to a common agreement/opinion about the subject of the arguments.\n \n <a:SP_bluearrow:951398530671591474> If both parties wish to continue with the argument, take it to dm's. We want everyone to be able to talk in chats and not feel awkward to do so.\n \n <a:SP_pinkarrow:951398530625445888> No offensive names/language of any kind. This rule applies to the server as well as in Dm's. If someone asks you to stop, STOP. Otherwise, you will get muted or banned.\n \n <a:SP_bluearrow:951398530671591474> If someone is using offensive nicknames/names/words, you're always free to report them to a mod to keep the server clean and wholesome for everyone. Thank you for your reports in advance.", inline=False)
        nsfwEmbed=nextcord.Embed(color=0xF8C8DC)
        nsfwEmbed.add_field(name='<:SP_rules:948080441624248341> NSFW CONTENT HAS NO PLACE', value="<a:SP_pinkarrow:951398530625445888> It's not that hard to keep it PG-13, so keep it in mind before posting or saying anything that may be considered NSFW content. This rule applies in both text and voice channels.\n \n <a:SP_bluearrow:951398530671591474> No nudity in profile pictures or lewd nicknames.\n \n <a:SP_pinkarrow:951398530625445888> No swear/inappropriate words in any form in chat/voice-chat/images.\n \n <a:SP_bluearrow:951398530671591474> Do not try bypassing the bots. If a mod catches you doing so, it will lead to a warning and mute and like any of the other rules if repeatedly broken, a ban.\n \n <a:SP_pinkarrow:951398530625445888>  If you want to share an image but you are unsure if it's inappropriate for the server, please consult and confirm it with a Staff.", inline=False)
        staffEmbed=nextcord.Embed(color=0xF8C8DC)
        staffEmbed.add_field(name='<:SP_rules:948080441624248341> ALWAYS LISTEN AND RESPECT THE STAFF', value='<a:SP_bluearrow:951398530671591474> Being disrespectful, rude, or simply not listening to any of them will result in an automatic mute or ban depending on the severity of the situation.\n \n <a:SP_pinkarrow:951398530625445888> Staff are normal human beings too, they also need to take care of things in their lives while also keeping the server in order. We ask you to be kind to each and every staff member.\n \n <a:SP_bluearrow:951398530671591474> Feel free to ping the Staff but ONLY if you require immediate assistance or to seek our attention to report rule-breakers')
        channelEmbed=nextcord.Embed(color=0xF8C8DC)
        channelEmbed.add_field(name='<:SP_rules:948080441624248341> FOLLOW CHANNEL RULES', value='<a:SP_pinkarrow:951398530625445888> Always remember to read the rules in the description and check the pins to know how to appropriately use a channel.\n \n <a:SP_bluearrow:951398530671591474> Stealing artworks or any kind of intellectual property is strictly prohibited and will not be tolerated. Always ask the permission of the original poster.\n \n <a:SP_pinkarrow:951398530625445888> Posting of fake selfies or art work will not be tolerated. Trolling with fake media will be dealt with severely.\n \n <a:SP_bluearrow:951398530671591474> Use the bots in appropriate channels. Do not spam the commands throughout the server.')

        guidelines=View()
        guidelines.add_item(button1)
        guidelines.add_item(button2)

        await ctx.channel.purge(limit=1)
        await ctx.send('https://cdn.discordapp.com/attachments/944570768363245571/953565257505316864/rules_snowy.png') 
        await ctx.send(embed=ruleEmbed, view=guidelines)
        await ctx.send(embed=advEmbed)
        await ctx.send(embed=respectEmbed)
        await ctx.send(embed=nsfwEmbed)
        await ctx.send(embed=staffEmbed)
        await ctx.send(embed=channelEmbed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def partner(self, ctx):
        p = nextcord.Embed(color=0x8BD3E6, description="╭⋟──────────────────╮")
        p.add_field(name="<a:YAY_yuki:979279604126744607> __Requirements for Partnerships__ <a:YAY_yuki:979279604126744607>", value="<a:SP_pinkarrow:951398530625445888> Your server MUST has 50+ members!\n<a:SP_bluearrow:951398530671591474> Your server follows the Discord TOS!\n<a:SP_pinkarrow:951398530625445888> Your server has a 'partner' channel available!\n<a:SP_bluearrow:951398530671591474> Your server is fully SFW (NSFW locked with an age verification is fine!)\n➥ DM any <@&947771899725905970> to get partnered!\n╰──────────────────⋞╯\n\n╭⋟──────────────────╮", inline= False)
        p.add_field(name="__Want to become a Partnership Manager in Yuki Café?__", value="<a:SP_pinkarrow:951398530625445888> Minimum of 5 partners a week!\n<a:SP_bluearrow:951398530671591474> You MUST have experience or be willing to learn to become a Partnership Manager!\n➥ DM <@!946011272607072266> or <@!870639335614087168> to get started.\n╰──────────────────⋞╯\n\n*The code block version of our server template will be posted down below ↓ We thank you greatly for your interest and look forward to working together!*\n```⋆✩* ┈┈┈┈﹤**Yuki Café*!***﹥ ┈┈┈┈ ✩⋆\n»»———— make new friends*!* —ミ✩\n:snowflake:・sfw & non-toxic\n:snowman2:・semi-active & friendly\ne:・cute emotes\n:ice_cube:・fun events\n:icecream:・always hiring pms\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nજ⁀➴ https://discord.gg/BVPSBw3UMb :･ﾟ✧:･ﾟ✧\nજ⁀➴ https://imgur.com/a/Y2VlV2v :･ﾟ✧:･ﾟ✧\nજ⁀➴ https://imgur.com/a/OSd2rOz :･ﾟ✧:･ﾟ✧```", inline= False)
        await ctx.send("https://cdn.discordapp.com/attachments/961610704060829696/979352969357189180/partners.png")
        await ctx.send(embed=p)

    

def setup(client):
    client.add_cog(Embeds(client))        
    print("✅ | Embeds cog ready!")  
    print("---------------------------")         