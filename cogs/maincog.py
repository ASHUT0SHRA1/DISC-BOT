import discord

from discord.ext import commands
from discord_components import DiscordComponents
from song_download import get_song

class ARS_BOT(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready to rock and roll")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("hello"):
            await message.channel.send("bye bye")

    @commands.Cog.listener()
    async def on_member_join(self, member):

        channel = self.client.get_channel(962715491930099754)
        if channel:
            await channel.self("welcome to the server of ARS {}".format(member.mention))
        await member.send("welcome to coding club:)")

    @commands.command()
    async def hello(self, ctx, arg):
        await  ctx.send('Hi {}'.format(ctx.message.author.name)+str(arg))

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("please connect to voice channel !!")
        else:
            channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await channel.connect()
            else:
                await ctx.voice_client.move_to(channel)

    @commands.command()
    async def play(self, ctx, *args):
        keyword = list(args)
        get_song(keyword=keyword)
        await self.join(ctx)
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_clients.stop()
        else:
            source = discord.FFmpegAudio("songs.mp3")
            ctx.voice_client.play(source)


    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("paused!")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("resumed")

    @commands.command()
    async def stop(self,ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("stopped")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = " no reason provided"
        await ctx.guild.kick(member)
        await ctx.send(f'User {member.mention} has been kicked for {reason}')


def setup(client):
    client.add_cog(ARS_BOT(client))
