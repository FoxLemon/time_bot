# Library
import json

# Varable
data = r"" #path to your data file

# Load user_balance and return an dict
def user_data() -> dict:
    file: str = open(data,"r").read()
    return json.loads(file)
# Save the new balance by over writing the old balance
def save_data(new_data: dict) -> None:
    old_data = open(data,"w")
    json.dump(new_data,old_data,indent=4)
# Set up a new data in the json file for new user
def new_user_data(uid: str,user_name: str) -> None:
    new_user = user_data()
    new_user["users"][uid] = dict()
    new_user["users"][uid]["name"] = user_name
    new_user["users"][uid]["balance"] = 1
    new_user["users"][uid]["green_token_balance"] = 0
    new_user["users"][uid]["message_multiplier"] = 1
    save_data(new_user)