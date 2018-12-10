import numpy as np
import re
import scipy.misc

def parse_input(line):
        result = re.search(r"(-?\d+), *(-?\d+)(> velocity=<) *(-?\d+), *(-?\d+)", line) #", *(-?\d+)", line)
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
    pts, vels = create_points_and_velocities("input")
    normalize_points(pts)

    pts += 10000*vels
    sky = create_sky(pts)
    fill_the_sky(sky, pts)

    print(sky)

#    print(pts)
#    scipy.misc.imsave(name, picture)


if __name__ == "__main__":
    main()
