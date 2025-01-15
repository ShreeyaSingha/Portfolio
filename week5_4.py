import sys
import requests

httpResponse = requests.get(sys.argv[1])
try:
    if httpResponse.status_code // 100 == 2:
        print(f"There is a working website at {sys.argv[1]}")
    else:
        print(f"There is no working website at {sys.argv[1]}")
except IOError:
    print("Please enter a url to be checked")

#note to self: look at RequestException and what it does
#i dont compleetely understand this one TT