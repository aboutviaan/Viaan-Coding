
import random

print("Rock Paper Scissors!")
print("---------------------")

user = input("Enter rock, paper, or scissors: ")

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "scissors":
    print("You win!")
elif user == "paper" and computer == "rock":
    print("You win!")
elif user == "scissors" and computer == "paper":
    print("You win!")
else:
    print("Computer wins!")