import numpy as np
import re

def parse_line(line):
    res = re.search(f"(\d+), *(\d+)", line)
    return [int(res.group(1)), int(res.group(2))]

def parse_input(inputFile):
    lines = open(inputFile).readlines()
    points = np.zeros(shape=(len(lines), 2)).astype(int)
    for i, line in enumerate(lines):
        points[i] = parse_line(line)
    return points

def normalize_points(points):
    points[:,0] -= min(points[:,0])
    points[:,1] -= min(points[:,1])

def main():
    points = parse_input("input")
    normalize_points(points)
    size_x = int(max(points[:,0])) + 1
    size_y = int(max(points[:,1])) + 1
    space = [(0,0)] * (size_x * size_y)

    #print(points)

    for j, p in enumerate(points):
        space[p[0] * size_x + p[1]] = (0, j)
        for i, point in enumerate(space):
            pos_x = int(i / size_x)
            pos_y = i % size_y
            dist = abs(p[0] - pos_x) + abs(p[1] - pos_y)
            point = dist, j
    print(space)

if __name__ == "__main__":
    main()
