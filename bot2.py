from discord.ext import commands
import discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def run():
    
    @bot.event
    async def on_message(message: discord.Message):
        
        
        content = message.content 
        channel = message.channel
        mentions = message.mentions

        print(mentions)
        for i in range(0,len(mentions)):
            if "thank" in content:
                await message.channel.send("{} was thanked".format(mentions[i].mention))
        
    #run the bot with your token
    bot.run('MTEzMzM1NDE4Mjk3MjI4NTAyOQ.Gj6khd.BfkXA-tmTttYQ4wBKVlTZ_ccfLGvH0vTYGs-dU')


run()