#https://cs50.harvard.edu/python/psets/4/game/
import random


def main():
    while True:
        try: 
            n = int(input("Level: "))
        except ValueError:
            continue
        if n < 1:
            continue
        
        break

    lucky_number = random.randint(1, n)
    guessing_game(lucky_number)



def guessing_game(n):
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        if guess < 1:
            continue

        if guess == n:
            print("Just right!")
            return

        elif guess < n:
            print("Too small!")    

        else:
            print("Too large!")

        

if __name__ == "__main__":
    main()