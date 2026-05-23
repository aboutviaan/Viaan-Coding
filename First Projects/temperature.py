temperature = int(input("Enter a temperature: "))

for i in range(1, temperature + 1):
    if i > 35:
        print(str(i) + " degrees is too hot!!")
    else:
        print(str(i) + " is normal.")