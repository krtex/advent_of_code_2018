def countRepeating(input):
    letters = set()
    doubles = set()
    triples = set()
    for c in input:
        if c in letters:
            if c in doubles:
                triples.add(c)
                doubles.remove(c)
            else:
                doubles.add(c)
        else:
            letters.add(c)
    return int(len(doubles) != 0), int(len(triples) != 0)

def main(inputFile):
    doubles = 0
    triples = 0
    for line in inputFile:
        d, t = countRepeating(line)
        doubles += d
        triples += t

    print("Checksum =", doubles*triples)

if __name__ == "__main__":
    main(open("input", 'r'))

