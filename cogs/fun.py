import nextcord, requests, os
from nextcord import client
from nextcord import *
import random
from nextcord.utils import get
from nextcord.ext import commands
from nextcord.ext.commands import bot
from random import choice
from nextcord import File, ButtonStyle
import asyncio
import aiohttp
import datetime
from bs4 import BeautifulSoup
from datetime import datetime
import json
import random
from nextcord.ui import Button, View
from nextcord import Embed
import simpcalc 
from simpcalc import simpcalc
import nekos          

class Fun(commands.Cog):
    """Some fun commands!"""
    def __init__(self,client):
        self.client=client  
        self.persistent_views_added = False   

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.persistent_views_added:
            self.client.add_view(InteractiveView())
            self.client.persistent_views_added = True

    @commands.command(aliases=["MEME","Meme"])
    async def meme(self,ctx):
        """Sends a MEME"""
        async def get_meme():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://www.reddit.com/r/memes/new.json?sort=hot") as r:
                    res = await r.json()

            return res['data']['children'][random.randint(0, 25)]['data']['url']

        async def button1_callback(interaction):            
            meme = await get_meme()
            emb = interaction.message.embeds[0].set_image(url=meme)
            await interaction.response.edit_message(embed=emb)
        async def button2_callback(interaction):
            await interaction.response.edit_message(view=disabled)    

        button1 = Button(label='Next Meme', style=nextcord.ButtonStyle.green)
        button2 = Button(label='End Interaction', style=nextcord.ButtonStyle.gray)
        button3 = Button(label='Next Meme', style=nextcord.ButtonStyle.green, disabled=True)
        button4 = Button(label='End Interaction', style=nextcord.ButtonStyle.gray, disabled=True)            
        view = View()
        disabled = View()
        button1.callback=button1_callback
        button2.callback=button2_callback
        view.add_item(button1) 
        view.add_item(button2)
        disabled.add_item(button3)
        disabled.add_item(button4)

        embed = nextcord.Embed(title='New Meme!', color=nextcord.Color.blue())
        embed.set_image(url=await get_meme())
        await ctx.reply(embed=embed,view=view)           

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        client.sniped_messages = {}        
        client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
    @commands.command(aliases=["SNIPE","Snipe"])
    async def snipe(self,ctx):
        """Shows the last deleted message"""
        try:
            contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
            
        except:
            await ctx.channel.send("Couldn't find a message to snipe!")
            return

        embed = nextcord.Embed(description=contents, color=nextcord.Color.random())
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar)

        await ctx.channel.send(embed=embed) 

    @commands.command(aliases=["TOPIC","Topic"])
    async def topic(self, ctx):
        """Sends a random topic"""
        topics = ['Who is your favourite actor?',
                'Are aliens real?',
                'Best anime?',
                'What was the last good book you read?',
                'Do you listen to any podcasts?',
                "What's your favorite holiday?",
                'Were you ever into fashion as a child or as a teenager?',
                "What's your favorite restaurant to go to?",
                "Would you go back in time if you were given the chance?",
                "What did you last eat?",
                'Do you have any pets?',
                "How much time do you spend watching sports in a week?",
                'What animal would you want to be reincarnated as?',
                'What country do you most want to travel to?',
                "What’s your favorite color?",
                "What’s your opinion on fate?",
                "What makes you anxious?",
                'What makes you angry?',
                "Do you have any siblings?",
                "How many languages can u speak?",
                "What's better, having high expectations or having low expectations?",
                'Favourite song?',
                "What have you recently become obsessed with?",
                "Dogs or cats? What would you choose and why?",
                "If you could cure a singles disease, which would you choose?",
                'Have you ever had a crush on a fictional character? If so, who?',
                'Do you believe in Bigfoot?',
                "Would you dress in drag for $25?",
                "What underrated anime would you recommend someone to watch?",
                'What skills do you posses that could help you survive the zombie apocalypse?',
                'Would you like to live to be 200 years old?',
                "Have you thrown up in a car?",
                'What would you rather throw away: Love or Money?',
                "What's the strangest thing in your refrigerator?",
                "What's your favorite TV show?",
                "What's one power you wished that you had?",
                "If you were invisible for a day, what would you choose to do with that power?",
                "What's your best memory?",
                "What do you look for in your partner?",
                "Is being negative person a bad thing?",
                "If you could be a model for any product, what would you choose and why?"]    
        await ctx.send(f'{random.choice(topics)}')              

    @commands.command(aliases=['8ball','8BALL','8Ball'])
    async def _8ball(self, ctx, *, question):
        """Sends a random answer to your question"""
        responses = ['🎱 It is certain.',
                    '🎱 It is decidedly so.',
                    '🎱 Without a doubt.',
                    '🎱 Oh cmon, you know it is a yes.',
                    "🎱 Oh cmon, you know it's a no.",
                    '🎱 Yes, definetly.',
                    '🎱 You may rely on it.',
                    '🎱 As I see it, yes.',
                    '🎱 Most likely.',
                    '🎱 Outlook good.',
                    '🎱 Yes.',
                    '🎱 Signs point to yes.',
                    '🎱 Reply hazy, try again.',
                    '🎱 Ask again later.',
                    '🎱 Better not tell you now.',
                    "🎱 Don't count on it.",
                    '🎱 My reply is no.',
                    '🎱 No.',
                    '🎱 Outlook not so good.',
                    '🎱 Very doubtful.',
                    "🎱 It's secret.",
                    "🎱 I don't care lol."]
        await ctx.reply(f'{random.choice(responses)}')

    @commands.command(aliases=["Emojify","EMOJIFY"])
    async def emojify(self, ctx,*,text):
        """Converts text to emoji"""
        emojis = []
        for s in text.lower():
            if s.isdecimal():
                num2emo = {'0':'zero','1':'one','2':'two',
                        '3':'three','4':'four','5':'five',
                        '6':'six','7':'seven','8':'eight','9':'nine'}
                emojis.append(f':{num2emo.get(s)}:')
            elif s.isalpha():
                emojis.append(f':regional_indicator_{s}:')
            else:
                emojis.append(s)
        await ctx.send(' '.join(emojis))         

    @commands.command(aliases=["UWUIFY","Uwuify"])
    async def uwuify(self, ctx, member:nextcord.Member):
        """Uwuifies the given member's name"""
        smileys = [';;w;;', '^w^', '>w<', '(*^ω^)','UwU', '(・`ω\´・)', '(´・ω・\`)','(◕ᴥ◕)','(◕‿◕✿)',' ღ(U꒳Uღ)','(◡ ሠ ◡)','( ᴜ ω ᴜ )','(ㅅꈍ ˘ ꈍ)','(˘ε˘)']        
        marks = ["??!","?!?","!!?",'!?!','!??','?!!']
        if member.bot == True:
            await ctx.send("You cannot uwuify a bot!")
        else:    
            await member.edit(nick=nekos.owoify(member.display_name))
            await ctx.send(f"{member.mention}'s name has been uwuified{random.choice(marks)} {random.choice(smileys)}")

    @commands.command(aliases=["Why","WHY"])
    async def why(self, ctx):
        """Sends a random WHY question"""
        await ctx.reply(nekos.why())

    @commands.command(aliases=["Name","NAME"])
    async def name(self, ctx):
        """Sends a random name"""
        await ctx.reply(nekos.name())

    @commands.command(aliases=["Fact","FACT"])
    async def fact(self, ctx):
        """Sends a random fact"""
        await ctx.reply(nekos.fact())        

    @commands.command(help="Send top 3 news")                   
    async def news(self, ctx):
        url = 'https://www.bbc.com/news'                               #URL for news
        response = requests.get(url)                                   

        soup = BeautifulSoup(response.text, 'html.parser')

        links = []

        for a in soup.select("[class~=gs-c-promo-heading]",href=True):
            links.append("https://www.bbc.com"+ a['href'])              #Add links to news article

        await ctx.send(f"{links[1]}\n{links[2]}\n{links[13]}\n")  

    @commands.command(name="calculate", aliases=["Calculate","CALCULATE","Calc","calc","CALC"])
    async def interactive_calc(self, ctx):
        """Shows you the calculator"""
        view = InteractiveView()
        await ctx.send(embed = nextcord.Embed(title=f"Calculator!", description="", color=nextcord.Color.blue()),view=view)        

