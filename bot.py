import discord
from discord.ext import commands

import sqlite3

client = commands.Bot(command_prefix='!')

client.remove_command("help")

@client.command()
async def say(ctx, *, say: str):
    await ctx.send(f"{say}")

client.run('ODA5ODYzMjgyNTk2NzczODg5.YCbR9Q.3vS01PjyMi7LJvvx-Q6vq5zQ77M')