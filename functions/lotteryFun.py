# Library
import json
from discord import *
from balanceFun import *

# Variable
lottery_data = r"" #path to your lottery_data file

# Load lottery and return an dict
def load_lottery() -> dict:
    file: str = open(lottery_data,"r").read()
    return json.loads(file)

# Save the new data by over writing the old data
def save_lottery(new_data: dict) -> None:
    old_data = open(lottery_data,"w")
    json.dump(new_data,old_data,indent=4)

# reset the lottery data file
def reset_lottery()-> None:
    default_data = {
        "lottery status": False,
    "involvement" : {},
    "prize pool" : 0,
    "tickets" : [],
    "tickets tracking" : 0
    }
    save_lottery(default_data)

# Add a user to the involvement
def add_lottery_involvement(uid: str, name: str) -> None:
    data = load_lottery()
    data["involvement"][uid] = dict()
    data["involvement"][uid]["name"] = name
    data["involvement"][uid]["tickests_owned"] = []
    save_lottery(data)

# Set up a new data for use if there aren't data about that user
def check_lottery_involvement(uid: str,name: str) -> None:
    data = load_lottery()
    if uid not in data["involvement"]:
        add_lottery_involvement(uid,name)