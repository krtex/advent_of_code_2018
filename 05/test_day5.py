from day5 import *

def test_givenEmptyString_returnEmpty():
    assert "" == trigger_polymer("")

def test_givenDifferentlyPolarizedPair_destroyThemAndReturnEmpty():
    assert "" == trigger_polymer("aA")

def test_differentLetters_returnNotDetroyed():
    assert "ab" == trigger_polymer("ab")

def test_destroyablePairAtTheEnd_returnFirstLetter():
    assert "b" == trigger_polymer("bAa")

def test_destroyablePairAtTheBegining_returnLastLetter():
    assert "b" == trigger_polymer("aAb")

def test_twoDestroyableNestedPairs_returnEmpty():
    assert "" == trigger_polymer("abBA")

def test_destroyablePairAtTheEnd_returnFirstTwoLetters():
    assert "ab" == trigger_polymer("abaA")

def test_twoPairsSameCase_returnOriginal():
    assert "aabAAB" == trigger_polymer("aabAAB")

def test_dataFormPage_resultFromPage_lol():
    assert "dabCBAcaDA" == trigger_polymer("dabAcCaCBAcCcaDA")
    assert 10 == len(trigger_polymer("dabAcCaCBAcCcaDA"))

def test_removing_letter_A_case_insensitively():
    assert "dbcCCBcCcD" == remove_unit("a", "dabAcCaCBAcCcaDA")
