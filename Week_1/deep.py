#https://cs50.harvard.edu/python/psets/1/deep/


def ask(prompt: str) -> str:
    user_input = input(prompt).strip().lower()
    if user_input in ("42", "forty-two", "forty two"):
        return "Yes"
    else:
        return "No"


def main():
    print(ask("What is the Answer to the Great Question of Life, the Universe, and Everything? "))


if __name__ == "__main__":
    main()