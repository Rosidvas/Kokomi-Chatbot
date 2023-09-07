
import discord
from discord import app_commands
from Main import analyze_Message

intents = discord.Intents.default()
intents.message_content = True

def message_respond(user, content):

    response = analyze_Message(user, content)
    return response
    

    
class MyClient(discord.Client):
    
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self) ## Will be used for Slash commands

    async def on_ready(self):

        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        user = message.author
        username = user.nick if user.nick else user.name
        content = message.content

        if user.bot:
            return
        
        response = message_respond(username, content)

        print(response)

        if response != False:
            
            await message.channel.send(response)
            

client = MyClient(intents=intents)
client.run('')

