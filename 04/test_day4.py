import day4
import numpy as np

reference = open("test_input").readlines()

def test_sort():
    input = open("test_random").readlines()
    input.sort()
    assert input == reference

def test_parse_guards_return_id_as_string():
    result = day4.find_guard("[1518-11-01 00:00] Guard #10 begins shift")
    assert '10' == result

def test_no_guard_found_return_false():
    result = day4.find_guard("[1518-11-01 00:05] falls asleep")
    assert False == result

def test_parse_sleep_return_time():
    result = day4.get_goodnight_time("[1518-11-01 00:05] falls asleep", "falls asleep")
    assert 5 == result

def test_parse_invalid_value_return_fale():
    result = day4.get_goodnight_time("asleep", "falls asleep")
    assert False == result

def test_parse_wakeup_return_time():
    result = day4.get_goodnight_time("[1518-11-01 00:55] wakes up", "wakes up")
    assert 55 == result

def test_given_array_return_key_with_max_value():
    schedule = {
        "1"  : [1, 2, 3, 4],
        "20" : [5, 6, 7, 8]
    }
    best = day4.find_best_time(schedule)
    assert ("20", 8) == best
    assert 60 == day4.calculate_best_shift_and_time(schedule, best)

