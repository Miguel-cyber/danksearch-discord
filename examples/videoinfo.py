"""

Please Don't use this example now, it is in development


"""
from discord.ext import commands
import danksearch
from danksearch import Video
danksearch.SAFESEARCH=True
danksearch.USEPAFY=True 
client=commands.Bot(command_prefix="bob!")
@client.event
async def on_ready():
    await client.wait_until_ready()
    print("Running")
@client.command()
async def videoinfo(ctx, *, query):
    video=Video()
    await video.search(query)
    await ctx.send(f"""
    Title: {video.data.title}
    Ratings: {video.data.rating}
    Views: {video.data.viewcount}
    Likes: {video.data.likes}
    Dislikes: {video.data.dislikes}
    Description: ```{video.data.description}```
    """)
print("ok")
client.run("TOKEN")