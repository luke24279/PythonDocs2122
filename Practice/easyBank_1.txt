# Luke Thompson, easyBanks_1
import basics

app = basics.newProgram()

user = basics.newUser()



app.balance = 1000

while app.running :
    print("Your Balance Is:", app.balance)
    user.choice = input("1 to deposit, 2 to withdraw, 3 to leave.")
    if user.choice == ("1"):
        userDeposit = input("How much do you want to deposit?")
        userDeposit = int(userDeposit)
        app.balance += userDeposit
    elif user.choice == ("2"):
        userWithdraw = input("How muc would you like to withdraw?")
        userWithdraw = int(userWithdraw)
        if userWithdraw > app.balance:
            print("You do not have enough money to do this action.")
        else :
            app.balance -= userWithdraw
    elif user.choice == ("3") :
        app.running = False
    else :
        print("Your choice was invalid. Please try again.")







