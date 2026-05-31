import random
import time

name=input("What is your name: ")
print("Finding your lucky number "+ name )
time.sleep(2)

def reveal_number(name, number):
    print("Your lucky number is " + str(number) + ", " + name + "!")

lucky_number = random.randint(1, 100)
reveal_number(name, lucky_number)