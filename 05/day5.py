import re
from string import ascii_lowercase

def trigger_polymer(polymer):
    if polymer:
        i = 0
        while i < len(polymer) - 2:
            if polymer[i].swapcase() == polymer[i+1]:
                polymer = polymer[:i] + polymer[i+2:]
                if i > 0: i = i - 1
            else:
                i += 1
        if len(polymer) > 1 and polymer[-1].swapcase() == polymer[-2]:
            return polymer[:-2]
        return polymer
    return ""

def remove_unit(unit, polymer):
    insensitive_unit = re.compile(re.escape(unit), re.IGNORECASE)
    return insensitive_unit.sub("", polymer)

def main(inputFile):
    polymer = open(inputFile).readline().strip()

    shortest = len(trigger_polymer(polymer))
    print("Part 1:", shortest)


    for c in ascii_lowercase:
        temp = len(trigger_polymer(remove_unit(c, polymer)))
        if temp < shortest:
            shortest = temp
    print("Part 2:", shortest)

if __name__ == "__main__":
    main("input")
