import day4
import numpy as np

reference = open("test_input").readlines()

def test_sort():
    input = open("test_random").readlines()
    input.sort()
    assert input == reference

def test_parse_guards():
    result = day4.find_guard("[1518-11-01 00:00] Guard #10 begins shift")
    assert 10 == result

def test_no_guard_found_return_false():
    result = day4.find_guard("[1518-11-01 00:05] falls asleep")
    assert False == result

