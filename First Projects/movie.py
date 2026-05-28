def confirm_ticket(name, movie):
    print("Enjoy the show " + name + ", your ticket for " + movie + " is booked!")

people = int(input("How many people are booking tickets? "))

for i in range(people):
    name = input("Enter your name: ")
    movie = input("Enter the movie you want to see: ")
    confirm_ticket(name, movie)