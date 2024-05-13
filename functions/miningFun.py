# Library
from discord import *
from functions.balanceFun import *
from random import randint
import setting

# Mining function
def mine(ctx: Message) -> bool:
    # function variable
    uid: str = str(ctx.author.id)

    # check if user exist and load data
    check_user(uid,str(ctx.author))
    data: dict = user_data()

    # Add the coin mined to the user balance
    data[uid]["balance"] += data[uid]["message_multiplier"]

    # Green token mining
    if randint(1,1000) <= setting.GREEN_TOKEN_CHANCE:
        data[uid]["green_token_balance"] += 1
        return True
    
    # Save data changes
    save_data(data)
    return False