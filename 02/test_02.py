from day_02 import countRepeating

def test_epmtyInputString_returnZeroes():
    assert (0,0) == countRepeating("")

def test_inputWithNoRepetitions_returnZeroes():
    assert (0,0) == countRepeating("abcdef")

def test_oneDouble_returnOneAndZero():
    assert (1, 0) == countRepeating("abbcde")

def  test_doubleAndTriple_returnTwoOnes():
    assert (1,1) == countRepeating("bababc")

def test_oneTriple_returnZeroAndOne():
    assert (0,1) == countRepeating("abcccd")

def test_twoDoubles_returnOneAndZero():
    assert(1,0) == countRepeating("aabcdd")

def test_twoTriples_returnZeroAndOne():
    assert (0,1) == countRepeating("ababab")

