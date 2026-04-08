import pytest
from datetime import datetime
from unittest.mock import patch
from seasons import convert_to_words, date_validator, minute_calculator


@pytest.mark.parametrize("int_input, output",[
        (525600, "Five hundred twenty-five thousand, six hundred minutes"),
        (500, "Five hundred minutes"),
        (100000,"One hundred thousand minutes"),
        (2500333,"Two million, five hundred thousand, three hundred thirty-three minutes")

])

def test_convert_to_words(int_input,output):
    assert convert_to_words(int_input) == output



#for mockkkk
def converter(s):
    date = datetime.strptime(s,"%Y-%m-%d").date()
    return date



@pytest.mark.parametrize("date_input, output",[
    (converter("2025-10-08"), 1440),
    (converter("2000-01-01"), 13554720),
    (converter("1999-10-09"), 13675680),
    (converter("2025-01-01"), 404640),
    (converter("2004-11-10"), 10998720)
])

def test_minute_calculator(date_input,output):
    fake_today = converter("2025-10-09")

    with patch("seasons.date")as mock_date:
        mock_date.today.return_value = fake_today
        mock_date.side_effect = lambda *a, **kw: datetime.date(*a, **kw)
        result = minute_calculator(date_input)

    assert result == output








@pytest.mark.parametrize("invalids",[
 ("June 12, 1898"),
 ("January 4, 2003"),
 ("1999-1-1"),
 ("2024-13-32"),
 ("2006")
])
def test_invalid_date_validator(invalids):
    with pytest.raises(SystemExit) as excinfo:
        date_validator(invalids)

    assert excinfo.value.code == "Invalid date"



@pytest.mark.parametrize("valids , output",[
    ("2025-10-09", converter("2025-10-9")),
    ("2000-01-01",converter("2000-01-01")),
    ("2006-03-12" ,converter("2006-03-12")),
    ("2004-11-10", converter("2004-11-10")),
    ("2000-11-09", converter("2000-11-09"))
])
def test_valid_date_validator(valids,output):
    assert date_validator(valids) == output