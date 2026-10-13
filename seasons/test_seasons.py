import pytest
from seasons import convert


def test_valid_dates():
    # These tests verify format parsing works
    # (exact minutes depend on today's date, so we check types)
    assert isinstance(convert("2000-01-01"), int)
    assert isinstance(convert("1999-12-31"), int)
    assert isinstance(convert("2020-02-29"), int)  # leap year


def test_minutes_are_positive():
    assert convert("2000-01-01") > 0
    assert convert("1999-12-31") > 0


def test_leap_year():
    # 2020 is a leap year → Feb 29 is valid
    assert isinstance(convert("2020-02-29"), int)


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("January 1, 2000")
    with pytest.raises(ValueError):
        convert("2000/01/01")
    with pytest.raises(ValueError):
        convert("01-01-2000")
    with pytest.raises(ValueError):
        convert("2000-1-1")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("hello")


def test_invalid_date():
    with pytest.raises(ValueError):
        convert("2000-13-01")   # month 13
    with pytest.raises(ValueError):
        convert("2000-01-32")   # day 32
    with pytest.raises(ValueError):
        convert("2000-02-30")   # Feb 30 doesn't exist
    with pytest.raises(ValueError):
        convert("2021-02-29")   # 2021 is not a leap year


def test_future_date():
    # A future date produces negative minutes — still valid as an int
    result = convert("3000-01-01")
    assert isinstance(result, int)
