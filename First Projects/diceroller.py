import random
import time

def show_result(name, number):
    print(name + " rolled a " + str(number) + "!")

players = int(input("How many players are there? "))

for i in range(players):
    name = input("Enter player name: ")
    print("Rolling the dice for " + name + "...")
    time.sleep(2)
    roll = random.randint(1, 6)
    show_result(name, roll)