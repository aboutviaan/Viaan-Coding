units=float(input("How many units of electricity have you used this month: "))
if units < 100:
    bill = units * 0.10
elif units >= 100 and units <= 300:
    bill = units * 0.15
else:
    bill = units * 0.20

print("Your total bill is " + str(bill))