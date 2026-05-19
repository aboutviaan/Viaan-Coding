print("Simple Calculator")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = float(num1)
num2 = float(num2)

print("What do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter 1, 2, 3, or 4: ")

if choice == "1":
    print("Answer:", num1- num2)
elif choice == "2":
    print("Answer:", num1 - num2)
elif choice == "3":
    print("Answer:", num1 * num2)
elif choice == "4":
    print("Answer:", num1 / num2)
else:
    print("Invalid choice!")