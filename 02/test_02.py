from day_02 import countRepeating

def test_epmtyInputString_returnsZeroes():
    assert (0,0) == countRepeating("")

def test_inputWithNoRepetitions_returnZeroes():
    assert (0,0) == countRepeating("abcdef")

def test_oneDouble_returnOneAndZero():
    assert (1, 0) == countRepeating("abbcde")

