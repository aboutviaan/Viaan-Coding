balance = 1000
interest_rate = 0.03
years = 3

# Interest compounds once a month.
for month in range(years * 12):
    interest = balance * interest_rate
    balance = round(balance + interest, 2)

    print("Current balance: $" + str(balance))