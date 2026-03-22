#https://cs50.harvard.edu/python/psets/3/fuel/


def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
        if x > y:
            raise ValueError
        return round(x / y * 100)
    except ZeroDivisionError:
        raise
    except ValueError:
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()