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
    #print("Timetable", guard, "guard\n", schedule)
    if guard in schedule:
        schedule[guard] += timetable
        return schedule[guard]
    else:
        schedule[guard] = timetable
        return schedule[guard]

def main(input_file):
    data = open(input_file).readlines()
    data.sort()
    schedule = {}

    i = 0
    while i < len(data)-2:
        guard = find_guard(data[i])
        print("Guard:", guard, "in", i)
        if not find_guard(data[i+1]):
            i, sleep_time, wake_time = get_sleep(data, i+1)
            schedule = add_sleep(schedule, guard, sleep_time, wake_time)
        else:
            i += 1

    print(schedule)

if __name__ == ("__main__"):
    main("input_short")
