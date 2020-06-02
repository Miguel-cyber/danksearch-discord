from discord.ext import commands
import danksearch
from danksearch import Video
danksearch.SAFESEARCH=True
client=commands.Bot(command_prefix="!")
@client.command()
async def youtube(ctx, *, query):
    video=Video()
    await video.search(query)
    await ctx.send(video.url)
client.run("TOKEN")