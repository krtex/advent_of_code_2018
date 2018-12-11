import numpy as np
import scipy.misc

def calculate_power(grid, sn):
    for x in range(1,len(grid) + 1):
        for y in range(1,len(grid) + 1):
            cell_rack_id = x +10
            grid[y-1, x-1] = int(((cell_rack_id * y + sn) * cell_rack_id) / 100) % 10 - 5

def sum_array(arr):
    return sum(map(sum,arr))

def sum_power_of_9(grid, x, y):
    return sum_array(grid[y - 1 : y + 3 - 1, x - 1 : x + 3 - 1])

def get_position_of_max_power(grid):
    max_energy = -float('Inf')
    position = (0, 0)
    for x in range(1,len(grid) + 1 - 2):
        for y in range(1,len(grid) + 1 -2):
            temp = sum_power_of_9(grid, x, y)
            #print("Power =", temp)
            if temp > max_energy:
                max_energy = temp
                position = (x, y)
    print("Power =", max_energy)
    return position

def main():
    size = 300
    grid = np.zeros((size,size))
    serial_number = 2694
    calculate_power(grid, serial_number)
    print(get_position_of_max_power(grid))
    #print(grid)
    scipy.misc.imsave("grid.jpg", grid)


if __name__ == "__main__":
    main()
