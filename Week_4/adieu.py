#https://cs50.harvard.edu/python/psets/4/adieu/
# need: pip install inflect
import inflect

p = inflect.engine()

def main():
    names = []

    while True:
        try:
            names.append(input("Name: ").strip())
        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
