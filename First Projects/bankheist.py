import random

money = 0
suspicion = 0

while True:

    if suspicion >= 75:
        print(" You got caught by the police!")
        print("GAME OVER")
        break

    print("=== BANK HEIST ===")
    print("Money:", money)
    print("Suspicion:", suspicion)
    print("1. Search")
    print("2. Hack Vault")
    print("3. Escape")
    print("4. Quit")

    choice = input("Choose: ")

    
    if choice == "1":
        print("You search the bank...")

        event = random.choice(["money", "nothing", "caught"])

        if event == "money":
            print("You found $500!")
            money += 500

        elif event == "nothing":
            print("You found nothing.")

        else:
            print("Security saw you!")
            suspicion += 20

    # Hack vault
    elif choice == "2":
        print("\nTrying to hack vault...")

        if random.choice(["success", "fail"]) == "success":
            print("Vault opened! +$2000")
            money += 2000
        else:
            print("Hack failed!")
            suspicion += 30

    # Escape
    elif choice == "3":
        if money >= 2000:
            print(" You escaped successfully!")
            print("You stole:", money)
            break
        else:
            print("You need at least $2000 to escape!")

    # Quit
    elif choice == "4":
        print("You quit the heist.")
        break

    else:
        print("Invalid choice.")