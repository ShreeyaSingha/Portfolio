#1
name = input("Hello, what's your name? ")
print(f"Hello, {name}. Good to meet you!")

#2
temperature = float(input("Enter the temperature in celsius: "))
print("Temperature in fahrenheit: ", (temperature*9/5)+32)

#3
studentNum = int(input("Enter the number of students: "))
groupSize = int(input("What is the size of one group? "))
print(f"There are {studentNum // groupSize} groups")
if studentNum % groupSize == 1:
    print("There is 1 leftover student.")
elif studentNum % groupSize != 0:
    print(f"There are {studentNum % groupSize} students left.")

#4
sweetsNum = int(input("How many sweets do you have? "))
pupilNum = int(input("Enter the number of pupils: "))
print(f"Each student gets {sweetsNum // pupilNum} sweets")
print(f"Leftover sweets = {sweetsNum % pupilNum}")
