def greet_friends(friends):
    for friend in friends:
        print("Hello " + friend + "!")

friends = []

amount = int(input("How many friends do you want to add? "))

for i in range(amount):
    name = input("Enter a friends name: ")
    friends.append(name)

greet_friends(friends)