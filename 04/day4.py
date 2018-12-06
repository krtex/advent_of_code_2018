import re
import numpy as np

input = open("test_random").readlines()

def find_guard(line):
    guard = re.search(r"#(\d+)", line)
    return guard.group(1) if guard else False

def get_goodnight_time(line, action):
    parsed_line = re.search(r":(\d+)\] (.*)", line)
    return int(parsed_line.group(1)) if (parsed_line and parsed_line.group(2) == action) else False

def get_sleep(data, idx):
    down = get_goodnight_time(data[idx], "falls asleep")
    up = get_goodnight_time(data[idx+1], "wakes up")
    return idx+2, down, up

def add_sleep(schedule, guard, sleep_time, wake_time):
    timetable = np.zeros(60)
    timetable[sleep_time:wake_time] = 1
    if guard in schedule:
        schedule[guard] += timetable
    else:
        schedule[guard] = timetable

def find_best_time(schedule):
    best = ("", -1)

    for g in schedule:
        temp = max(schedule[g])
        if temp > best[1]:
            best = (g, temp)
    print(best)
    return best

def calculate_best_shift_and_time(schedule, best):
    for i, elem in enumerate(schedule[best[0]]):
        print(i, elem)
        if elem == best[1]:
            return i * int(best[0])
    return False

def main(input_file):
    data = open(input_file).readlines()
    data.sort()
    schedule = {}

    i = 0
    while i < len(data)-2:
        g = find_guard(data[i])
        if False != g:
            guard = g
            i += 1
        if not find_guard(data[i+1]):
            i, sleep_time, wake_time = get_sleep(data, i)
            add_sleep(schedule, guard, sleep_time, wake_time)
        else:
            i += 1

    print(calculate_best_shift_and_time(schedule, find_best_time(schedule)))

if __name__ == ("__main__"):
    main("test_random")
