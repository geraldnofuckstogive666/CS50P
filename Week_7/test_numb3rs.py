from numb3rs import validate


def test_validate():
    test_valid()
    test_invalid()


def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True
    assert validate("1.1.1.1") == True
    assert validate("255.0.1.127") == True


def test_invalid():
    assert validate("256.256.256.256") == False
    assert validate("0.0.0") == False
    assert validate("0.0.1") == False
    assert validate("1.1.1.1.1.1") == False
    assert validate("255.255.255.255.255.255") == False
    assert validate("cat") == False
    assert validate("") == False