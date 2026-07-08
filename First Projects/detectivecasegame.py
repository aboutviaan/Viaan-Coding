import random

case_name = "The Missing Tech Device"
actions_left = 6
evidence = []
suspects = ["Alex", "Jordan", "Sam", "Taylor"]
culprit = "Jordan"

clue_pool = ["Footprints near window", "Broken lock", "Fingerprint on desk.", "CCTV footage missing", " Suspicious note found", "Nothing useful found"]
  

while True:
    if actions_left <= 0:
        print("You ran out of actions. The case is closed.")
        break

    print("Case:", case_name)
    print("Actions left:", actions_left)
    print("1. Search crime scene")
    print("2. Question suspect")
    print("3. Check evidence")
    print("4. Make accusation")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You search the crime scene.")
        clue = random.choice(clue_pool)
        print("Result:", clue)

        if clue != "Nothing useful found":
            evidence.append(clue)

        actions_left -= 1

    elif choice == "2":
        print("You question a suspect.")
        suspect = random.choice(suspects)
        print("Suspect:", suspect)

        response = random.choice([
            "I was at home",
            "I saw something strange",
            "I know nothing",
            "I was not there"
        ])

        print("Response:", response)
        actions_left -= 1

    elif choice == "3":
        print("Evidence list:")
        for item in evidence:
            print(item)

        actions_left -= 1

    elif choice == "4":
        guess = input("Who is the culprit? ")

        if guess == culprit:
            print("Correct! You have solved the case!")
        else:
            print("Wrong suspect. Case failed.")

        break

    elif choice == "5":
        print("You quit the case.")
        break

    else:
        print("Invalid choice.")