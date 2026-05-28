balance=float(input("Enter your starting balance: "))

while True:
    choice = input("What do you want to do? (deposit/withdraw/exit): ")
    
    if choice == "deposit":
        amount = float(input("How much do you want to deposit? "))
        balance = balance + amount
        print("Your new balance is " + str(balance))
        
    elif choice == "withdraw":
        amount = float(input("How much do you want to withdraw? "))
        if amount > balance:
            print("You dont have enough money!")
        else:
            balance = balance - amount
            print("Your new balance is " + str(balance))
            
    elif choice == "exit":
        print("Your final balance is " + str(balance))
        break
        
    else:
        print("Invalid input! Please type deposit, withdraw or exit")