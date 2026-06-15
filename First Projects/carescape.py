import random

health = 50

while True:

    if health <= 0:
        print(" You got eaten by zombies!")
        print("GAME OVER")
        break

    print("=== ZOMBIE ESCAPE ===")
    print("Health:", health)
    print("1. Search for supplies")
    print("2. Fight zombie")
    print("3. Heal")
    print("4. Escape")
    print("5. Quit")

    choice = input("Choose: ")

    if choice == "1":
        print("You search the area...")

        if random.choice(["good", "bad"]) == "good":
            print("You found food! +10 health")
            health += 10
        else:
            print("Zombie ambush! -10 health")
            health -= 10

    
    elif choice == "2":
        print("You fight a zombie...")

        if random.choice(["win", "lose"]) == "win":
            print("You killed it! ")
        else:
            print("You got bitten! -15 health")
            health -= 15

    
    elif choice == "3":
        print("You rest...")
        health += 10
        print("You healed +10 health")

    
    elif choice == "4":
        if health >= 60:
            print(" You escaped the city! YOU WIN!")
            break
        else:
            print("Not strong enough to escape!")

    
    elif choice == "5":
        print("You gave up.")
        break

    else:
        print("Invalid choice.")