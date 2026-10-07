import pytest
from working import convert

def test_basic_am_pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 2:30 PM") == "10:30 to 14:30"
    assert convert("1:00 PM to 3:00 PM") == "13:00 to 15:00"


def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 2 PM") == "10:00 to 14:00"
    assert convert("1 PM to 3 PM") == "13:00 to 15:00"


def test_midnight_noon():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_am_am():
    assert convert("9:00 AM to 10:00 AM") == "09:00 to 10:00"
    assert convert("11:59 AM to 12:00 PM") == "11:59 to 12:00"


def test_pm_pm():
    assert convert("1:00 PM to 11:00 PM") == "13:00 to 23:00"
    assert convert("12:00 PM to 11:59 PM") == "12:00 to 23:59"


def test_edge_times():
    assert convert("12:00 AM to 11:59 PM") == "00:00 to 23:59"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")
    with pytest.raises(ValueError):
        convert("hello")
    with pytest.raises(ValueError):
        convert("")


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:99 AM to 5:00 PM")


def test_missing_am_pm():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00")
    with pytest.raises(ValueError):
        convert("9:00 XM to 5:00 PM")
