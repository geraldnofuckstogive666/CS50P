def main():
    word = input("Input: ")
    output = shorten(word)
    print(f"Output: {output}")

def shorten(word):
    vowels = ('a', 'i', 'e', 'o', 'u')
    return "".join("" if letter.lower() in vowels else letter for letter in word)


if __name__ == "__main__":
    main()


