import sys

_, inputFile = sys.argv

# Causes recursion depth error xD
def addLines(file, previousSum):
    line = file.readline()

    if(line):
        previousSum += int(line)
        addLines(file, previousSum)

data = open(inputFile)
print(addLines(data, 0))
data.close()

