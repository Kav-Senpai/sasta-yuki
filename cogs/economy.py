import nextcord
from nextcord.ext.commands import cooldown, command
from nextcord.ext import commands
import os
import json
import random
from random import choice

class Economy(commands.Cog):

    def __init__(self,client):
        self.client = client  
    
    os.chdir('C:\\Users\\Naveen Bagotra\\Documents\\GitHub\\sasta-yuki')    

    mainshop = [{"name":"<@&978556685557833750>","price":"5,000,000","emoji":"<a:S_SnowStone:976808329076678686>"},
                {"name":"<@&978555585110872134> <@&978555580631367701> <@&978555595315634196> <@&978555589368086528>","price":"2,000,000","emoji":"<a:S_SnowStone:976808329076678686>"},
                {"name":"<@&978554836863815751> <@&978554832698892308> <@&978554820535398470>","price":"1,000,000","emoji":"<a:S_SnowStone:976808329076678686>"},                
                {"name":"<@&978308684318924830> <@&978553757518401587> <@&978308676131622992> <@&978308687888277576>","price":"500,000","emoji":"<a:S_SnowStone:976808329076678686>"},                
                {"name":"<@&978551261936885860> <@&978551211454234624> <@&978551184543580211> <@&978551157070917642> <@&978551234346745887>","price":"250,000","emoji":"<a:S_SnowStone:976808329076678686>"},
                {"name":"<@&955395667575046176> <@&955395423802126377> <@&955395643428470814> <@&955395654371397643> <@&955395156171956228> <@&955396048258498580>","price":"100,000","emoji":"<a:S_SnowStone:976808329076678686>"},                
                {"name":"<@&955395403271008256> <@&955395443393720370> <@&955395392076390410> <@&955395374716170291> <@&955395183145533500>","price":"50,000","emoji":"<a:S_SnowStone:976808329076678686>"},                
                {"name":"<@&955395970995195954> <@&955395167521738812> <@&955395178930241547> <@&955395991006240798> <@&955396028285210624>","price":"20,000","emoji":"<a:S_SnowStone:976808329076678686>"},                
                {"name":"<@&978549357009858571>","price":"10,000","emoji":"<a:S_SnowStone:976808329076678686>"}]
                
    @commands.command(aliases=["bal","BAL","BALANCE","Balance"])
    async def balance(self,ctx, member:nextcord.Member=None): 
        if member is None:        
            await self.open_account(ctx.author)
            user = ctx.author
            users = await self.get_bank_data()

            wallet_amt = users[str(user.id)]["wallet"]
            bank_amt = users[str(user.id)]["bank"]

            em = nextcord.Embed(color=ctx.author.color)
            em.set_author(name=f"{ctx.author.name}'s balance", icon_url=ctx.author.avatar)
            em.add_field(name="Wallet Balance", value=f"{wallet_amt} <a:S_SnowStone:976808329076678686>")
            em.add_field(name="Bank Balance", value=f"{bank_amt} <a:S_SnowStone:976808329076678686>")
            await ctx.reply(embed=em)
        else:
            await self.open_account(member)
            user = member
            users = await self.get_bank_data()

            wallet_amt = users[str(user.id)]["wallet"]
            bank_amt = users[str(user.id)]["bank"]

            em = nextcord.Embed(color=member.color)
            em.set_author(name=f"{member.name}'s balance", icon_url=member.avatar)
            em.add_field(name="Wallet Balance", value=f"{wallet_amt} <a:S_SnowStone:976808329076678686>")
            em.add_field(name="Bank Balance", value=f"{bank_amt} <a:S_SnowStone:976808329076678686>")
            await ctx.reply(embed=em)
    
    async def open_account(self,user):

        users = await self.get_bank_data()
        
        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 500

        with open("mainbank.json","w") as f:
            json.dump(users, f)
        return True    

    async def get_bank_data(self):
        with open("mainbank.json","r") as f:
            users = json.load(f)
        return users    

    async def update_bank(self,user,change = 0, mode="bank"):
        users = await self.get_bank_data()

        users[str(user.id)][mode] += change

        with open("mainbank.json","w") as f:
            json.dump(users,f)

        bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
        return bal    

    @commands.command(aliases=["with","WITH","WITHDRAW","Withdraw"])
    async def withdraw(self, ctx, amount = None):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        bal = await self.update_bank(ctx.author)    
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]    

        if amount == None:
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Warn:951397930961633291> **Please enter the amount to be withdrawn!**", color=nextcord.Color.red()))  
            return      
        if amount == "all":
            amount = bank_amt    

        amount = int(amount)
        if amount>bal[1]:
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Warn:951397930961633291> **You don't have enough money!**", color=nextcord.Color.red()))  
            return
        if amount<0:
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Warn:951397930961633291> **Please enter a positive amount!**", color=nextcord.Color.red()))  
            return         

        await self.update_bank(ctx.author, +1*amount, "wallet")
        await self.update_bank(ctx.author, -1*amount, "bank")

        em=nextcord.Embed(color=ctx.author.color)
        em.add_field(name="Withdrawn", value=f"`{amount}` <a:S_SnowStone:976808329076678686>", inline=False)
        em.add_field(name="Current Wallet Balance", value=f"`{wallet_amt+amount}` <a:S_SnowStone:976808329076678686>")
        em.add_field(name="Current Bank Balance", value=f"`{bank_amt-amount}` <a:S_SnowStone:976808329076678686>")
        await ctx.reply(embed=em)  

    @commands.command(aliases=["dep","DEP","DEPOSIT","Deposit"])
    async def deposit(self, ctx, amount = None):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        bal = await self.update_bank(ctx.author)
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]    

        if amount == None:
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Warn:951397930961633291> **Please enter the amount to be deposited!**", color=nextcord.Color.red()))  
            return      
        if amount == "all":
            amount = wallet_amt  

        amount = int(amount)
        if amount>bal[0]:
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Warn:951397930961633291> **You don't have enough money!**", color=nextcord.Color.red()))  
            return
        if amount<0:
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Warn:951397930961633291> **Please enter a positive amount!**", color=nextcord.Color.red()))  
            return         
        if bank_amt+amount > 10000000:
            await ctx.reply(embed=nextcord.Embed(description="<a:S_Warn:951397930961633291> **You cannot deposit more than 10M!**", color=nextcord.Color.red()))  
            return

        await self.update_bank(ctx.author, -1*amount, "wallet")
        await self.update_bank(ctx.author, +1*amount, "bank")

        em=nextcord.Embed(color=ctx.author.color)
        em.add_field(name="Deposited", value=f"`{amount}` <a:S_SnowStone:976808329076678686>", inline=False)
        em.add_field(name="Current Wallet Balance", value=f"`{wallet_amt-amount}` <a:S_SnowStone:976808329076678686>")
        em.add_field(name="Current Bank Balance", value=f"`{bank_amt+amount}` <a:S_SnowStone:976808329076678686>")
        await ctx.reply(embed=em) 

    @commands.command(aliases=["give","GIVE","SEND","Send","Give"])
    async def send(self, ctx, member:nextcord.Member=None, amount = None):
        await self.open_account(ctx.author)
        await self.open_account(member)
        user = ctx.author
        users = await self.get_bank_data()

        if member == None:
            await ctx.reply("Please ping a member!")
            return
        if member == ctx.author:
            await ctx.reply("You can't send money to yourself!")    
            return      

        bal = await self.update_bank(ctx.author)

        if amount == None:
            await ctx.reply("Please enter the amount!") 
            return      
        if amount == "all":
            amount = wallet_amt  

        amount = int(amount)
        if amount>bal[0]:
            await ctx.reply("You don't have that much money!")
            return
        if amount<0:
            await ctx.reply("Amount must be positive!")
            return         

        await self.update_bank(ctx.author, -1*amount, "wallet")
        await self.update_bank(member, +1*amount, "wallet")

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em=nextcord.Embed(color=member.color)
        em.add_field(name="You gave", value=f"`{amount}` <a:S_SnowStone:976808329076678686> to {member.mention}", inline=False)
        em.add_field(name="Current Wallet Balance", value=f"`{wallet_amt-amount}` <a:S_SnowStone:976808329076678686>")
        em.add_field(name="Current Bank Balance", value=f"`{bank_amt}` <a:S_SnowStone:976808329076678686>")
        await ctx.reply(embed=em)  

    @commands.command(aliases=["Beg","BEG"])
    @commands.cooldown(1, 40, commands.BucketType.user)
    async def beg(self,ctx):

        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        earnings = random.randrange(100)

        users[str(user.id)]["wallet"] += earnings
        em = nextcord.Embed(color=ctx.author.color, description=f"Someone gave you **{earnings}** <a:S_SnowStone:976808329076678686>", colour=ctx.author.color)
        await ctx.reply(embed=em)

        with open("mainbank.json","w") as f:
            json.dump(users, f)   
    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = nextcord.Embed(description=f'**Still on cooldown! Try after {error.retry_after:,.0f} seconds.**', color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar)
            await ctx.reply(embed=em)  

    @commands.command(aliases=["DAILY","Daily"])
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self,ctx):

        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        earnings = 1000

        users[str(user.id)]["wallet"] += earnings
        em = nextcord.Embed(color=nextcord.Color.green(), description=f"<a:S_Claimed:976839237800439858> **You have claimed your daily: {earnings}** <a:S_SnowStone:976808329076678686>")
        await ctx.reply(embed=em)

        with open("mainbank.json","w") as f:
            json.dump(users, f)   
    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timeLeft = round(error.retry_after)
            hoursLeft = timeLeft/3600
            hours = round(hoursLeft)
            em = nextcord.Embed(description=f'**Already claimed! Try again in {hours} hours.**', color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar)
            await ctx.reply(embed=em) 

    @commands.command(aliases=["HOURLY","Hourly"])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def hourly(self,ctx):

        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        earnings = 200

        users[str(user.id)]["wallet"] += earnings
        em = nextcord.Embed(color=nextcord.Color.green(), description=f"<a:S_Claimed:976839237800439858> **You have claimed your hourly: {earnings}** <a:S_SnowStone:976808329076678686>")
        await ctx.reply(embed=em)

        with open("mainbank.json","w") as f:
            json.dump(users, f)   
    @hourly.error
    async def hourly_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timeLeft = round(error.retry_after)
            minutesLeft = timeLeft/60
            minutes = round(minutesLeft)
            em = nextcord.Embed(description=f'**Already claimed! Try again in {minutes} minutes.**', color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar)
            await ctx.reply(embed=em)              

    @commands.command(aliases=["WORK","Work"])
    @commands.cooldown(1, 18000, commands.BucketType.user)
    async def work(self,ctx):
        works = ["worked hard and got",
                 "grinded and received",
                 "hugged Miku! Aww here is what you get",
                 "did a fist bomb with Miku and earned",
                 "gave a highfive to Miku and got"]

        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        earnings = random.randrange(800)

        users[str(user.id)]["wallet"] += earnings
        em = nextcord.Embed(color=nextcord.Color.green(), description=f"<a:S_Claimed:976839237800439858> **{ctx.author.mention} {random.choice(works)} {earnings}** <a:S_SnowStone:976808329076678686>")
        await ctx.reply(embed=em)

        with open("mainbank.json","w") as f:
            json.dump(users, f)   
    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timeLeft = round(error.retry_after)
            minutesLeft = timeLeft/3600
            minutes = round(minutesLeft)
            em = nextcord.Embed(description=f"**Don't work too hard! Try again in {minutes} hours.**", color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar)
            await ctx.reply(embed=em)   

    @commands.command(aliases=["BAKE","Bake"], pass_context=True)
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def bake(self,ctx):
        members = [m for m in ctx.guild.members if str(m.status) != "offline" or not m.bot]
        target = random.choice(members)
        food = ["pie 🥧",
                "cake 🍰",
                "bread 🥖",
                "burger 🍔",
                "pizza 🍕",
                "cookie 🍪"]    

        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        earnings = random.randrange(1000)

        users[str(user.id)]["wallet"] += earnings
        em = nextcord.Embed(color=ctx.author.color, description=f"You baked a {random.choice(food)} for {target.mention} <a:S_Love:977929410214776893> . . .\n They love you for being so thoughtful and gave you {earnings} <a:S_SnowStone:976808329076678686>! <3")
        await ctx.reply(embed=em)

        with open("mainbank.json","w") as f:
            json.dump(users, f)   
    @bake.error
    async def bake_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timeLeft = round(error.retry_after)
            minutesLeft = timeLeft/60
            minutes = round(minutesLeft)
            em = nextcord.Embed(description=f'**You can use this command again after {minutes} minutes.**', color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar)
            await ctx.reply(embed=em)

    @commands.command(aliases=["ROB","Rob"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def rob(self, ctx, member:nextcord.Member=None):
        await self.open_account(member)
        await self.open_account(ctx.author)

        bal = await self.update_bank(member)

        if bal[0]<5000:
            await ctx.reply(embed=nextcord.Embed(description=f"{member.name} does not even have 5000 <a:S_SnowStone:976808329076678686> in their wallet! Its not worth it.", color=nextcord.Color.red()))
            return

        earnings = random.randrange(0, bal[0])

        await self.update_bank(ctx.author, +1*earnings, "wallet")
        await self.update_bank(member, -1*earnings, "wallet")

        await ctx.reply(embed=nextcord.Embed(title=f"{member.name} was robbed!", description=f"You managed to steal {earnings} <a:S_SnowStone:976808329076678686>", color=member.color))

        em=nextcord.Embed(color=nextcord.Color.red(), title=f"You have been stolen from!", description=f"**{ctx.author.name}#{ctx.author.discriminator}** ({ctx.author.mention}) has stolen {earnings} <a:S_SnowStone:976808329076678686> from your wallet!")
        em.set_footer(text="Tip~ Snowstones cannot get stolen when in mainbank!")
        await member.send(embed=em)
    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = nextcord.Embed(description=f'**You can use this command again after {error.retry_after:,.0f} seconds!**', color=nextcord.Color.red())
            em.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar)
            await ctx.reply(embed=em)        

    @commands.command(aliases=["lb","Lb","LB","LEADERBOARD","Leaderboard"])
    async def leaderboard(self, ctx, x=10):
        users = await self.get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total, reverse=True)

        em=nextcord.Embed(color=ctx.author.color, title="Top 10 richest people!")
        em.set_author(icon_url=ctx.author.avatar, name=ctx.guild.name)
        em.set_thumbnail(url=ctx.guild.icon)
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = self.client.get_user(id_)
            name = member.name
            em.add_field(name= f"{index}. {name}", value=amt, inline=False) 
            if index == x:
                break
            else:
                index += 1
        await ctx.send(embed=em)      

    @commands.command(aliases=["Shop","SHOP"])
    async def shop(self, ctx):
        em = nextcord.Embed(color=ctx.author.color, title="Yuki Café Role Shop")
        em.set_footer(text="Yuki Café | .buy <rolename>", icon_url=ctx.guild.icon)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/961610704060829696/979650967509291008/unknown.png")

        for item in self.mainshop:
            name = item["name"]
            price = item["price"]
            emoji = item["emoji"]
            em.add_field(name=f"{price} {emoji}", value=f"> {name}", inline=False)
        await ctx.send(embed=em)

    @commands.command(aliases=["Buy","BUY"])
    async def buy(self, ctx, role):
        await self.open_account(ctx.author)
        bal = await self.update_bank(ctx.author)

        if role == "DJ":
            role = nextcord.utils.get(ctx.guild.roles, id=978549357009858571)
            if bal[0]<10000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 10000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You  successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")

        if role == "Jellal":
            role = nextcord.utils.get(ctx.guild.roles, id=955395970995195954)
            if bal[0]<20000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 20000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")

        if role == "Saitama":
            role = nextcord.utils.get(ctx.guild.roles, id=955395167521738812)
            if bal[0]<20000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 20000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")

        if role == "Stella":
            role = nextcord.utils.get(ctx.guild.roles, id=955395178930241547)
            if bal[0]<20000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 20000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")

        if role == "Gintoki":
            role = nextcord.utils.get(ctx.guild.roles, id=955395991006240798)
            if bal[0]<20000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 20000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")  

        if role == "Yuu.Kashima":
            role = nextcord.utils.get(ctx.guild.roles, id=955396028285210624)
            if bal[0]<20000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 20000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Neko.Girl":
            role = nextcord.utils.get(ctx.guild.roles, id=955395403271008256)
            if bal[0]<50000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 50000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Avenger":
            role = nextcord.utils.get(ctx.guild.roles, id=955395443393720370)
            if bal[0]<50000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 50000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Cosplayer":
            role = nextcord.utils.get(ctx.guild.roles, id=955395392076390410)
            if bal[0]<50000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 50000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Shion":
            role = nextcord.utils.get(ctx.guild.roles, id=955395374716170291)
            if bal[0]<50000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 50000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 
        
        if role == "Yoruichi":
            role = nextcord.utils.get(ctx.guild.roles, id=955395183145533500)
            if bal[0]<50000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 50000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Geass":
            role = nextcord.utils.get(ctx.guild.roles, id=955395667575046176)
            if bal[0]<100000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 100000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Tsundere":
            role = nextcord.utils.get(ctx.guild.roles, id=955395423802126377)
            if bal[0]<100000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 100000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Maid":
            role = nextcord.utils.get(ctx.guild.roles, id=955395643428470814)
            if bal[0]<100000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 100000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")    

        if role == "Holostar":
            role = nextcord.utils.get(ctx.guild.roles, id=955395654371397643)
            if bal[0]<100000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 100000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")  

        if role == "Alchemist":
            role = nextcord.utils.get(ctx.guild.roles, id=955395156171956228)
            if bal[0]<100000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 100000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")  

        if role == "Detective":
            role = nextcord.utils.get(ctx.guild.roles, id=955396048258498580)
            if bal[0]<100000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 100000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Sakura":
            role = nextcord.utils.get(ctx.guild.roles, id=978551261936885860)
            if bal[0]<250000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 250000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")  

        if role == "Titan":
            role = nextcord.utils.get(ctx.guild.roles, id=978551211454234624)
            if bal[0]<250000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 250000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Sharingan":
            role = nextcord.utils.get(ctx.guild.roles, id=978551184543580211)
            if bal[0]<250000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 250000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")    

        if role == "Chive.Bloom":
            role = nextcord.utils.get(ctx.guild.roles, id=978551157070917642)
            if bal[0]<250000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 250000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")                                                                                                 

        if role == "Chika":
            role = nextcord.utils.get(ctx.guild.roles, id=978551234346745887)
            if bal[0]<250000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 250000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")    

        if role == "Jeagerist":
            role = nextcord.utils.get(ctx.guild.roles, id=978308684318924830)
            if bal[0]<500000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 500000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")   

        if role == "Valentine":
            role = nextcord.utils.get(ctx.guild.roles, id=978553757518401587)
            if bal[0]<500000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 500000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")   

        if role == "Pirate.King":
            role = nextcord.utils.get(ctx.guild.roles, id=978308676131622992)
            if bal[0]<500000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 500000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Soul.Reaper":
            role = nextcord.utils.get(ctx.guild.roles, id=978308687888277576)
            if bal[0]<500000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 500000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")                                                                                                                                                 

        if role == "Bunny.Girl":
            role = nextcord.utils.get(ctx.guild.roles, id=978554836863815751)
            if bal[0]<1000000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 1000000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")  

        if role == "Jujutsu.Sorcerer":
            role = nextcord.utils.get(ctx.guild.roles, id=978554832698892308)
            if bal[0]<1000000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 1000000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Curse":
            role = nextcord.utils.get(ctx.guild.roles, id=978554820535398470)
            if bal[0]<1000000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 1000000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Ackerman":
            role = nextcord.utils.get(ctx.guild.roles, id=978555585110872134)
            if bal[0]<2000000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 2000000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet") 

        if role == "Darling":
            role = nextcord.utils.get(ctx.guild.roles, id=978555580631367701)
            if bal[0]<2000000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 2000000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")  

        if role == "Sukuna":
            role = nextcord.utils.get(ctx.guild.roles, id=978555595315634196)
            if bal[0]<2000000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 2000000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")    

        if role == "Hashira":
            role = nextcord.utils.get(ctx.guild.roles, id=978555589368086528)
            if bal[0]<2000000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy** {role.mention}", color=nextcord.Color.red()))
                return            
            amount = 2000000    
            if role in ctx.author.roles:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You already have the role** {role.mention}", color=nextcord.Color.red()))
            else:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Tick_yuki:981140827579502632> **You successfully bought the role** {role.mention}", color=nextcord.Color.green()))
                await ctx.author.add_roles(role)
            await self.update_bank(ctx.author, -1*amount, "wallet")                                                                                                                                                                                                                           

        if role == "CUSTOM.ROLE":
            if bal[0]<5000000:
                await ctx.reply(embed=nextcord.Embed(description=f"<:Cross_yuki:981141014016307310> **You dont have enough money in your wallet to buy a custom role**", color=nextcord.Color.red()))
                return             
            em=nextcord.Embed(title="Yayy! You managed to get the top role!", description=f"To get your Custom Role dm an <@&947771896320114699> the screenshot of this message!", color=ctx.author.color)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/948067148037767188/981482286052696124/980751170454835230.gif")               
            em.set_footer(text="Your money has been deducted from your wallet!", icon_url=ctx.author.avatar)
            amount = 5000000    
            await self.update_bank(ctx.author, -1*amount, "wallet") 
            await ctx.reply(embed=em)                          

def setup(client):
    client.add_cog(Economy(client))        
    print("✅ | Economy cog ready!")  
    print("---------------------------")          