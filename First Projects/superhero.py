import random
import time

superhero_names = ["Iron Coder", "Python Man", "The Debug", "Captain Loop", "Shadow Function", "The Mighty Import","Nova Zenith","Quantum Vex","Zephyr Wing"]

roster = []

while True:
    name = input("Add a person or type done to stop: ")
    if name == "done":
        break
    roster.append(name)

def assign_superhero(real_name, superhero_name):
    print(real_name + " your superhero name is... " + superhero_name + "!")

print("Assigning superhero names...")

for name in roster:
    time.sleep(2)
    superhero = random.choice(superhero_names)
    assign_superhero(name, superhero)