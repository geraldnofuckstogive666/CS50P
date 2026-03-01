#https://cs50.harvard.edu/python/psets/3/taqueria/


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0
    while True:
        try:
            user = input("Item: ").strip().title()
            total += menu.get(user, 0)

        except EOFError:
            break

        print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()