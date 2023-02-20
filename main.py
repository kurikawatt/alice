import discord
import os
import dotenv

# load .env file 
dotenv.load_dotenv()
# get token from environnement variable
TOKEN = str(os.getenv("TOKEN"))

# create bot, Bot() supports slash commands instead of Client()
bot = discord.Bot()



# run bot
bot.run(TOKEN)
