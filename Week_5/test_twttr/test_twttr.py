#https://cs50.harvard.edu/python/psets/5/test_twttr/

from twttr import shorten
import sys


def main():
    test_shorten()



def test_shorten():
    try:
        assert shorten("HEY") == "HY"   #with capital vowel removed
    except AssertionError:
        sys.exit("Failed!")

    try:
        assert shorten("What's your name?") == "Wht's yr nm?"  #without capitalized vowel removed
    except AssertionError:
        sys.exit("Failed!")


    try:
        assert shorten("CS50") == "CS50"    #without vowel replacement
    except AssertionError:
        sys.exit("Failed!")

    try:
        assert shorten("PYTHON") == "PYTHN"
    except AssertionError:
        sys.exit("Failed!")

    try:
        assert shorten("wkwkwk") == "wkwkwk"
    except AssertionError:
        sys.exit("Failed!")


if __name__ == "__main__":
    main()