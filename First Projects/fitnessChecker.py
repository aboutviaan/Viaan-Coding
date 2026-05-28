goal = int(input("Enter your daily step goal: "))

total = 0

for i in range(1, 8):
    steps = int(input("Day " + str(i) + " - Enter your steps: "))
    total = total + steps
    
    if steps >= goal:
        print("Great job you hit your goal today!")
    else:
        difference = goal - steps
        print("You are " + str(difference) + " steps short of your goal!")

print("Your weekly total is " + str(total) + " steps!")