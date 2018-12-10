from collections import deque
import time

def part12(players, marbles):
    score_table = [0] * players
    circle = deque([0])
    for i in range(1, marbles + 1):
        if i % 23:
            circle.rotate(-1)
            circle.append(i)
        else:
            circle.rotate(7)
            score_table[i % players] += i + circle.pop()
            circle.rotate(-1)

    return max(score_table)

def main():
    start = time.time()
    print(part12(470, 71))
    end = time.time()
    print("Time:", end - start)

    print(part12(470, 719))
    end = time.time()
    print("Time:", end - start)

    print(part12(470, 7194))
    end = time.time()
    print("Time:", end - start)

    print(part12(470, 71944))
    end = time.time()
    print("Time:", end - start)

    print(part12(470, 719440))
    end = time.time()
    print("Time:", end - start)

    print(part12(470, 7194400))
    end = time.time()
    print("Time:", end - start)

if __name__ == "__main__":
    main()
