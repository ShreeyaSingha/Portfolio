#1
name = input("Hello, what's your name? ")
if name == "":
    print("Hello, stranger!")
else:
    print(f"Hello, {name}. Good to meet you!")

#2
password1 = input("Please enter a password: ")
password2 = input("Please enter the password again: ")
if password1 == password2:
    print("Password Set!")
else:
    print("Entered passwords were not the same. Please try again.")

#3
password1 = input("Please enter a password: ")
password2 = input("Please enter the password again: ")
if password1 == password2:
    if 8 <= len(password1) <= 12:
        print("Password Set!")
    else:
        print("Password must be between 8 and 12 characters (inclusive)")
else:
    print("Entered passwords were not the same. Please try again.")

#4
BAD_PASSWORDS = ['password','letmein','sesame','hello','justinbieber']
password1 = input("Please enter a password: ")
password2 = input("Please enter the password again: ")
if password1 == password2:
    if password1 in BAD_PASSWORDS:
        print("Password cannot be any of the following: ", BAD_PASSWORDS)
    if 8 <= len(password1) <= 12:
        print("Password Set!")
    else:
        print("Password must be between 8 and 12 characters (inclusive)")
else:
    print("Entered passwords were not the same. Please try again.")

#5
BAD_PASSWORDS = ['password','letmein','sesame','hello','justinbieber']
passwordSet = False
while passwordSet == False:
    password1 = input("Please enter a password: ")
    password2 = input("Please enter the password again: ")
    if password1 == password2:
        if password1 in BAD_PASSWORDS:
            print("Password cannot be any of the following: ", BAD_PASSWORDS)
        if 8 <= len(password1) <= 12:
            print("Password Set!")
            passwordSet = True
        else:
            print("Password must be between 8 and 12 characters (inclusive)")
    else:
        print("Entered passwords were not the same. Please try again.")

#6
for i in range(13):
    print(f"7 x {i} = {7*i}")

#7
num = int(input("Enter a number (0-12): "))
for i in range(13):
    print(f"{num} x {i} = {num*i}")

#8
num = int(input("Enter a number (0-12): "))
if num > 0:
    for i in range(13):
        print(f"{num} x {i} = {num*i}")
else:
    for i in range(12,-1,-1):
        print(f"{num} x {i} = {num*i}")
