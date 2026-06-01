import random
import time

players = []

while True:
    name = input("Add a player or type done to stop: ")
    if name == "done":
        break
    else:
        players.append(name)

def announce_winner(name):
    print("And the winner is... " + name + "!")

print("Picking a winner...")
time.sleep(3)
winner = random.choice(players)
announce_winner(winner)