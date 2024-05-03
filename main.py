# Library
import os
from typing import Final
from dotenv import load_dotenv                                      #pip install python-dotenv
from discord import *                                               #pip install discord
from base_functions import *

# Environment Setup
load_dotenv()
TOKEN: Final[str] = os.getenv("BOT_TOKEN")
ID_AU: Final[list] = os.getenv("AUTHORIZED_USER_ID").split(",")
ID_AC: Final[list] = os.getenv("ANNOUNCEMENT_CHANNEL_ID").split(",")
ID_S: Final[str] = os.getenv("SERVER_ID")
GTC: Final[int] = int(os.getenv("GREEN_TOKEN_CHANCE"))
LTP: Final[int] = int(os.getenv("LOTTERY_TICKET_PRICE"))

# Bot setup
intents: Intents = Intents.all()
intents.message_content = True
client: Client = Client(intents=intents)
tree = app_commands.CommandTree(client)

# Handling bot start up
@client.event
async def on_ready() -> None:
    await tree.sync(guild=Object(id=ID_S))
    print(f"Logged in as {client.user.name} succesfully!")

# On message event
@client.event
async def on_message(message: Message) -> None:
    if message.author.bot:
        return
    uid: str = str(message.author.id)
    mine(uid,message)