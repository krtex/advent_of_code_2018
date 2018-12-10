import numpy as np
import re
import scipy.misc

def parse_input(line):
        result = re.search(r"(-?\d+), *(-?\d+)(> velocity=<) *(-?\d+), *(-?\d+)", line) #", *(-?\d+)", line)
        pos = int(result.group(1)),  int(result.group(2))
        vel = int(result.group(4)),  int(result.group(5))
        return pos, vel

def main():
    points = []
    velocities = []
    for line in open("input_test").readlines():
        pos, vel = parse_input(line)
        points.append(pos)
        velocities.append(vel)

    arr = np.array(points)
    max_x = max(arr[:,0])
    min_x = min(arr[:,0])
    max_y = max(arr[:,1])
    min_y = min(arr[:,1])

    if(min_x < 0): arr[:,0] -= min_x
    if(min_y < 0): arr[:,1] -= min_y

    size_x = max_x +abs(min_x) + 1
    size_y = max_y +abs(min_y) + 1
    picture = np.zeros((size_x, size_y))

    for p in arr:
        picture[p[0], p[1]] = 1
    print("\n",picture)

    for i in range(1,5):
        for i, p in enumerate(points):
            p += velocities[i] * i

        arr = np.array(points)
        arr[:,0] -= min_x
        arr[:,1] -= min_y
        picture = np.zeros((size_x, size_y))
        for p in arr:
            picture[p[0], p[1]] = 1
        print("\n",picture)

if __name__ == "__main__":
    main()
