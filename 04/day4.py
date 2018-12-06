import re

input = open("test_random").readlines()

def find_guard(line):
    guard = re.search(r"#(\d+)", line)
    return int(guard.group(1)) if guard else False

