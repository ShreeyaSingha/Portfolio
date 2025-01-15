import sys

args = sys.argv[1:]
argsLen = []
for i in args:
    argsLen.append(len(i))
shortestArg = args[argsLen.index(min(argsLen))]
print("No arguments provided") if not args else print(f"Shortest argument is {shortestArg}")