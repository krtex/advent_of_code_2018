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

def main(inputFile):
    print("Part 1:", len(trigger_polymer(open(inputFile).readline().strip())))

if __name__ == "__main__":
    main("input")
