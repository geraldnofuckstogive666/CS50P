#https://cs50.harvard.edu/python/psets/2/twttr/

VOWELS = {"a", "i", "e", "o", "u"}


def main():
    user_input = input("Input: ").strip()
    output = shorten(user_input)
    print(f"Output: {output}")


def shorten(word: str) -> str:
    return "".join([letter for letter in word if letter.lower() not in VOWELS])

if __name__ == "__main__":
    main()
