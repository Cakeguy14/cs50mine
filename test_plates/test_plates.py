from plates import is_valid


def test_word():
    assert is_valid("CS50") == False


def test_num():
    assert is_valid("CAT00")

def test_firstzero()
