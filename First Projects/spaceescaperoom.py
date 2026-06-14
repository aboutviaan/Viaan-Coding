import random

oxygen = 100

while True:
    print(" SPACE ESCAPE ROOM ")
    print("Oxygen:", oxygen, "%")
    print("1. Search room")
    print("2. Hack door")
    print("3. Check oxygen")
    print("4. Quit")

    
    oxygen -= 5

    if oxygen <= 0:
        print(" You ran out of oxygen... GAME OVER.")
        break

    choice = input("Choose an option: ")

    if choice == "1":
        print("You search the room...")

        event = random.choice([
            "You found a tool ",
            "Nothing useful...",
            "You found an oxygen canister  (+15 oxygen)"
        ])

        print(event)

        if "oxygen" in event:
            oxygen += 15

    elif choice == "2":
        print("You attempt to hack the door...")

        hack = random.choice(["success","fail"])

        if hack == "success":
            print("Door unlocked! ")
            print("YOU ESCAPED!! ")
            break
        else:
            print("Hack failed! System shock  (-10 oxygen)")
            oxygen -= 10

    elif choice == "3":
        print("Oxygen level:", oxygen, "%")

    elif choice == "4":
        print("Game exited. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")