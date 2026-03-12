#https://cs50.harvard.edu/python/psets/4/professor/

import random


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        errors = 0

        while errors < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                errors += 1
                continue

            if answer == x + y:
                score += 1
                break
            else:
                print("EEE")
                errors += 1

        if errors == 3:
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level not in (1, 2, 3):
        raise ValueError

    return random.randint(10**(level-1), 10**level - 1)


if __name__ == "__main__":
    main()