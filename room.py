import asyncio
from discord.ext import commands


class Room(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready!")

    @commands.group(name="room", invoke_without_command=True)
    async def room(self, ctx):
        await ctx.send("Calling room")

    @room.command()
    async def create(self, ctx, channel_name):
        category = ctx.channel.category

        await ctx.guild.create_text_channel(channel_name, category=category)
        await ctx.send(f"Channel {channel_name} has been created")

    @room.command()
    async def create_temp(self, ctx, channel_name, seconds=10):
        await ctx.invoke(self.room.get_command("create"), channel_name=channel_name)
        await asyncio.gather(self.warning(ctx, seconds), self.deleting(ctx, channel_name, seconds))

    async def warning(self, ctx, seconds):
        await asyncio.sleep(seconds - 5)
        await ctx.send("Deleting in 5 seconds")

    async def deleting(self, ctx, channel_name, seconds):
        await asyncio.sleep(seconds)
        await ctx.invoke(self.room.get_command("delete"), channel_name=channel_name)

    @room.command()
    async def delete(self, ctx, channel_name):
        channels = list(filter(lambda x: x.name ==
                        channel_name, ctx.guild.channels))

        if len(channels) == 0:
            await ctx.send(f"No channel found with the name {channel_name}")
            return

        for channel in channels:
            await channel.delete()
            await ctx.send(f"Channel {channel_name} has been deleted")
