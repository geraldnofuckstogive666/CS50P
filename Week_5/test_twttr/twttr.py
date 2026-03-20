def main():
    word = input("Input: ")
    output = shorten(word)
    print(f"Output: {output}")

def shorten(word):
    vowels = ('a', 'i', 'e', 'o', 'u')
    return "".join(letter for letter in word if letter.lower() not in vowels)


if __name__ == "__main__":
    main()