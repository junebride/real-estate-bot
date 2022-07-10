import os
from discord.ext import commands
from dotenv import load_dotenv
from room import Room

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')

@bot.command()
async def stop(ctx):
    await bot.close()

bot.add_cog(Room(bot))
bot.run(TOKEN)
