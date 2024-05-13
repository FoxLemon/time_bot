# Libaray
from discord import *
from functions.balanceFun import *
from discord.ext import commands

# check the balance of the one who call the command
@commands.hybrid_command()
async def balance(ctx: Message) -> None:
    # Description
    """Checks your balance"""
    # Function variable
    uid: str = str(ctx.author.id)
    name: str = str(ctx.author)
    check_user(uid,name)
    data: dict = user_data()
    #send message
    await ctx.send(f"{data[uid]["name"]} have {data[uid]["balance"]} in balance, and {data[uid]["green_token_balance"]} green tokens")

# check the balance of the user user wanted
@commands.hybrid_command()
async def balanceof(ctx: Message, user: Member) -> None:
    # Description
    """Checks the balance of another user"""
    # Function variable
    uid: str = str(user.id)
    name: str = str(user.name)
    check_user(uid,name)
    data: dict = user_data()
    #send message
    await ctx.send(f"{data[uid]["name"]} have {data[uid]["balance"]} in balance, and {data[uid]["green_token_balance"]} green tokens")

# pay the other user
@commands.hybrid_command()
async def pay(ctx: Message, user: Member, amount: int) -> None:
    # Description
    """Pay the other user"""
    # Check
    check_user(str(ctx.author.id),str(ctx.author))
    check_user(str(user.id),str(user.name))
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
    # await ctx.send(f"@{user.name.capitalize()} you have received ${amount} from {ctx.author} ")

async def setup(bot):
    bot.add_command(balance)
    bot.add_command(balanceof)
    bot.add_command(pay)