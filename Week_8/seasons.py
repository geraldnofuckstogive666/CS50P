#https://cs50.harvard.edu/python/psets/8/seasons/


import inflect
import sys
from datetime import date, datetime, timedelta
from validator_collection import validators, checkers, errors


def main():
    user_input = input("Date of Birth: ").strip()
    date = minute_calculator(date_validator(user_input))
    print(convert_to_words(date))


def convert_to_words(num):
    p = inflect.engine()

    existence = p.number_to_words(num)
    return f"{existence.capitalize().replace(" and", "")} minutes"


def date_validator(s):
    try:
        date = validators.date(s)
        return date
    except (errors.EmptyValueError, errors.CannotCoerceError) as e:
        sys.exit("Invalid date")


def minute_calculator(d):
    today = date.today()
    date_difference = today - d
    days = date_difference.days

    return days * 24 * 60




if __name__ == "__main__":
    main()