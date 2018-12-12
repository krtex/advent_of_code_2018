import re

def create_header_and_body_from_file(inputFile):
    with open(inputFile) as myFile:
        header = "".join(re.findall(r"[#\.]", myFile.readline()))
        body = "".join(re.findall(r"[#\.]", myFile.read()))
    return header, body

def to_num(char):
    return 1 if (char == '#') else 0

def to_char(num):
    return '#' if (num == 1) else '.'

def create_pots_from_header(header):
    pots = 0
    for i, c in enumerate(header):
        pots |= to_num(c) << len(header) -1 - i
    return pots

def create_masks_from_text(body):
    masks = []
    temp = 0
    for i, c in enumerate(body):
        if 5 == i % 6:
            masks.append((temp, to_num(c)))
            temp = 0
        else:
            temp |= to_num(c) << 4 - (i % 6)
    return masks

def pull_out_plants(pots, length_difference):
    plants = 0
    for i in range(pots.bit_length() - 1 -2, length_difference - 1 -4, -1):
        if pots & 1:
            plants += i
            print(plants, i)#if pots & 1 else 0
        pots >>= 1
    return plants

def print_pots(pots):
    word = []
    while pots:
        word.append(to_char(pots & 1))
        pots >>= 1
    print("".join(word[::-1]))

def get_next_generation_based_on_mask(pots, m):
    new_pots = 0
    for n in range(pots.bit_length()):
        if ((m[0] ^ (pots >> n)) & 31) == 0:
            new_pots |= m[1] << n
    return new_pots

def predict_future_of_plants_better_this_time(pots, masks, generation):
    new_pots = 0
    for i in range(1, generation + 1):
        for m in masks:
            pots = pots << 4 if (pots & 15 != 0) else pots
            new_pots |= get_next_generation_based_on_mask(pots, m)
        print_pots(new_pots)
        if i == generation: total_plants = pull_out_plants(new_pots, pots.bit_length() - new_pots.bit_length())
        pots = new_pots
        new_pots = 0
    print("Total plants in {} generations".format(generation), total_plants)
    return new_pots

def main():
    header, body = create_header_and_body_from_file("input_test")
    pots = create_pots_from_header(header)
    masks = create_masks_from_text(body)
    generation = 20
    new_pots = predict_future_of_plants_better_this_time(pots, masks, generation)

if __name__ == "__main__":
    main()
