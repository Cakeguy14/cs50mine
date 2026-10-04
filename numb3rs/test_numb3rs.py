from numb3rs import validate


def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True
    assert validate("192.168.1.1") == True
    assert validate("10.0.0.1") == True


def test_out_of_range():
    assert validate("512.512.512.512") == False
    assert validate("256.0.0.1") == False
    assert validate("1.2.3.1000") == False
    assert validate("-1.0.0.0") == False


def test_wrong_number_of_parts():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat") == False
    assert validate("") == False


def test_non_numeric():
    assert validate("1.2.3.a") == False
    assert validate("a.b.c.d") == False
    assert validate("1.2.3.4a") == False


def test_leading_zeros():
    assert validate("192.168.001.1") == False
    assert validate("01.02.03.04") == False
    assert validate("0.0.0.0") == True    # "0" alone is valid


def test_edge_cases():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("256.1.1.1") == False
