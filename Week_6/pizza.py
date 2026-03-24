#https://cs50.harvard.edu/python/psets/6/pizza/

import sys
import csv
from tabulate import tabulate  #need pip install tabulate


x = len(sys.argv)

if x == 2:
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV File")
    else:
        filename = sys.argv[1]
        try:
            with open(filename, "r" , newline='') as csvfile:
                contentreader = csv.reader(csvfile)

                print(tabulate(contentreader, headers="firstrow",tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")


elif x < 2:
    sys.exit("Too few command-line arguments")


else:
    sys.exit("Too many command-line arguments")
