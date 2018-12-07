from day5 import *

def test_givenEmptyString_returnEmpty():
    assert "" == trigger_polymer("")

def test_givenDifferentlyPolarizedPair_destroyThemAndReturnEmpty():
    assert "" == trigger_polymer("aA")

def test_differentLetters_returnNotDetroyed():
    assert "ab" == trigger_polymer("ab")

def test_twoDestroyableNestedPairs_returnEmpty():
    assert "" == trigger_polymer("abBA")

def test_twoPairsSameCase_returnOriginal():
    assert "aabAAB" == trigger_polymer("aabAAB")

def test_dataFormPage_resultFromPage_lol():
    assert "dabCBAcaDA" == trigger_polymer("dabAcCaCBAcCcaDA")
