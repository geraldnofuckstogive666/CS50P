#https://cs50.harvard.edu/python/psets/4/professor/

import random


def main():
    score = 0
    numbers = generate_integer(get_level())
    pass






def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if not (1 <= level <= 3):
            continue

        return level

def generate_integer(level):
    x = [random.randint(10 ** (level - 1), 10 ** level - 1) for _ in range(10)]
    y = [random.randint(10 ** (level - 1), 10 ** level - 1) for _ in range(10)]
    return list(zip(x, y))






if __name__ == "__main__":
    main()


