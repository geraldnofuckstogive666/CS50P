#https://cs50.harvard.edu/python/psets/1/bank/


def greet(greetings: str) -> str:
    if greetings[0] == 'h':  
        if 'hello' in greetings:
            return '$0'
        else:
            return '$20'
    else:
        return '$100'
    

def main():
    user_input = input("Greetings: ").lower().strip()
    print(greet(user_input))



if __name__ == "__main__":
    main()