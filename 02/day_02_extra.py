from sys import argv

def compareTwoLines(first, second):
    f = set(first)
    s = set(second)

    f.intersection_update(s)

    if len(f) == len(s) or len(f)+1 == len(s):
        return ''.join(sorted(str(c) for c in f))
    return False

def main(pathToFile):
    with open(pathToFile) as f:
            lines = f.read().splitlines()

    for i, line1 in enumerate(lines):
        for line2 in lines[i+1:]:
            result = compareTwoLines(line1, line2)
            if result != False:
                result

if __name__ == "__main__":
    _, input = argv
    print(main(input))


