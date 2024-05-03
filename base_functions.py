# Library
from discord import *
from balance_functions import *

# Variable
u_data: dict = user_data()

# Mining function
def mine(user_id: str,message: Message) -> None:
    if message.guild:
        
