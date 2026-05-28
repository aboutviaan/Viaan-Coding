weight=float(input("Enter your weight in kg: "))
height = float(input("Enter your height in centimeters: ")) / 100
bmi= weight / (height * height)

if bmi < 18.5:
    print("You are underweight!")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are healthy! Nice!")
elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight!")
elif bmi > 30:
    print("You are obese!")