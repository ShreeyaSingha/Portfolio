import sys
import os

def getDriversDetails():
    details = open("f1_drivers.txt", 'r')
    driversDetails = {}
    for line in details:
        info = line.strip().split(',')      #splits the string wherever the parameter is and returns substrings
        driverCode = info[1]
        driverName = info[2]
        driverTeam = info[3]
        driversDetails[driverCode] = (driverName,driverTeam)
    details.close()
    return driversDetails


def processFile(filename):
    if not os.path.isfile(filename):
        print(f"{filename} does not exist.")
    f = open(filename, 'r')
    raceName = f.readline().strip()
    print(f"The race is located at {raceName}")
    data = f.readlines()       #list of lap data from the file
    timeline = {}       #empty dictionary
    for i in data:
        driverCode = i[:3].strip()
        lapTime = float(i[3:].strip())
        if driverCode not in timeline:
            timeline[driverCode] = []       #to make each value a list
        timeline[driverCode].append(lapTime)        #.append() works since each value is now a list
    f.close()
    return timeline

def displayFastest(timeline, details):
    fastestDriver = min(timeline, key= lambda dt: min(timeline[dt]))      #dt is drivers time(the list value of each key)       #lambda function used to find fastest time of each driver since i don't need that fuction anywhere else
    fastestTimeTotal = min(timeline[fastestDriver])      #smallest time of fastest driver is fastest time overall
    print(f"""Fastest Driver: {fastestDriver}({details[fastestDriver][0]}) from {details[fastestDriver][1]}
Fastest Time: {fastestTimeTotal:>8}""")
    print("")       #for clarity

def displayAverageOverall(timeline):
    #Display fastest, avg time for each driver and overall
    totalTime = 0
    totalLaps = 0
    for driver in timeline.keys():
        times = timeline[driver]
        totalTime += sum(times)
        totalLaps += len(times)
    overallAverageTime = totalTime / totalLaps
    print(f"Average Time Overall: {overallAverageTime: .3f}")       #output upto 3 decimal spaces
    print("")       #for clarity

def displayAverageTimeEach(timeline,details):
    print("Average times of each driver:")
    print("")       #for clarity
    for driver in timeline.keys():
        print("")       #for clarity
        times = timeline[driver]
        avgTime = sum(times)/len(times)
        print(f"""{driver} ({details[driver][0]}) from {details[driver][0]}
Average Time: {avgTime:>8.3f}""")     #has 3 decimal places
    print("")       #for clarity

def displayFastestTimesDescending(timeline,details):
    print("Fastest times in descending order:")
    print("")       #for clarity
    fastestTimes = [(driver, min(times)) for driver, times in timeline.items()]     #key and values from each item. smallest value from each list of times
    fastestTimes = sorted(fastestTimes,key=lambda dt: dt[1], reverse=True)       #sort() method to sort into ascending BUT use sorted() function so that it is still a list instead of nonetype     #key lambda expression ensures sorting is done acc to time and not driver codes      #set reverse flag to get descending order
    for d,t in fastestTimes:
        print(f"{d:>4}     {details[d][0]:<20} from       {details[d][1]:<20}         Fastest Time: {t:>8.3f}")      #alignments and decimal points
    print("")       #for clarity


def menu():
    print("""1. Fastest Driver
2. Overall Average Time of Drivers
3. Average Time of Each Driver
4. Fastest Time of Each Driver (Descending)""")
    print("Enter X once you are ready to exit")

def choose(timeline,details):
    try:
        choice = input("Please enter the corresponding index for information you would like to access: ")
        print("")       #for clarity
        if choice == "1":
            displayFastest(timeline, details)
            choose(timeline,details)
        elif choice == "2":
            displayAverageOverall(timeline)
            choose(timeline,details)
        elif choice == "3":
            displayAverageTimeEach(timeline, details)
            choose(timeline,details)
        elif choice == "4":
            displayFastestTimesDescending(timeline, details)
            choose(timeline,details)
        elif choice == 'x' or choice == 'X':
            sys.exit()
        else:
            print("Enter a valid index from the menu")
            choose(timeline,details)
    except IOError:
        print("Enter a valid index from the menu")
        choose(timeline,details)

def main():
    if len(sys.argv) != 2:
        print("Usage: python race_analysis.py <file_name>")
        return
    timeline = processFile(sys.argv[1])
    menu()
    driverDetails = getDriversDetails()
    choose(timeline, driverDetails)

if __name__ == "__main__":
    main()
