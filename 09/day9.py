import timeit

def part1_slow(players, marbles):
    score_table = {}
    circle = [0]
    index = 0
    for i in range(marbles)[1:]:
        if i % 23:
            index = (index + 2) % len(circle)
            circle.insert(index, i)
        else:
            index = (index - 7) % len(circle)
            score = i + circle[index]
            del circle[index]
            if (i % players) in score_table:
                score_table[(i % players)] += score
            else:
                score_table[(i % players)] = score

    print(max(score_table.values()))

def part1_faster(players, marbles):
    score_table = [0] * players
    circle = [0]
    index = 0
    for i in range(marbles)[1:]:
        if i % 23:
            index = (index + 2) % len(circle)
            circle.insert(index, i)
        else:
            index = (index - 7) % len(circle)
            score = i + circle[index]
            del circle[index]
            score_table[i % players] += score

    print(max(score_table))

def main(players, marbles):
    #part1_slow(players, marbles)
    part1_faster(players, marbles)

if __name__ == "__main__":
    #main(9, 25)
    main(423, 7194400)

