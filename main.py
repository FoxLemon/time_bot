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
    await bot.tree.sync()
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

# check the balance of the one who call the command
@bot.command()
async def balance(ctx: Message) -> None:
    # Description
    """Checks your balance"""
    # Function variable
    check_user(ctx)
    data: dict = user_data()
    uid: str = str(ctx.author.id)
    #send message
    await ctx.send(f"{data[uid]["name"]} have {data[uid]["balance"]} in balance, and {data[uid]["green_token_balance"]} green tokens")

# check the balance of the user user wanted
@bot.command()
async def balanceof(ctx: Message,user: Member) -> None:
    # Description
    """Checks the balance of another user"""
    # Function variable
    check_user(ctx)
    data: dict = user_data()
    uid: str = str(user.id)
    #send message
    await ctx.send(f"{data[uid]["name"]} have {data[uid]["balance"]} in balance, and {data[uid]["green_token_balance"]} green tokens")

# pay the other user
@bot.command()
async def pay(ctx: Message, user: Member, amount: int) -> None:
    # Description
    """Pay the other user"""
    # Function variable
    data: dict = user_data()
    # balance out from:
    bOut: dict = data[str(ctx.author.id)]
    # balance in to:
    bIn: dict = data[str(user.id)]
    # transaction
    bOut["balance"] -= amount
    bIn["balance"] += amount
    save_data(data)
    #send message to the payer
    await ctx.send(f"you've payed {user.name} ${amount}")
    #send message to the receiver
    await ctx.send(f"@{user.name.capitalize()} you have received ${amount} from {ctx.author} ")

    

# Main entery point
def main() -> None:
    bot.run(token=setting.TOKEN)
if __name__ == "__main__":
    main()