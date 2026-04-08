import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"
    assert jar.capacity == 12


    jar2 = Jar(24)
    jar2.deposit(12)
    assert jar2.size == 12
    assert str(jar2) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    assert jar2.capacity == 24



def test_withdraw():
    jar1 = Jar()
    jar1.size = 10
    jar1.withdraw(6)
    assert jar1.size == 4
    assert str(jar1) == "🍪🍪🍪🍪"

    jar2 = Jar()
    jar2.size = 12
    jar2.withdraw(6)
    assert jar2.size == 6
    assert str(jar2) == "🍪🍪🍪🍪🍪🍪"



def test_invalid_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(5)

    jar1 = Jar()
    jar1.deposit(10)
    with pytest.raises(ValueError):
        jar1.withdraw(11)



def test_error_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)


    jar1 = Jar()
    with pytest.raises(ValueError):
        jar1.deposit(100)