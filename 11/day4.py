import numpy as np

def create_grid(size):
    return np.zeros((size + 1, size + 1))

def calculate_power(grid, sn):
    for x in range(1,len(grid)):
        for y in range(1,len(grid)):
            cell_rack_id = x +10
            grid[y, x] = int(((cell_rack_id * y + sn) * cell_rack_id) / 100) % 10 - 5

def sum_array(arr):
    return sum(map(sum,arr))

def sum_power_of_9(grid, x, y):
    return sum_array(grid[y : y + 3, x : x + 3])

def get_position_of_max_power_of_9(grid):
    max_energy = -float('Inf')
    position = (0, 0)
    for x in range(1, len(grid) - 2):
        for y in range(1, len(grid) - 2):
            temp = sum_power_of_9(grid, x, y)
            #print("Power =", temp)
            if temp > max_energy:
                max_energy = temp
                position = (x, y)
    print("Power =", max_energy)
    return position

def sum_area(grid):
    for x in range(1,len(grid)):
        for y in range(1,len(grid)):
            grid[y, x] = grid[y, x] + grid[y - 1, x] + grid[y, x - 1] - grid[y - 1, x - 1]

def get_position_of_max_power(grid):
    max_energy = -float('Inf')
    position = (0, 0)
    size = 0

    for diag in range(1, len(grid)):
        for x in range(diag, len(grid)):
            for y in range(diag, len(grid)):
                temp = grid[y, x] + grid[y - diag, x - diag] - grid[y - diag, x] - grid[y, x - diag]
                if temp > max_energy:
                    max_energy = temp
                    position = (x - diag + 1, y - diag + 1)
                    size = diag
    print("Power =", max_energy)
    return position, size

def main():
    size = 300
    grid = create_grid(size)
    serial_number = 2694
    calculate_power(grid, serial_number)
    print(get_position_of_max_power_of_9(grid))
    sum_area(grid)
    print(get_position_of_max_power(grid))

if __name__ == "__main__":
    main()
