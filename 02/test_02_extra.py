from day_02_extra import compareTwoLines

def test_twoDifferentStrings_returnFalse():
    assert False == compareTwoLines("asd", "qwe")

def test_twoIdenticalStrings_returnSameString():
    assert "asd" == compareTwoLines("asd", "asd")

def test_oneLetterDifference_returnCommon():
    assert "asd" == compareTwoLines("asdf", "asde")

def test_oneLetterDifferenceDifferentOrder_returnCommon():
    assert False == compareTwoLines("asdf", "edsa")

def test_twoLetterDifference_returnFalse():
    assert False == compareTwoLines("asdf", "asqw")

