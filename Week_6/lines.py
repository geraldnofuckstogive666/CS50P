#https://cs50.harvard.edu/python/psets/6/lines/

import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")


try: 
    with open(filename, "r") as f:
        count = 0
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") :
                count += 1

        print(count)

except FileNotFoundError:
    sys.exit("File does not exist")



