import random
import time

prizes = ["Car", "Free Vacation", "iPhone", "piece of nothing", "thousand Dollars"]

def show_prize(name, prize):
    print("Congratulations " + name + ", you won a " + prize + "!")

players = int(input("How many players are spinning? "))

for i in range(players):
    name = input("Enter your name: ")
    print("Spinning the wheel for " + name + "...")
    time.sleep(2)
    prize = random.choice(prizes)
    show_prize(name, prize)