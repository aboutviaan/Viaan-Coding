grade = int(input("Grade: "))
ticket = input("Have a ticket? (yes/no): ")
suspended = input("Suspended? (yes/no): ")

allowed = grade >= 7 and ticket == "yes" and suspended == "no"

if allowed:
    print("You may enter!")
else:
    print("Access denied.")