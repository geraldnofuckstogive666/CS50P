#https://cs50.harvard.edu/python/psets/2/camel/


def main():
    user_input = input("camelCase: ").strip()
    converted = snake_case(user_input)
    print(converted)




def snake_case(camel: str) -> str:
    snake_case_word  = ''
    for letter in camel:
        if not letter.isupper():
            snake_case_word += letter
        else:
            snake_case_word += "_" + letter.lower() 

    return snake_case_word       


if __name__ == "__main__":
    main()