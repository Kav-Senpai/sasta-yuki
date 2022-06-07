import nextcord
from nextcord.ext import commands

class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Uncomment line 26 for printing debug
        print(error)

        # Bot does not have permission
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Bot Permission Missing!')

def setup(client):
    client.add_cog(Errors(client))   
    print("✅ | Errors cog ready!")
    print("---------------------------")             