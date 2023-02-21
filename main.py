import discord
import os
import dotenv
from colorama import Back, Style


# load .env file 
dotenv.load_dotenv()
# get token from environnement variable
TOKEN = str(os.getenv("TOKEN"))

# create bot, Bot() supports slash commands instead of Client()
bot = discord.Bot()

# import all cogs
all_modules = os.listdir("modules")
for module in all_modules:
    if module.endswith(".py"):
        bot.load_extension(f"modules.{module[:-3]}")

#when the bot is ready
@bot.event
async def on_ready():
    print(f"{Back.GREEN}[Status]{Style.RESET_ALL} Logged in as {bot.user}")

#when a message is sent
@bot.event
async def on_message(message):
    # ignore messages from the bot itself
    if message.author == bot.user:
        return

# run bot
bot.run(TOKEN)
