#https://cs50.harvard.edu/python/psets/7/um/

import re

def main():
    print(count(input("Text: ")))


def count(s):
    num = 0
    if here := re.findall(r"\bum\b",s, re.IGNORECASE):
        for _ in here:
            num += 1

    return num


if __name__ == "__main__":
    main()