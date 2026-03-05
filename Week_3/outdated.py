#https://cs50.harvard.edu/python/psets/3/outdated/


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



def main():
    while True:
        date = input("Date: ").strip().title()

        try:
            print(converter(date))
            return
        except ValueError:
            pass


def converter(date):
    if "/" in date:
        m, d, y = map(int, date.split("/"))

    else:
        m, d, y = date.split()
        m = months.index(m) + 1
        d = int(d.removesuffix(","))
        y = int(y)

    if not (1 <= m <= 12):
        raise ValueError

    if not (1 <= d <= 31):
        raise ValueError

    return f"{y:04}-{m:02}-{d:02}"


if __name__ == "__main__":
    main()




