# Libaray
from discord import *
from functions.balanceFun import *
from discord.ext import commands

# The balance_cmd group
class balance_cmd(app_commands.Group):
# check the balance of the one who call the command
    @app_commands.command(name="balance", description="Checks your balance.")
    async def balance(self, inter: Interaction) -> None:
        # Function variable
        uid: str = str(inter.user.id)
        name: str = str(inter.user.name)
        check_user(uid,name)
        data: dict = user_data()
        #send message
        await inter.response.send_message(f"{data[uid]["name"]} have {data[uid]["balance"]} in balance, and {data[uid]["green_token_balance"]} green tokens")

    # check the balance of the user user wanted
    @app_commands.command(name="balanceof", description="Checks the balance of another user.")
    async def balanceof(self, inter: Interaction, user: Member) -> None:
        # Function variable
        uid: str = str(inter.user.id)
        name: str = str(inter.user.name)
        check_user(uid,name)
        data: dict = user_data()
        #send message
        await inter.response.send_message(f"{data[uid]["name"]} have {data[uid]["balance"]} in balance, and {data[uid]["green_token_balance"]} green tokens")

    # pay the other user
    @app_commands.command(name="pay", description="Pay the other user.")
    async def pay(self, inter: Interaction, user: Member, amount: int ) -> None:
        # Check
        check_user(str(inter.user.id),str(inter.user.name))
        check_user(str(user.id),str(user.name))
        # Function variable
        data: dict = user_data()
        # balance out from:
        bOut: dict = data[str(inter.user.id)]
        # balance in to:
        bIn: dict = data[str(user.id)]
        # transaction
        if bOut["balance"] < amount:
            await inter.response.send_message(f"payment failed, you do not have enough money.")
            return
        bOut["balance"] -= amount
        bIn["balance"] += amount
        save_data(data)
        #send message to the payer
        await inter.response.send_message(f"you've payed {user.name} ${amount}")
        #send message to the receiver
        await user.send(f"you have received ${amount} from {inter.user.name}.")

    # pay the other user with green token
    @app_commands.command(name="greentran", description="Pay the other user with green token.")
    async def greentran(self, inter: Interaction, user: Member, amount: int) -> None:
        # Check
        check_user(str(inter.user.id),str(inter.user.name))
        check_user(str(user.id),str(user.name))
        # Function variable
        data: dict = user_data()
        # balance out from:
        bOut: dict = data[str(inter.user.id)]
        # balance in to:
        bIn: dict = data[str(user.id)]
        # transaction
        if bOut["balance"] < amount:
            await inter.response.send_message(f"payment failed, you do not have enough green tokens.")
            return
        bOut["balance"] -= amount
        bIn["balance"] += amount
        save_data(data)
        #send message to the payer
        await inter.response.send_message(f"you've payed {user.name} {amount} green tokens.")
        #send message to the receiver
        await user.send(f"you have received {amount} green tokens from {inter.user.name}.")

# Entry point
async def setup(bot):
    group = balance_cmd(name="balance_cmd",description="consist of balance related commands")
    bot.tree.add_command(group)