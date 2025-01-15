#1
def toBinary(num):
    if num > 0:
        return bin(num)
    else:
        print("Please enter a postive integer")
        return num

#2
def findFactors(num):
        factors = [i for i in range(1, num+1) if num%i == 0]
        return factors
#test
testNum = int(input("Enter an integer number: "))
if testNum > 0:
     print(f"The factors of {testNum} are: {findFactors(testNum)}")
else:
     print("Number must be positive integer")

#3
def checkPrime(num):
     if num <= 1:
          return False
     else:
          factors = [i for i in range(1, num+1) if num%i == 0]
          if len(factors) == 2:
               return True
          else:
               return False
#test
testNum = int(input("Enter an integer number: "))
if checkPrime(testNum):
     print(f"{testNum} is a prime number.")
else:
     print(f"{testNum} is not a prime number.")

#4
def obfuscate(message):
     encrypted = message.replace(" ","")[::-1]
     return encrypted
#test
testMessage = input("Enter a message for encryption: ")
print(f"The encrypted message is: {obfuscate(testMessage)}")

#5
import random
import string
def encrypt(message):
     interval = random.randint(2,20)
     encrypted = ""
     for i in range(len(message)):
          encrypted = encrypted + message[i]
          for i in range(interval):
               encrypted = encrypted + random.choice(string.ascii_letters)
     return encrypted
#test
testMessage = input("Enter a message for encryption: ")
print(f"The encrypted message is: {encrypt(testMessage)}")

#6