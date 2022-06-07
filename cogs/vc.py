import nextcord
from nextcord.ext import commands

class VC(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = self.client.get_guild(961167197101756416)
        if after.channel != None:
            if after.channel.id == 972318355673477170:
                    maincategory = nextcord.utils.get(
                        guild.categories, id=972318352880054362)
                    channel2 = await guild.create_voice_channel(name=f'{member.display_name}', category=maincategory)
                    await channel2.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                    await member.move_to(channel2)
                    await member.edit(nick=f"[👑] {member.display_name}")                

                    def check(x, y, z):
                        return len(channel2.members) == 0
                    await self.client.wait_for('voice_state_update', check=check)
                    await channel2.delete()    
                    await member.edit(nick=f"{member.name}")          

def setup(client):
    client.add_cog(VC(client))        
    print("✅ | VC cog ready!")  
    print("---------------------------")           