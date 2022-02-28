import discord, os
from discord.ext import commands

#Client
client = commands.Bot(
    command_prefix = '$',
    help_command=None,
    self_bot=True
)

#Register Events
@client.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('logged in as {}'.format(client.user))
    
@client.command()
async def stream(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/TWITCHURL", 
    )
    await client.change_presence(activity=stream)
    await ctx.message.edit(content='Your streaming status: {}'.format(message))

client.run("TOKEN", bot=False, reconnect=True)
