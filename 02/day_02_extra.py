from sys import argv

def compareTwoLines(first, second):
    differences = 0
    result = ""

    for i, c in enumerate(first):
        if c != second[i]:
            differences += 1
        else:
            result += c

    return result if differences < 2 else False

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


