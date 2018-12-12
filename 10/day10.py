import numpy as np
import re
import scipy.misc

def parse_input(line):
        result = re.search(r"(-?\d+), *(-?\d+)(> velocity=<) *(-?\d+), *(-?\d+)", line)
        pos = [int(result.group(1)),  int(result.group(2))]
        vel = [int(result.group(4)),  int(result.group(5))]
        return pos, vel

def create_points_and_velocities(inputFile):
    lines = open(inputFile).readlines()
    points = np.zeros(shape=(len(lines), 2))
    velocities = np.zeros(shape=(len(lines), 2))
    for i, line in enumerate(lines):
        pos, vel = parse_input(line)
        points[i] = pos
        velocities[i] = vel
    return points.astype(int), velocities.astype(int)

def normalize_points(points):
    points[:,0] -= min(points[:,0])
    points[:,1] -= min(points[:,1])

def create_sky(points):
    # indexes are fine, they're swap in a story, so i do the same here
    return np.zeros(shape=(int(max(points[:,1])) + 1, int(max(points[:,0])) + 1)).astype(int)

def fill_the_sky(sky, points):
    # indexes are fine, they're swap in a story, so i do the same here
    for p in points:
        sky[p[1], p[0]] = 1

def main():
    points, vels = create_points_and_velocities("input")
    points += 10080*vels # based on input size;)
    # that's an ugly solution. Proper one would search for the minimal
    # breadth of the points. Some day I'll improve it.
    for i in range(10):  # some int to iterate:P
        points += vels
        normalize_points(points)
        sky = create_sky(points)
        fill_the_sky(sky, points)
        scipy.misc.imsave("sky{}.jpg".format(i), sky)

if __name__ == "__main__":
    main()
