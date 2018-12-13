import re

def to_num(char):
    return 1 if (char == '#') else 0

def to_char(num):
    return '#' if (num == 1) else '.'

def print_pots(pots):
    word = []
    while pots:
        word.append(to_char(pots & 1))
        pots >>= 1
    print("".join(word))

def create_header_and_body_from_file(inputFile):
    with open(inputFile) as myFile:
        header = "".join(re.findall(r"[#\.]", myFile.readline()))
        body = "".join(re.findall(r"[#\.]", myFile.read()))
    return header, body

def create_pots_from_header(header):
    pots = 0
    for i, c in enumerate(header):
        pots |= to_num(c) << i
    return pots

def create_masks_from_text(body):
    masks = []
    temp = 0
    for i, c in enumerate(body):
        if 5 == i % 6:
            masks.append((temp, to_num(c)))
            temp = 0
        else:
            temp |= to_num(c) << (i % 6)
    return masks

def pull_out_plants(pots, head):
    plants = 0
    #print("======================")
    for n in range(pots.bit_length()):
        if pots >> n & 1:
            #print(n)
            plants += n + 5
            #print(plants, i)#if pots & 1 else 0
        #pots >>= 1
    return plants

def get_next_generation_based_on_mask(pots, m, head):
    new_pots = 0
    for n in range(pots.bit_length()):
        if ((m[0] ^ (pots >> n)) & 31) == 0:
            new_pots |= m[1] << n
    return new_pots, 0
    # return new_pots

def func(pots):
    for i in range(pots.bit_length()):
        if pots >> i & 1:
            return i

def predict_future_of_plants(pots, masks, generation):
    new_pots = 0
    head = 0
    for i in range(1, generation + 1):
        for m in masks:
            while pots & 15 != 0:
                pots <<= 1
                head += 1
            res = get_next_generation_based_on_mask(pots, m, head)
            new_pots |= res[0]
            head += res[1]
            #new_pots |= res
        head -= func(new_pots)
        #print("HEAD", head)
        #print_pots(new_pots)
        if i == generation: total_plants = pull_out_plants(new_pots, head)
        pots = new_pots
        new_pots = 0
    print("Total plants in {} generations is:".format(generation), total_plants, head)
    return new_pots

def main():
    header, body = create_header_and_body_from_file("input")
    pots = create_pots_from_header(header)
    masks = create_masks_from_text(body)
    generation = 50000000000
    new_pots = predict_future_of_plants(pots, masks, generation)

if __name__ == "__main__":
    main()
