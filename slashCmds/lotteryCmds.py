# Libaray
from discord import *
from functions.balanceFun import *
from discord.ext import commands
from functions.balanceFun import *
from functions.lotteryFun import *
from main import is_owner
import setting

# The lottery command group
class lottery_cmd(app_commands.Group):
    # Starts a lottery
    @app_commands.command(name= "startlottery", description="starts a lottary event.(Owner only)")
    @app_commands.check(is_owner)
    async def startlottery(self, inter: Interaction) -> None:
        # Function variable
        data: dict = load_lottery()
        # Check if there is a lottery event happening 
        if data["status"]:
            await inter.response.send_message(f"There is already a lottery event going on")
        else:
            # starts the lottery event
            data["status"] = True
            announcement_channel = utils.get(inter.guild.channels,id=setting.ANNOUNCEMENT_ID)
            if announcement_channel:
                await announcement_channel.send(f"@everyone A new lottery event has started.")
            save_lottery(data)

    # Ends the lottery
    @app_commands.command(name= "endlottery", description="ends the lottary event.(Owner only)")
    @app_commands.check(is_owner)
    async def endlottery(self, inter: Interaction) -> None:
        # Function variable
        data: dict = load_lottery()
        user: dict = user_data()
        announcement_channel = utils.get(inter.guild.channels,id=setting.ANNOUNCEMENT_ID)
        # if there is a lottery going on or not
        if data["status"] == False:
            await inter.response.send_message(f"There is not a lottery going on currently.")
            return
        # getting the winner
        winner = get_winner()
        # if there is a winner
        if winner != 0:
            # give the user the prize pool
            user[str(winner)]["balance"] += data["prize_pool"]
            save_data(user)
            # send the result to announcement
            if announcement_channel:
                await announcement_channel.send(f"@everyone The lottery event has ended.")
                await announcement_channel.send(f"@everyone The winner is {user[str(winner)]["name"]}!!!")
            await inter.response.send_message(f"lottery ended", ephemeral=True)
            reset_lottery()
        else:
            if announcement_channel:
                await announcement_channel.send(f"@everyone The lottery event has ended.")
                await announcement_channel.send(f"Nobody have won this lottery cause of lack of participation.")
            reset_lottery()
            
    
    # letting people to buy tickets
    @app_commands.command(name= "buylotterytickets", description="buy a number of lottery tickes in the current lottery event.")
    async def buylotterytickets(self, inter: Interaction, amount: int) -> None:
        # Function variables
        data: dict = load_lottery()
        users: dict = user_data()
        userBal: dict = users[str(inter.user.id)]
        # check if a lottery is happening
        if data["status"] == False:
            await inter.response.send_message(f"There is not a lottery going on currently.")
            return
        # buying the ticket
        cost: int = amount*setting.LOTTERY_TICKET_PRICE
        current_ticket: int = data["tickets_tracking"] + 1
        if userBal["balance"] < cost:
            await inter.response.send_message(f"payment failed, you are {cost - userBal["balance"]} short.")
            return
        data["prize_pool"] += cost
        userBal["balance"] -= cost
        check_lottery_involvement(str(inter.user.id),str(inter.user.name))
        for i in range(current_ticket,current_ticket+amount):
            data["involvement"][str(inter.user.id)]["tickests_owned"].append(i)
            data["tickets_tracking"] += 1
            data["tickets"].append(i)
        save_data(users)
        save_lottery(data)
        await inter.response.send_message(f"you have bought {amount} lottery tickets")

# Entry point
async def setup(bot):
    group = lottery_cmd(name="lottery_cmd",description="consist of lottery related commands.")
    bot.tree.add_command(group)