#https://cs50.harvard.edu/python/psets/5/test_plates/


from plates import is_valid


def test_accepted():
    assert is_valid("AA22") == True
    assert is_valid("ABC123") == True


def test_only_alphabet():
    assert is_valid("ABCDEF") == True
    assert is_valid("CS") == True


def test_without_alphabet():
    assert is_valid("123456") == False
    assert is_valid("0") == False


def test_num_char_combination():
    assert is_valid("AA012") == False
    assert is_valid("AA12") == True
    assert is_valid("AB123C") == False
    assert is_valid("123ABC") == False

def test_special_char():
    assert is_valid(" ") == False
    assert is_valid("A B") == False
    assert is_valid("!@#!%@&*") == False
    assert is_valid("ABC!.,") == False
    assert is_valid("#CS50") == False


def test_length():
    assert is_valid("AA") == True
    assert is_valid("AAA123") == True
    assert is_valid("")  == False
    assert is_valid("ABCD12345") == False