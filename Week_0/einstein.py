import sys
try:
    m = int(input("m: "))

except:
    sys.exit("Not a Number.")

E = m * 300000000 ** 2

print(f"E: {E}")