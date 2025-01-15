import sys

temperatures = []
try:
    while True:
        temperature = sys.argv[1:]
        for i in temperature:
            temp_value = float(i[:-2])
            temperatures.append(temp_value)
except IOError:
    print("Please enter the temperatures after the program name")
print(f"""Maximum of inputs = {max(temperatures)}
Minimum of inputs = {min(temperatures)}
Mean of inputs = {sum(temperatures)/len(temperatures)} """)
