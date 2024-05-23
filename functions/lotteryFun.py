# Library
import json
from discord import *
from functions.balanceFun import *
from random import choice

# Variable
lottery_data = r"C:\Users\zhang\OneDrive\Documents\time_bot\data_base\lottery_data.txt" #path to your lottery_data file

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
    "status": False,
    "involvement": {},
    "prize_pool": 0,
    "tickets": [],
    "tickets_tracking": 0
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

# get the winner on the lottery
def get_winner() -> int:
    data: dict = load_lottery()
    try:
        winning_ticket = choice(data["tickets"])
    except IndexError:
        return 0
    for people in data["involvement"]:
        if winning_ticket in data["involvement"][str(people)]["tickests_owned"]:
            return int(people) # return the id of ther person winned