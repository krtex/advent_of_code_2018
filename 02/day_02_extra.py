from sys import argv

def compareTwoLines(first, second):
    result = ""
    for c1, c2 in zip(first, second):
        if c1 == c2:
            result += c1

    return result if len(result) + 1 >= len(first) else False

def main(pathToFile):
    with open(pathToFile) as f:
            lines = f.read().splitlines()

    for i, line1 in enumerate(lines):
        for line2 in lines[i+1:]:
            result = compareTwoLines(line1, line2)
            if result != False:
                return result

if __name__ == "__main__":
    _, input = argv
    print(main(input))


