from discord.ext import commands as cmd
import discord
from typing import Optional

class Ping(cmd.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @discord.slash_command(name="ping")
    async def ping(self, ctx:cmd.Context) -> None:
        await ctx.respond(f"Pong in {self.bot.latency}!")

# when loaded, setup will load the cog (slash commands) to the main script
def setup(bot):
    bot.add_cog(Ping(bot))
    print("[Modules] Ping module loaded!")
