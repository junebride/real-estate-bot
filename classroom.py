import asyncio
import discord
from discord.ext import commands


class Classroom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready!")

    @commands.group(name="classroom", invoke_without_command=True)
    async def classroom(self, ctx):
        await ctx.send("Calling classroom")

    @classroom.command()
    async def create(self, ctx, channel_name, seconds=10):
        category= ctx.channel.category
        
        await ctx.guild.create_text_channel(channel_name, category=category)
        await ctx.send(f"Channel {channel_name} has been created")
        await asyncio.sleep(seconds)
        await ctx.invoke(self.classroom.get_command("delete"), channel_name=channel_name)

    @classroom.command()
    async def delete(self, ctx, channel_name):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        await channel.delete()
        await ctx.send(f"Channel {channel_name} has been deleted")
