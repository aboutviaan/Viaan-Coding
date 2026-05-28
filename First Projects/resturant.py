def confirm_order(customer_name, food):
    print("Thank you " + customer_name + ", your order of " + food + " is confirmed!")

customers = int(input("How many customers are there? "))

for i in range(customers):
    customer_name = input("Enter one of the customer's name: ")
    food = input("Enter food order: ")
    confirm_order(customer_name, food)  