import sys

_, inputFile = sys.argv

def addLines(file):
    sum = 0
    for line in file:
        sum += int(line)
    return sum

print(addLines(open(inputFile)))

