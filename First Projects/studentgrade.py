import time

students = []
grades = []

amount = int(input("How many students are there? "))

for i in range(amount):
    name = input("Enter student name: ")
    grade = int(input("Enter their grade: "))
    students.append(name)
    grades.append(grade)

def announce_result(name, grade):
    if grade > 50:
        print("Congratulations " + name + ", you passed!")
    else:
        print("Sorry " + name + ", you failed!")

for i in range(amount):
    announce_result(students[i], grades[i])
    time.sleep(1)