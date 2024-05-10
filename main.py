# Library
import os
import discord
from typing import Final
from dotenv import load_dotenv                                      #pip install python-dotenv
from discord import *                                               #pip install discord
from discord.ext import commands
from base_functions import *

# Environment Setup
load_dotenv()
TOKEN: Final[str] = os.getenv("BOT_TOKEN")
ID_AU: Final[list] = os.getenv("AUTHORIZED_USER_ID").split(",")
ID_AC: Final[int] = int(os.getenv("ANNOUNCEMENT_CHANNEL_ID"))
ID_S: Final[str] = os.getenv("SERVER_ID")
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
async def on_message(ctx: Message) -> None:
    if ctx.author.bot:
        return
    
    # Function variable
    uid: str = str(ctx.author.id)
    user_name: str = str(ctx.author)

    # coin minning
    if mine(uid,user_name):
        # send announcement to the announcement channel
        announcement_channel = client.get_channel(ID_AC)
        if announcement_channel:
            await announcement_channel.send(f"🎉 <@{uid}> has minted a Green Token!")

@tree.command(
    name="balance",
    description="tell you your balance.")
async def balance(inter: Interaction) -> None:
    user = user_data()["user"][str(inter.user.id)]
    await inter.response.send_message(f"{user['name']} have {user['balance']} in balance, and {user['green_token_balance']} green tokens")


# Main entry point
def main() -> None:
    client.run(token=TOKEN)
if __name__ == "__main__":
    main()