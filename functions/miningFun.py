# Library
from typing import Final
from discord import *
from functions.balanceFun import *
from random import randint
import setting

# Variable
data: dict = user_data()

# Mining function
def mine(ctx: Message) -> bool:
    # function variable
    uid: str = str(ctx.author.id)
    name: str = str(ctx.author)
    
    # set up the data for new user
    if uid not in data["users"]:
        new_user_data(uid,name)

    # Add the coin mined to the user balance
    data["users"][uid]["balance"] += data["users"][uid]["message_multiplier"]

    # Green token mining
    if randint(1,1000) <= setting.GREEN_TOKEN_CHANCE:
        data["users"][uid]["green_token_balance"] += 1
        return True
    
    # Save data changes
    save_data(data)
    return False