import random
import time

jobs = ["Pilot", "Engineer", "Scientist", "Navigator", "Medic"]
crew = []

while True:
    name = input("Add a crew member or type done to stop: ")
    if name == "done":
        break
    crew.append(name)

def announce_member(name, job):
    print(name + " will serve as the " + job + " on this mission!")

print("Assembling your space crew...")
time.sleep(2)

for member in crew:
    time.sleep(1)
    job = random.choice(jobs)
    announce_member(member, job)

print("Crew assembled! Prepare for launch! 🚀")