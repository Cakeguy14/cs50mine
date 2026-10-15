import pytest
from jar import Jar


def test_init_default():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_init_custom_capacity():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    jar = Jar(100)
    assert jar.capacity == 100
    assert jar.size == 0


def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(-100)
    with pytest.raises(ValueError):
        Jar("12")
    with pytest.raises(ValueError):
        Jar(3.5)


def test_str_empty():
    jar = Jar()
    assert str(jar) == ""


def test_str_with_cookies():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    assert jar.capacity == 12

    jar.deposit(7)
    assert jar.size == 12


def test_deposit_exceeds_capacity():
    jar = Jar(3)
    with pytest.raises(ValueError):
        jar.deposit(4)
    with pytest.raises(ValueError):
        jar.deposit(100)


def test_deposit_zero():
    jar = Jar()
    jar.deposit(0)
    assert jar.size == 0


def test_deposit_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0


def test_withdraw_exceeds_size():
    jar = Jar()
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)
    with pytest.raises(ValueError):
        jar.withdraw(100)


def test_withdraw_zero():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(0)
    assert jar.size == 3


def test_withdraw_negative():
    jar = Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(-1)


def test_withdraw_empty_jar():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_capacity_read_only():
    jar = Jar()
    with pytest.raises(AttributeError):
        jar.capacity = 20


def test_size_read_only():
    jar = Jar()
    with pytest.raises(AttributeError):
        jar.size = 5
