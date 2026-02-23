#https://cs50.harvard.edu/python/psets/2/camel/


def main():
    user_input = input("camelCase: ").strip()
    converted = snake_case(user_input)
    print(converted)



def snake_case(camel: str) -> str:
    result = []

    for i, letter in enumerate(camel):
        if letter.isupper():
            if i != 0:
                result.append("_")
            result.append(letter.lower())
        else:
            result.append(letter)


    return ''.join(result)


if __name__ == "__main__":
    main()