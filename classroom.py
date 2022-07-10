import asyncio
import discord
import os
from discord.ext import commands


class Classroom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx, channel_name):
        guild = ctx.guild
        await guild.create_text_channel(channel_name)
        await ctx.send(f"Channel {channel_name} has been created")
        await asyncio.sleep(10)
        await ctx.invoke(self.bot.get_command("delete"), channel_name=channel_name)

    @commands.command()
    async def delete(self, ctx, channel_name):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        await channel.delete()
        await ctx.send(f"Channel {channel_name} has been deleted")
