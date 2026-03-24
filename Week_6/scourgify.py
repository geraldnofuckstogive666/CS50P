#https://cs50.harvard.edu/python/psets/6/scourgify/
import sys
import csv

x = len(sys.argv)

if x == 3:
    filename = sys.argv[1]
    new_file = sys.argv[2]
    if ".csv" not in filename:
        sys.exit("Not a CSV File")
    elif ".csv" not in new_file:
        sys.exit("Output should be a CSV File")

    else:
        try:
            with open(filename, "r", newline='') as csvfile, open(new_file, "w", newline='') as output_file:
                contentreader = csv.reader(csvfile)
                outputwriter = csv.writer(output_file)
                next(contentreader)
                outputwriter.writerow(["first","last","house"])

                for row in contentreader:
                    full_name = row[0].split(",")
                    first_name = full_name[1].strip()
                    last_name = full_name[0].strip()
                    house = row[1].strip()
                    outputwriter.writerow([first_name, last_name, house])


        except FileNotFoundError:
            sys.exit(f"Could not read {filename}")

elif x < 3:
    sys.exit("Too few command-line arguments")

else:
    sys.exit("Too many command-line arguments")