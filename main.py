import discord
import os
from dotenv import load_dotenv
load_dotenv()

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.message_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
   name="Bookmark Message"
)
async def bookmark(
    ctx,
    message: discord.Message
):
    await ctx.respond(f"🔖 Bookmarked!", ephemeral=True)
    embed = discord.Embed(title="<:mdibookmark:1311457777834528768> Bookmark", description=f"{message.content}", color=discord.Colour.random())
    embed.add_field(name="<:mdiaccount:1311490376091045989> Author", value=f"<@{message.author.id}>", inline=True)
    embed.add_field(name="<:mdilinkvariant:1311490590747267082> Link", value=f"{message.jump_url}", inline=True)
    embed.set_thumbnail(url=f"{message.author.avatar.url}")
    await ctx.user.send(embed=embed)
    for i in message.attachments:
        await ctx.user.send(i)

if __name__ == "__main__":
    bot.run(str(os.getenv('TOKEN'))) # run the bot with the token
