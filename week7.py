#1
def uniqueLetters(string):
    uLettersList = []
    for i in string:
        if not (i in uLettersList):
            uLettersList.append(i)
    return uLettersList
#test
testString = input("Enter a string: ")
print(f"Unique Letters: {uniqueLetters(testString)}")

#2
def inAtleastOne(string1, string2):
    return set(string1) | set(string2)
def inBoth(string1,string2):
    return set(string1) & set(string2)
def notInBoth(string1, string2):
    return set(string1) ^ set(string2)
#test
testString1 = input("Enter a string: ")
testString2 = input("Enter another string: ")
print(f"Letters in atleast one: {inAtleastOne(testString1,testString2)}")
print(f"Letters in both: {inBoth(testString1,testString2)}")
print(f"Letters in one but not both: {notInBoth(testString1,testString2)}")
