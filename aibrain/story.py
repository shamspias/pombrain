import discord
from discord.ext import commands
from discord.ext.commands import Context
from utils import song as song_brain
from helpers import checks


class SongWriter(commands.Cog, name="songwriter"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.hybrid_command(
        name="writesong",
        aliases=["write_song", "song_write", "ws", "sw"],
        description="To Write song with GPT-3",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    @checks.is_owner()
    async def write_song(self, context: Context, *, topic: str) -> None:
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        :param topic: The topic that should be song title given by the user.
        """
        op_song = song_brain.normal_song(topic)
        embed = discord.Embed(
            title=topic,
            description=op_song,
            color=0x9C84EF
        )

        await context.send(embed=embed)

    # And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.


async def setup(bot):
    await bot.add_cog(SongWriter(bot))
