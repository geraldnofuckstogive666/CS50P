import pytest
from working import convert


def test_valid_convert():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1 AM to 1:30 AM") == "01:00 to 01:30"
    assert convert("12:00 AM to 2 PM") == "00:00 to 14:00"
    assert convert("1:30 AM to 4:00 PM") == "01:30 to 16:00"
    assert convert("12 PM to 6 PM") == "12:00 to 18:00"
    assert convert("1:00 PM to 1 AM") == "13:00 to 01:00"
    assert convert("1:44 AM to 12:51 PM") == "01:44 to 12:51"



import pytest

@pytest.mark.parametrize("time_str", [
    "2:60 AM",
    "3AM",
    "4 PM",
    "9:00 AM - 17:00 PM",
    "9:00 AM  5:00 PM",
    "1 PM5 PM",
    "100:00 AM to 12:00 PM",
    "1:67 PM to 2:45 PM",
    "1:30 to 5:40",
    "09:00 AM - 17:00 PM",
    "9:00 AM 5:00 PM",
    "9:60 AM to 5:60 PM",
    "9 AM - 5 PM",
    "9 AM5 PM",
    "9 AM 5 PM",
    "9:72 to 6:30",
])


def test_invalid_convert(time_str):
    with pytest.raises(ValueError):
        convert(time_str)