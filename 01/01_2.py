import sys

_, inputFile = sys.argv

def addLines(file):
    sum = 0
    frequences = set()
    while(1):
        for line in file:
            sum += int(line)
            if sum in frequences:
                return sum
            frequences.add(sum)
        print("No frequence was reached twice!")
        file.seek(0)
    print(len(frequences))

print(addLines(open(inputFile)))

