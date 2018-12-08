from functools import reduce
import re

def sum_metadata(input):
    HEADER = 2
    children, data = input[:HEADER]

    ch_sum = 0
    ch_length = 0
    for i in range(children):
        cl, cs = sum_metadata(input[HEADER + ch_length:])
        ch_sum += cs
        ch_length += cl

    my_length = HEADER + ch_length + data
    my_sum = reduce((lambda x,y: x+y), input[HEADER + ch_length : HEADER + ch_length + data]) + ch_sum
    return my_length, my_sum

def main(inputFile):
    input = list(map(int, open(inputFile).readline().strip().split(' ')))
    print(sum_metadata(input))

if __name__ == "__main__":
    main("input")

