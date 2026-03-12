#https://cs50.harvard.edu/python/psets/4/professor/

import random


def main():
    score = 0
    numbers = generate_integer(get_level())
    for x, y in numbers:
        error = 0 
        while True:
            print(f'{x} + {y} = ',end='')
            try:
                answer = int(input())
            except ValueError:
                error += 1
            
            if answer == x + y:
                score += 1
                break
            else:
                print("EEE")
                error += 1
            
            if error == 3:
                print(f'{x} + {y} = {x + y}')
                break

    print(f"Score: {score}")


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