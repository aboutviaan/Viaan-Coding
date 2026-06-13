import random

dragon_name = input("What is your dragon's name? ")

hunger = 50
strength = 10

print(dragon_name, "has hatched!")

while True:
    print("=== Dragon Trainer ===")
    print("1. Feed Dragon")
    print("2. Train Dragon")
    print("3. Go Flying")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        hunger -= 10
        print(dragon_name, "enjoyed the food.")
        print("Hunger is now:", hunger)

    elif choice == "2":
        strength += 5
        print(dragon_name, "trained hard.")
        print("Strength is now:", strength)

    elif choice == "3":
        location = input("Fly to mountains or forest? ")

        event = random.choice([
            "You found an ancient cave.",
            "You discovered a hidden lake.",
            "A wild windstorm passed by.",
            "You found nothing special."
        ])

        print(event)

        