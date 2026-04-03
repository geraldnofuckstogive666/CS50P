#https://cs50.harvard.edu/python/psets/7/response/

from validator_collection import validators, errors

user = input("What's your email? ")


try:
    email_address = validators.email(user)
    if email_address:
        print("Valid")


except (errors.EmptyValueError, errors.InvalidEmailError) as e:
    print("Invalid")