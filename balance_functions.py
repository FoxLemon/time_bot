# Library
import json

# Varable
balance = "user_balances"

# Load user_balance and return an dict
def user_balance() -> dict:
    with open(balance,"r") as file:
        return json.loads(file)
# 