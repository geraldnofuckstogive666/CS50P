#https://cs50.harvard.edu/python/psets/5/test_bank/

from bank import value

def main():
    test_value()


def test_value():
    assert value("Hello, Newman") == 0
    assert value("hello, mickey") == 0
    assert value("Hey, aRtuRo") == 20
    assert value("nihao! neiga") == 100


if __name__ == "__main__":
    main()