import os
from discord.ext import commands
from dotenv import load_dotenv
from classroom import Classroom

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')

@bot.command()
async def stop(ctx):
    await bot.close()

bot.add_cog(Classroom(bot))
bot.run(TOKEN)
