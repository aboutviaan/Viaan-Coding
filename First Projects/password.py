password=input("Enter a password: ")
if len(password) < 8:
    print("Warning! Your password is too short!")
else:
    print("Your password is strong!")