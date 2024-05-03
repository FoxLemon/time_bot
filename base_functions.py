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
ID_AC: Final[list] = os.getenv("ANNOUNCEMENT_CHANNEL_ID").split(",")

# Mining function
def mine(uid: str,user_name: str) -> None:
    # set up the data for new user
    if uid not in data["users"]:
        new_user_data(uid,user_name)
    
    # Function variables (for easier programming & easier understaning)
    balance = data["users"][uid]["balance"]
    message_multiplier = data["users"][uid]["message_multiplier"]
    green_token_balance = data["user"][uid]["green_token_balance"]

    # Add the coin mined to the user balance
    balance += message_multiplier

    # Green token mining
    if randint(1,1000) <= GTC:
        green_token_balance += 1
        for ac_id in ID_AC:
            announcement_channel = client.get_channel(ac_id)
            if announcement_channel:
                announcement_channel.send(f"🎉 <@{uid}> has minted a Green Token!")
    
    # Save data changes
    save_data(data)