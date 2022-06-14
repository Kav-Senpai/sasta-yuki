import nextcord, requests, os
from nextcord.ext import commands
import random
import aiohttp
import asyncio
import json
import animec 
from animec import waifu, Waifu, kao
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View

class Anime(commands.Cog):
    """Anime and Roleplay Commands"""
    def __init__(self,client):
        self.client = client

    @commands.command(aliases=["Anime","ANIME"])
    async def anime(self, ctx:commands.Context,*, query):
        try:
            anime = animec.Anime(query)
        except:
            await ctx.reply(embed= nextcord.Embed(description="<a:S_Cross:963039895922814996> | No corresponding Anime was found for the search query!", color=nextcord.Color.red())) 
            return
    
        link=Button(label="Link to Anime",url=anime.url,style=ButtonStyle.link)
        view = View()
        view.add_item(link)

        embed = nextcord.Embed(title=anime.title_english,description=f"{anime.description[:300]}...",color=ctx.author.color) 
        embed.add_field(name=":stopwatch: Episodes",value= str(anime.episodes))  
        embed.add_field(name=":star: Rating",value= str(anime.rating))  
        embed.add_field(name=":globe_with_meridians: Broadcast",value= str(anime.broadcast))  
        embed.add_field(name=":hourglass: Status",value= str(anime.status))  
        embed.add_field(name=":information_source: Type",value= str(anime.type))  
        embed.add_field(name=":warning: NSFW Status",value= str(anime.is_nsfw()))  
        embed.set_thumbnail(url= anime.poster)
        await ctx.send(embed=embed,view=view)  
    @anime.error
    async def anime_error(self, ctx:commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Cross:963039895922814996> | Please mention the name of an anime!",color=nextcord.Color.red()))        

    @commands.command(aliases=["CH","ch","cH","Ch","CHARACTER","Character"])
    async def character(self,ctx:commands.Context,*,query):
        try:
            char = animec.Charsearch(query)
        except:
            await ctx.reply(embed= nextcord.Embed(description="<a:S_Cross:963039895922814996> | No corresponding Anime Character was found for the search query!", color=nextcord.Color.red())) 
            return
        
        link=Button(label="Link to Character",url=char.url,style=ButtonStyle.link)
        view = View()
        view.add_item(link)            

        embed=nextcord.Embed(title=char.title,color=ctx.author.color)
        embed.set_image(url=char.image_url)
        embed.set_footer(text=", ".join(list(char.references.keys())[:2]))
        await ctx.send(embed=embed,view=view)        
    @character.error    
    async def character_error(self, ctx:commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Cross:963039895922814996> | Please mention the name of a character!",color=nextcord.Color.red()))      

    @commands.command(aliases=["WALLPAPER", "Wallpaper"])
    async def wallpaper(self,ctx):
            async def get_wallpaper():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://www.reddit.com/r/animewallpaper/new.json?sort=hot") as r:
                        res = await r.json()

                return res['data']['children'][random.randint(0, 25)]['data']['url']

            async def button1_callback(interaction):            
                wallpaper = await get_wallpaper()
                emb = interaction.message.embeds[0].set_image(url=wallpaper)
                await interaction.response.edit_message(embed=emb)
            async def button2_callback(interaction):
                await interaction.response.edit_message(view=disabled)    

            button1 = Button(label='Next Wallpaper', style=nextcord.ButtonStyle.green)
            button2 = Button(label='End Interaction', style=nextcord.ButtonStyle.gray)
            button3 = Button(label='Next Wallpaper', style=nextcord.ButtonStyle.green, disabled=True)
            button4 = Button(label='End Interaction', style=nextcord.ButtonStyle.gray, disabled=True)            
            view = View()
            disabled = View()
            button1.callback=button1_callback
            button2.callback=button2_callback
            view.add_item(button1) 
            view.add_item(button2)
            disabled.add_item(button3)
            disabled.add_item(button4)

            wallpaper = await get_wallpaper()
            embed = nextcord.Embed(title="New Wallpaper!", color=ctx.author.color)
            embed.set_image(url=await get_wallpaper())
            await ctx.reply(embed=embed,view=view)     

    @commands.command(aliases=["BLUSH","Blush"])
    async def blush(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        blush_names = ["blushed!! >///<","'s face is red!","has turned into a tomato!","is blushing!"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)    
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} blushed because of {original.author.name}!")
            embed.set_image(url=char.blush())
            embed.set_footer(text="How cuteeee :3")
            await ctx.send(embed=embed)   
            return
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(blush_names)}")
            em.set_image(url=char.blush())
            em.set_footer(text="How cuteeee :3")
            await ctx.send(embed=em)
            return
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} blushed because of {member.name}!")
            embed.set_image(url=char.blush())
            embed.set_footer(text="How cuteeee :3")
            await ctx.send(embed=embed)    
            return        

    @commands.command(aliases=["Cry","CRY"])
    async def cry(self, ctx:commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        cry_names = ["cries a river :'c","cries ;-;","is crying :'<","needs a hug..."]
    
        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)    
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} cried because of {original.author.name}!")
            embed.set_image(url=char.cry())
            embed.set_footer(text="Why u made them cry >:(")
            await ctx.send(embed=embed) 
            return            
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(cry_names)}")
            em.set_image(url=char.cry())
            em.set_footer(text="Who made them cry >:(")
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            em=nextcord.Embed(description= reason, color= member.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(cry_names)}")
            em.set_image(url=char.cry())
            em.set_footer(text="Who made them cry >:(")
            await ctx.send(embed=em)
            return            
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} cried because of {member.name}!")
            embed.set_image(url=char.cry())
            embed.set_footer(text="Why u made them cry >:(")
            await ctx.send(embed=embed)
            return 

    @commands.command(aliases=["WINK","Wink"])
    async def wink(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["is winking~","winked!"]
        mingle_wink = ["winks at","is winking at"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)    
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {original.author.name}!")
            embed.set_image(url=char.wink())
            embed.set_footer(text="Winky wink ;)")
            await ctx.send(embed=embed) 
            return            
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.wink())
            em.set_footer(text="Winky wink ;)")
            await ctx.send(embed=em)    
            return
        if member == ctx.author:
            em=nextcord.Embed(description= reason, color= member.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.wink())
            em.set_footer(text="Winky wink ;)")
            await ctx.send(embed=em)    
            return            
        else:    
            embed=nextcord.Embed(description= reason, color= ctx.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {member.name}!")
            embed.set_image(url=char.wink())
            embed.set_footer(text="Winky wink ;)")
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=["BULLY","Bully"])
    async def bully(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["bullied someone >:0","bullied!"]
        mingle_wink = ["bullies","bullied","is bullying"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)    
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {original.author.name}!")
            embed.set_image(url=char.bully())
            embed.set_footer(text="Bullying is not so gud.. '-'")
            await ctx.send(embed=embed) 
            return   
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.bully())
            em.set_footer(text="Bullying is not so gud.. '-'")
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.bully())
            em.set_footer(text="Bullying is not so gud.. '-'")
            await ctx.send(embed=em)
            return            
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {member.name}!")
            embed.set_image(url=char.bully())
            embed.set_footer(text="Bullying is not so gud.. '-'")
            await ctx.send(embed=embed)  
            return

    @commands.command(aliases=["CUDDLE","Cuddle"])
    async def cuddle(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["wants someone to cuddle with~","wants some cuddles :<"]
        mingle_wink = ["cuddles with","cuddled","is cuddling with"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {original.author.name}!")
            embed.set_image(url=char.cuddle())
            embed.set_footer(text="Awiee :3")
            await ctx.send(embed=embed)
            return         
        em=nextcord.Embed(description= reason, color= ctx.author.color)
        em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
        em.set_image(url=char.cuddle())
        em.set_footer(text="Awiee :3")
        if member == None:
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            await ctx.send(embed=em)  
            return  
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {member.name}!")
            embed.set_image(url=char.cuddle())
            embed.set_footer(text="Awiee :3")
            await ctx.send(embed=embed)
            return  

    @commands.command(aliases=["KILL","Kill"])
    async def kill(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        mingle_wink = ["killed","was killing","is killing"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {original.author.name}!")
            embed.set_image(url=char.kick())
            embed.set_footer(text="Nuu fightinggg >:(")
            await ctx.send(embed=embed)
            return  
        em=nextcord.Embed(description= reason, colour= ctx.author.color)
        em.set_author(name=f"{ctx.author.name} killed themselves!")
        em.set_image(url=char.kick())
        em.set_footer(text="Oofs :<")
        if member == None:
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            await ctx.send(embed=em)    
            return
        else:    
            embed=nextcord.Embed(description= reason, colour= member.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {member.name}!")
            embed.set_image(url=char.kick())
            embed.set_footer(text="Nuu fightinggg >:(")
            await ctx.send(embed=embed)   
            return              

    @commands.command(aliases=["HANDHOLD","Handhold"])
    async def handhold(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["wants to hold hands with someone~","wants someone to hold hands with :<"]
        mingle_wink = ["hold hands with","holded hands with","is holding hands with"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {original.author.name}!")
            embed.set_image(url=char.handhold())
            embed.set_footer(text="Awiee :3")
            await ctx.send(embed=embed)  
            return
        em=nextcord.Embed(description= reason, color= ctx.author.color)
        em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
        em.set_image(url=char.handhold())
        em.set_footer(text="I'll hold your handdd :3")
        if member == None:
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            await ctx.send(embed=em)  
            return  
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {member.name}!")
            embed.set_image(url=char.handhold())
            embed.set_footer(text="Awiee :3")
            await ctx.send(embed=embed)  
            return  

    @commands.command(aliases=["DANCE","Dance"])
    async def dance(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["wants someone to dance with someone~","wants someone to dance with :<"]
        mingle_wink = ["is dancing with","danced with"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {original.author.name}!")
            embed.set_image(url=char.dance())
            embed.set_footer(text="The moves tho >:3")
            await ctx.send(embed=embed)  
            return
        em=nextcord.Embed(description= reason, color= ctx.author.color)
        em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
        em.set_image(url=char.dance())
        em.set_footer(text="Lemme dance with you >:3")
        if member == None:
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            await ctx.send(embed=em)    
            return
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {member.name}!")
            embed.set_image(url=char.dance())
            embed.set_footer(text="The moves tho >:3")
            await ctx.send(embed=embed) 
            return

    @commands.command(aliases=["SMUG","Smug"])
    async def smug(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        mingle_wink = ["smugged to","is smugging to"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {original.author.name}!")
            embed.set_image(url=char.smug())
            embed.set_footer(text="Ouu 😏")
            await ctx.send(embed=embed)  
            return
        em=nextcord.Embed(description= reason, color= ctx.author.color)
        em.set_author(name=f"Something caused {ctx.author.name} to smug!")
        em.set_image(url=char.smug())
        em.set_footer(text="Ouu 😏")
        if member == None:
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            await ctx.send(embed=em)   
            return 
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(mingle_wink)} {member.name}!")
            embed.set_image(url=char.smug())
            embed.set_footer(text="Ouu 😏")
            await ctx.send(embed=embed)     
            return                                           

    @commands.command(aliases=["BITE","Bite"])
    async def bite(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()
        bite_gifs = ["https://cdn.discordapp.com/attachments/713915865375965224/713940461307297852/DC0OjkZsLW6.gif",
                     "https://cdn.discordapp.com/attachments/713915865375965224/713940467292569690/He-8cZ2smMP.gif",
                     "https://cdn.discordapp.com/attachments/713915865375965224/713940455749976164/9fFfgfq_3A4.gif"]
        bite_names = ["is biting","bites","bitted"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(bite_names)} {original.author.name}!")
            embed.set_image(url=char.bite())
            embed.set_footer(text="Ouch~ That hurts..")
            await ctx.send(embed=embed)  
            return
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} wants to bite something!")
            em.set_image(url=random.choice(bite_gifs))
            em.set_footer(text="S-Stay awayy '-'")
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} bitted themselves!")
            embed.set_image(url=char.bite())
            embed.set_footer(text="Ouch~ That hurts..")
            await ctx.send(embed=embed)  
            return           
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(bite_names)} {member.name}!")
            embed.set_image(url=char.bite())
            embed.set_footer(text="Ouch~ That hurts..")
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=["Cringe","CRINGE"])
    async def cringe(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["is cringing hard!","cringed~"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{original.author.name} caused {ctx.author.name} to cringe!")
            embed.set_image(url=char.cringe())
            embed.set_footer(text="It was cringe >:p")
            await ctx.send(embed=embed)
            return
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.cringe())
            em.set_footer(text="It was cringe >:p")
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} cringed at themselves!")
            em.set_image(url=char.cringe())
            em.set_footer(text="It was cringe >:p")
            await ctx.send(embed=em)
            return            
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{member.name} caused {ctx.author.name} to cringe!")
            embed.set_image(url=char.cringe())
            embed.set_footer(text="It was cringe >:p")
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=["HAPPY","Happy"])
    async def happy(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["is happy!","is very happy~"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{original.author.name} made {ctx.author.name} happy!")
            embed.set_image(url=char.happy())
            embed.set_footer(text="That's niceee :3")
            await ctx.send(embed=embed)
            return
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.happy())
            em.set_footer(text="That's niceee :3")
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.happy())
            em.set_footer(text="That's niceee :3")
            await ctx.send(embed=em)   
            return         
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{member.name} made {ctx.author.name} happy!")
            embed.set_image(url=char.happy())
            embed.set_footer(text="That's niceee :3")
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=["SMILE","Smile"])
    async def smile(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["is smiling!","smiled~"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)            
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{original.author.name} made {ctx.author.name} smile!")
            embed.set_image(url=char.happy())
            embed.set_footer(text="You look cutee :3")
            await ctx.send(embed=embed)       
            return
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.happy())
            em.set_footer(text="You look cutee :3")
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} {random.choice(single_wink)}")
            em.set_image(url=char.happy())
            em.set_footer(text="You look cutee :3")
            await ctx.send(embed=em)       
            return     
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{member.name} made {ctx.author.name} smile!")
            embed.set_image(url=char.happy())
            embed.set_footer(text="You look cutee :3")
            await ctx.send(embed=embed) 
            return           

    @commands.command(aliases=["Highfive","HIGHFIVE"])
    async def highfive(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        
        highfive = ["gave a highfive to","highfives","highfives with"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)         
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(highfive)} {original.author.name}!")
            embed.set_image(url=char.highfive())
            embed.set_footer(text="Highfivesss!!")
            await ctx.send(embed=embed)
            return             
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"Someone gave {ctx.author.name} a highfive!")
            em.set_image(url=char.highfive())
            em.set_footer(text="Highfivesss!!")
            await ctx.send(embed=em)
            return
        else:    
            embed=nextcord.Embed(description= reason, color= member.color)
            embed.set_author(name=f"{ctx.author.name} {random.choice(highfive)} {member.name}!")
            embed.set_image(url=char.highfive())
            embed.set_footer(text="Highfivesss!!")
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=["BONK","Bonk"])
    async def bonk(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        

        single_wink = ["is getting bonked by","got bonked by"]

        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)   
            embed=nextcord.Embed(description= reason, color= original.author.color)
            embed.set_author(name=f"{original.author.name} {random.choice(single_wink)} {ctx.author.name}!")
            embed.set_image(url=char.bonk())
            embed.set_footer(text="Oops~")
            await ctx.send(embed=embed)
            return              
        if member == None:
            em=nextcord.Embed(description= reason, color= ctx.author.color)
            em.set_author(name=f"{ctx.author.name} bonked themselves..")
            em.set_image(url=char.bonk())
            em.set_footer(text="Oops~")
            await ctx.send(embed=em)
            return
        if member == ctx.author:
            em=nextcord.Embed(description= reason, color= member.color)
            em.set_author(name=f"{ctx.author.name} bonked themselves..")
            em.set_image(url=char.bonk())
            em.set_footer(text="Oops~")
            await ctx.send(embed=em)   
            return         
        else:    
            embed=nextcord.Embed(description= reason, color= ctx.author.color)
            embed.set_author(name=f"{member.name} {random.choice(single_wink)} {ctx.author.name}!")
            embed.set_image(url=char.bonk())
            embed.set_footer(text="Oops~")
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=["SLAP","Slap"])
    async def slap(self, ctx: commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()
        slaps = ["slapped", "is slapping", "slaps"]

        selfslap=nextcord.Embed(description= reason, color=ctx.author.color)
        selfslap.set_author(name=f"{ctx.author.name} is slapping themselves!")
        selfslap.set_image(url="https://cdn.discordapp.com/attachments/728925291644190730/737146559732514956/slap1.gif")
        selfslap.set_footer(text="Just why tho..")
        if member == ctx.author:
            await ctx.send(embed=selfslap)
            return
        if member == None:
            await ctx.send(embed=selfslap)
            return    
        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)     
            slapEmbed=nextcord.Embed(description= reason, color=original.author.color)
            slapEmbed.set_author(name=f"{ctx.author.name} {(random.choice(slaps))} {original.author.name}!")
            slapEmbed.set_image(url=char.slap())
            slapEmbed.set_footer(text="You kinda deserved it..")
            await ctx.send(embed=slapEmbed)   
            return                     
        else:    
            slapEmbed=nextcord.Embed(description= reason, color=member.color)
            slapEmbed.set_author(name=f"{ctx.author.name} {(random.choice(slaps))} {member.name}!")
            slapEmbed.set_image(url=char.slap())
            slapEmbed.set_footer(text="You kinda deserved it..")
            await ctx.send(embed=slapEmbed)
            return

    @commands.command(aliases=["HUG","Hug"])
    async def hug(self, ctx:commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()
        hugs = ["hugs", "gives a hug to", "is hugging"]  

        selfhugs = ["https://c.tenor.com/UQKg3vQJsbkAAAAC/grabby-hand-anime-i-want-attention.gif",
                    "https://c.tenor.com/JEF0J3lnj98AAAAC/hestia-anime.gif",
                    "https://c.tenor.com/JSc-J4cBaWIAAAAC/kotarou-pay-attention.gif"]
        
        selfhug=nextcord.Embed(description= reason, color= ctx.author.color)
        selfhug.set_author(name=f"{ctx.author.name} want some hugs!")
        selfhug.set_image(url=(random.choice(selfhugs)))
        selfhug.set_footer(text="dw you're loved <3")
        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)     
            hugEmbed=nextcord.Embed(description= reason, color=original.author.color)
            hugEmbed.set_author(name=f"{ctx.author.name} {(random.choice(hugs))} {original.author.name}!")
            hugEmbed.set_image(url=char.hug())
            hugEmbed.set_footer(text="Aww you got a hug!")
            await ctx.send(embed=hugEmbed)     
            return           
        if member == ctx.author:
            await ctx.send(embed=selfhug)
            return
        if member == None:
            await ctx.send(embed=selfhug)
            return                             
        else:    
            hugEmbed=nextcord.Embed(description= reason, color=member.color)
            hugEmbed.set_author(name=f"{ctx.author.name} {(random.choice(hugs))} {member.name}!")
            hugEmbed.set_image(url=char.hug())
            hugEmbed.set_footer(text="Aww you got a hug!")
            await ctx.send(embed=hugEmbed)   
            return

    @commands.command(aliases=["Kiss","KISS"])
    async def kiss(self, ctx:commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()
        kiss_names = ["kissed", "is kissing", "kisses"]
        selfkiss_gifs = ["https://c.tenor.com/vberBgo__S4AAAAC/naruko-anime.gif",
                         "https://images-ext-1.discordapp.net/external/d8mL1A7ANJEUkch7XcXj9O6foC_pVVNCeiEBgR3J7EU/https/media1.tenor.com/images/f948190a4904f066c2bd65eebbe4278c/tenor.gif",
                         "https://c.tenor.com/kUZh6lmPu90AAAAd/anime-elbow-kiss.gif"]
        selfkiss=nextcord.Embed(description= reason, color= ctx.author.color)
        selfkiss.set_author(name=f"{ctx.author.name} want some kisses!")
        selfkiss.set_image(url=(random.choice(selfkiss_gifs)))
        selfkiss.set_footer(text="Being single is sometimes nice thou..")
        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id)    
            kissEmbed=nextcord.Embed(description= reason, color=original.author.color)
            kissEmbed.set_author(name=f"{ctx.author.name} {(random.choice(kiss_names))} {original.author.name}!")
            kissEmbed.set_image(url=char.kiss())
            kissEmbed.set_footer(text="Lewd people..'-'")
            await ctx.send(embed=kissEmbed)     
            return              
        if member == ctx.author:
            await ctx.send(embed=selfkiss)
            return
        if member == None:
            await ctx.send(embed=selfkiss)
            return                      
        else:    
            kissEmbed=nextcord.Embed(description= reason, color=member.color)
            kissEmbed.set_author(name=f"{ctx.author.name} {(random.choice(kiss_names))} {member.name}!")
            kissEmbed.set_image(url=char.kiss())
            kissEmbed.set_footer(text="Lewd people..'-'")
            await ctx.send(embed=kissEmbed)            
            return  

    @commands.command(aliases=["Pat","PAT"])
    async def pat(self, ctx:commands.Context, member:nextcord.Member=None, *, reason=""):
        char = animec.waifu.Waifu()        
        pat_names = ["pats", "is patting", "patted"]
        selfpat=nextcord.Embed(description= reason, color= ctx.author.color)
        selfpat.set_author(name=f"{ctx.author.name} want some pats..")
        selfpat.set_image(url="https://cdn.discordapp.com/attachments/728925291644190730/737122101634531338/pat.gif")
        selfpat.set_footer(text="Someone please pat..'-'")
        if ctx.message.reference:
            original = await ctx.channel.fetch_message(ctx.message.reference.message_id) 
            patEmbed=nextcord.Embed(description= reason, color=original.author.color)
            patEmbed.set_author(name=f"{ctx.author.name} {(random.choice(pat_names))} {original.author.name}!")
            patEmbed.set_image(url=char.pat())
            patEmbed.set_footer(text="Aww you got a pat!")
            await ctx.send(embed=patEmbed) 
            return           
        if member == ctx.author:
            await ctx.send(embed=selfpat)   
            return
        if member == None:
            await ctx.send(embed=selfpat)
            return                      
        else:    
            patEmbed=nextcord.Embed(description= reason, color=member.color)
            patEmbed.set_author(name=f"{ctx.author.name} {(random.choice(pat_names))} {member.name}!")
            patEmbed.set_image(url=char.pat())
            patEmbed.set_footer(text="Aww you got a pat!")
            await ctx.send(embed=patEmbed)   
            return 

    @commands.command(aliases=["Waifu","WAIFU"])
    async def waifu(self, ctx):
        char = animec.waifu.Waifu()
        em = nextcord.Embed(title="A waifu appeared!", color=ctx.author.color)
        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)       
        em.set_image(url=char.waifu())
        await ctx.reply(embed=em)

    @commands.command(aliases=["Neko","NEKO"])
    async def neko(self, ctx):
        char = animec.waifu.Waifu()
        em = nextcord.Embed(title="A neko appeared!", color=ctx.author.color)
        em.set_image(url=char.neko())
        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.reply(embed=em)

    @commands.command(aliases=["Awoo","AWOO"])
    async def awoo(self, ctx):
        char = animec.waifu.Waifu()
        em = nextcord.Embed(title="Hear the awooo~", color=ctx.author.color)
        em.set_image(url=char.awoo())
        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.reply(embed=em)                         

def setup(client):
    client.add_cog(Anime(client))        
    print("✅ | Anime cog ready!")  
    print("---------------------------")          