# Libaray
import setting
from discord import *
from discord.ext import commands
from functions.miningFun import mine
from functions.balanceFun import *

# Bot set up
intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)

# Handling bot start up
@bot.event
async def on_ready() -> None:
    for cmd_file in setting.CMDS_DIR.glob("*.py"):
        if cmd_file.name != "__init__.py":
            await bot.load_extension(f"slashCmds.{cmd_file.name[:-3]}")
    bot.tree.copy_global_to(guild=setting.GUILD_ID)
    await bot.tree.sync(guild=setting.GUILD_ID)
    print(f"Logged in as {bot.user.name} succesfully!")

# On message events: mining etc...
@bot.event
async def on_message(ctx: Message) -> None:
    if ctx.author.bot: return
    # Mining
    if mine(ctx):
        # send announcement to the announcement channel
        announcement_channel = bot.get_channel(setting.ANNOUNCEMENT_ID)
        if announcement_channel:
            await announcement_channel.send(f"🎉 <@{ctx.author}> has minted a Green Token!")
    
    # command running
    await bot.process_commands(ctx)

# Main entery point
def main() -> None:
    bot.run(token=setting.TOKEN)
if __name__ == "__main__":
    main()