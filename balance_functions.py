# Library
import json

# Varable
balance = "user_balances"

# Load user_balance and return an dict
def user_balance() -> dict:
    with open(balance,"r") as file:
        return json.loads(file)
# save the new balance by over writing the old balance
def save_balance(new_balance: dict) -> None:
    with open(balance,"w") as old_balance:
        json.dump(new_balance,old_balance,indent=2)
