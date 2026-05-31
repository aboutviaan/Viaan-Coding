import random
import time

answers = ["Yes definitely!", "No way!", "Maybe...", "Ask again later", "Absolutely not!"]

def show_answer(question, answer):
    print("You asked: " + question + " ... The Magic 8 Ball says: " + answer)

questions = int(input("How many questions do you want to ask? "))

for i in range(questions):
    question = input("Ask the Magic 8 Ball a question: ")
    print("The Magic 8 Ball is thinking...")
    time.sleep(2)
    answer = random.choice(answers)
    show_answer(question, answer)