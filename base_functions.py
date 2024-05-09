# Library
import os
from typing import Final
from discord import *
from balance_functions import *
from dotenv import load_dotenv
from random import randint

# Variable
load_dotenv()
data: dict = user_data()

# Environment Setup
GTC: Final[int] = int(os.getenv("GREEN_TOKEN_CHANCE"))

# Mining function
def mine(uid: str,user_name: str) -> bool:
    # set up the data for new user
    if uid not in data["users"]:
        new_user_data(uid,user_name)

    # Add the coin mined to the user balance
    data["users"][uid]["balance"] += data["users"][uid]["message_multiplier"]

    # Green token mining
    if randint(1,1000) <= GTC:
        data["users"][uid]["green_token_balance"] += 1
        return True
    
    # Save data changes
    save_data(data)
    return False