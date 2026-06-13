import random

while True:
    print("=== SPACE ADVENTURE ===")
    print("1. Explore Planet")
    print("2. Repair Ship")
    print("3. Sleep")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You fly down to a mysterious planet...")
        event = random.choice([
            "You found glowing crystals! ",
            "You encountered friendly aliens ",
            "Nothing happened... it's quiet."
        ])
        print(event)

    elif choice == "2":
        print("You repair your ship ")
        print("Ship integrity improved!")

    elif choice == "3":
        print("You go to sleep ")
        print("Energy restored.")

    elif choice == "4":
        print("Goodbye, Commander! ")
        break

    else:
        print("Invalid choice. Try again.")