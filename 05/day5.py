def trigger_polymer(polymer):
    if polymer:
        i = 0
        while i < len(polymer) - 2:
            if polymer[i].swapcase() == polymer[i+1]:
                polymer = polymer[:i] + polymer[i+2:]
            i += 1
        if polymer[0].swapcase() == polymer[1]:
            return ""
        return polymer
    return ""
