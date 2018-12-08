from functools import reduce
import re

HEADER = 2

def sum_scope(input):
    return reduce((lambda x,y: x+y), input)

def sum_metadata(input):
    children, data = input[:HEADER]

    ch_length = 0
    ch_sum = 0
    for i in range(children):
        cl, cs = sum_metadata(input[HEADER + ch_length:])
        ch_length += cl
        ch_sum += cs

    my_length = HEADER + ch_length + data
    my_sum = sum_scope(input[HEADER + ch_length : HEADER + ch_length + data]) + ch_sum
    return my_length, my_sum

def get_root_value(input):
    children, data = input[:HEADER]
    my_value = 0

    ch_length = 0
    ch_values = []
    for i in range(children):
        cl, cv = get_root_value(input[HEADER + ch_length:])
        ch_length += cl
        ch_values.append(cv)

    if len(ch_values):
        for v in input[HEADER + ch_length : HEADER + ch_length + data]:
            if v-1 <  len(ch_values):
                my_value += ch_values[v-1]
    else:
        my_value = sum_scope(input[HEADER:HEADER + data])

    my_length = HEADER + ch_length + data
    return my_length, my_value


def main(inputFile):
    input = list(map(int, open(inputFile).readline().strip().split(' ')))
    print("Part 1", sum_metadata(input))
    print("Part 2", get_root_value(input))

if __name__ == "__main__":
    main("input")

