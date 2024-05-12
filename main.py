# Libaray
import setting
from discord import *
from discord.ext import commands
from functions.miningFun import mine

# Bot set up
intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)

# Handling bot start up
@bot.event
async def on_ready() -> None:
    await bot.tree.sync()
    print(f"Logged in as {bot.user.name} succesfully!")

# On message events: mining etc...
@bot.event
async def on_message(ctx: Message):
    if ctx.author.bot: return

    # Mining
    if mine(ctx):
        # send announcement to the announcement channel
        announcement_channel = bot.get_channel(setting.ANNOUNCEMENT_ID)
        if announcement_channel:
            await announcement_channel.send(f"🎉 <@{ctx.author}> has minted a Green Token!")
    
# @bot.hybrid_command()
# async def ping(ctx):
#     await ctx.send_message("pong")

# Main entery point
def main() -> None:
    bot.run(token=setting.TOKEN, root_logger= True)
if __name__ == "__main__":
    main()