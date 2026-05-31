students = []

amount = int(input("How many students are in the class: "))

for i in range(amount):
    name = input("Enter a students name: ")
    students.append(name)

def announce_students(students):
    for student in students:
        print("Welcome to class, " + student + "!")
        
announce_students(students)