class InteractiveView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.expr = ""
        self.calc = simpcalc.Calculate() # if you are using the above function, no need to declare this!    

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="1", row=0, custom_id="1")
    async def one(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "1"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="2", row=0, custom_id="2")
    async def two(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "2"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="3", row=0, custom_id="3")
    async def three(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "3"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, label="×", row=0, custom_id="*")
    async def multiply(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "*"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.red, label="Exit", row=0, custom_id="Exit")
    async def _exit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        for child in self.children:
            child.disabled=True
        self.expr = "Calculator Closed!"
        await interaction.message.edit(embed = nextcord.Embed(title=self.expr,color=nextcord.Color.blue()), view=self)        

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="4", row=1, custom_id="4")
    async def last(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "4"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="5", row=1, custom_id="5")
    async def five(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "5"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="6", row=1, custom_id="6")
    async def six(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "6"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, label="÷", row=1, custom_id="/")
    async def divide(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
            self.expr += "/"
            await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.red, label="🠀", row=1, custom_id="Back")
    async def back(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr = self.expr[:-1]
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))            

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="7", row=2, custom_id="7")
    async def seven(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "7"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="8", row=2, custom_id="8")
    async def eight(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "8"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="9", row=2, custom_id="9")
    async def nine(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "9"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, label="+", row=2, custom_id="+")
    async def plus(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "+"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.red, label="Clear", row=2, custom_id="lol")
    async def clear(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr = ""
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))                   

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="00", row=3, custom_id="00")
    async def doublezero(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr = "00"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label="0", row=3, custom_id="0")
    async def zero(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "0"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))

    @nextcord.ui.button(style=nextcord.ButtonStyle.grey, label=".", row=3, custom_id=".")
    async def dot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "."
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))   

    @nextcord.ui.button(style=nextcord.ButtonStyle.blurple, label="-", row=3, custom_id="-")
    async def minus(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.expr += "-"
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue()))             

    @nextcord.ui.button(style=nextcord.ButtonStyle.green, label="=", row=3, custom_id="=")
    async def equal(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        try:
            self.expr = await self.calc.calculate(self.expr)
        except errors.BadArgument: # if you are function only, change this to BadArgument
            return await interaction.response.send_message("Um, looks like you provided a wrong expression....", ephemeral=True)
        await interaction.message.edit(embed = nextcord.Embed(title=f"Calculator!", description=self.expr, color=nextcord.Color.blue())) 

def setup(client):
    client.add_cog(Fun(client))        
    print("✅ | Fun cog ready!")
    print("---------------------------")        