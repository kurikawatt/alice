from discord.ext import commands as cmd
import discord
from typing import Optional
from colorama import Back, Style

class Lookup(cmd.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @discord.slash_command(name="lookup", description="Return the user pinged information")
    async def lookup(self, ctx:cmd.Context, user:Optional[discord.Member]) -> None:
        if user is None:
            user = ctx.author
        embed = discord.Embed(title=f"User information for {user.name}", color=0x103a9c)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.add_field(name="User", value=f"<@{user.id}>", inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="Server related information", value="", inline=False)
        embed.add_field(name="Nickname", value=user.nick, inline=True)
        embed.add_field(name="Highest role", value=user.top_role, inline=True)
        join_info = f"{user.joined_at.strftime('%d/%m/%Y')} ({user.joined_at.strftime('%H:%M:%S')})"
        embed.add_field(name="Member since", value=join_info, inline=True)
        embed.set_thumbnail(url=user.avatar)
        await ctx.respond(embed=embed)

# when loaded, setup will load the cog (slash commands) to the main script
def setup(bot):
    bot.add_cog(Lookup(bot))
    print(f"{Back.BLUE}[Modules]{Style.RESET_ALL} Lookup module loaded!")