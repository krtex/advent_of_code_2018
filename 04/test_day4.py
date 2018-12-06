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

# def test_find_guard():
#     arr = np.array([np.zeros(2),np.zeros(2)])
#     arr[1,1] = 1
#     assert 1 == int(np.where(arr[1,:] == 1)))
