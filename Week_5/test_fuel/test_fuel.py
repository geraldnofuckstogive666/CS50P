#https://cs50.harvard.edu/python/psets/5/test_fuel/


from fuel import gauge, convert



def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("2/3") == 67
    assert convert("3/3") == 100


def test_convert_negative():
    try:
        convert("-1/4")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError but none was raised"

def test_convert_zero_denominator():
    try:
        convert("4/0")
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError but none was raised"




def test_gauge_F():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_E():
    assert gauge(1) == "E"


def test_gauge_normal():
    assert gauge(2) =="2%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(98) == "98%"