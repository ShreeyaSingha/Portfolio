#1
def testNum(num):
    """ function to test if entered number is between 0 and 100 """
    if 0<=num<=100:
        return True
    else:
        return False
#main
if testNum(num=int(input("Enter a number: "))):
    print("The number is between 0 and 100")
else:
    print("The number is not between 0 and 100")

#2
def countLetters(word):
    """ function to count the number of lowercase and uppercase letters in a string """
    lower_count = 0
    upper_count = 0
    for i in word:
        if 'a' <= i <= 'z':
            lower_count += 1
        elif 'A' <= i <= 'Z':
            upper_count += 1
    return lower_count, upper_count
lowercase, uppercase = countLetters(input("Type something to count the number of lowercase and uppercase letters: "))
print(f"""There are {lowercase} lowercase letters.
There are {uppercase} uppercase letters.""")

#3
name = input("Hello, what's your name? ")
format_name = ""
format_name = (name[0:1]).upper() + (name[1:]).lower()
if format_name == "":
    print("Hello, stranger!")
else:
    print(f"Hello, {format_name}. Good to meet you!")

#4
def remove_char(line):
    if len(line)<=1:
        return line
    else:
        return line[:-2]
#main
string = "This is a line.n"
print (remove_char(string))

#5
def c_to_f(temperature):
    """ to convert temperature in celsius to fahrenheit """
    return (temperature*(9/5))+32
def f_to_c(temperature):
    """ to convert temperature in fahrenheit to celsius """
    return (temperature-32)*(5/9)
#main
temp1 = float(input("Enter the temperature in celsius: "))
temp2 = float(input("Enter the temperature in fahrenheit: "))
print(f"""{temp1}C = {c_to_f(temp1)}F
{temp2}F = {f_to_c(temp2)}C """)

#6
temperature = input("Enter the temperature in celsius (input must be a number followed by a letter C): ")
temp_value = float(temperature[:-2])
print(f"Temperature in fahrenheit:  {(temp_value*9/5)+32}F")

#7
temperatures = []
for i in range(6):
    temperature = input("Enter the temperature in celsius (input must be a number followed by a space and the letter C): ")
    temp_value = float(temperature[:-3])
    temperatures.append(temp_value)
print(f"""Maximum of inputs = {max(temperatures)}
Minimum of inputs = {min(temperatures)}
Mean of inputs = {sum(temperatures)/len(temperatures)} """)

#8
temperatures = []
while True:
    temperature = input("Enter the temperature in celsius (input must be a number followed by a letter C): ")
    if temperature == "":
        break
    temp_value = float(temperature[:-2])
    temperatures.append(temp_value)
print(f"""Maximum of inputs = {max(temperatures)}
Minimum of inputs = {min(temperatures)}
Mean of inputs = {sum(temperatures)/len(temperatures)} """)
