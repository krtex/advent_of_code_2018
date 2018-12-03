import numpy as np
import re
import scipy.misc
from functools import reduce

def parseLine(line):
    id, _, xpos, ypos, xsize, ysize = re.split(' |,|: |x|\n',line)
    position = (int(xpos), int(ypos))
    size = (int(xsize), int(ysize))
    return id, position, size

def putPatchOnFabric(fabric, position, size):
    xpos, ypos = position
    xsize, ysize = size
    fabric[xpos:xpos+xsize, ypos:ypos+ysize] += 1

def getValueOfPatch(fabric, position, size):
    xpos, ypos = position
    xsize, ysize = size
    return np.sum(fabric[xpos:xpos+xsize, ypos:ypos+ysize])

def part1(fabric, lines):
    for line in lines:
        _, position, size = parseLine(line)
        putPatchOnFabric(fabric, position, size)

    counted_zeros = np.count_nonzero(fabric==0)
    counted_ones = np.count_nonzero(fabric==1)
    print("Overlaping area is equal to", 1000000 - counted_zeros - counted_ones)

def part2(fabric, lines):
    for line in lines:
        id, position, size = parseLine(line)
        if getValueOfPatch(fabric, position, size) == reduce(lambda a,b: a*b, size):
            print("Patch id is", id)
            break

def main(pathToFile):
    with open(pathToFile) as f:
        lines = f.read().splitlines()

    fabric = np.zeros((1000, 1000))
    part1(fabric, lines)
    part2(fabric, lines)
    #    scipy.misc.imsave('outfile.jpg', fabric)

if __name__ == "__main__":
    main("input")

