#-Libaray-----------------------------------------------------------------------------
import os
from dotenv import load_dotenv
#-------------------------------------------------------------------------------------

#-varables----------------------------------------------------------------------------
    # The Bot Token from Discord.
TOKEN: str = os.getenv("BOT_TOKEN")
    # The Channel ID where announcements (Minted Green Tokens, Milestones, Lottery, etc..)
ANNOUNCEMENT_ID: int = 1235996734056824892
    # The ID of the user that should have access to admin commands.
ADMINS: list = []
    # ID of the server that the bot should be in.
SERVER_ID: str =""
    # The chance that a Green Token will be minted when a user sends a message.
    # This chance is out of 1000
GREEN_TOKEN_CHANCE: int = 10
    # The price of a single lottery ticket
LOTTERY_TICKET_PRICE: int = 5
#-------------------------------------------------------------------------------------