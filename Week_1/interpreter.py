#https://cs50.harvard.edu/python/psets/1/interpreter/
def main():
    expression = input("Expression: ").strip()
    x, operator, z = expression.split()

    x = int(x)
    z = int(z)

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z
    else:
        raise ValueError("Invalid operator")

    print(f"{result:.1f}")


if __name__ == "__main__":
    main()