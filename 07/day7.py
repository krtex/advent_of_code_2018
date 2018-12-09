from string import ascii_uppercase
import re
from operator import attrgetter

class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.before = []
        self.after = []

    def __repr__(self):
        return self.letter

    def __str__(self):
        return "Letter {}".format(self.letter)

    def print_relations(self):
        print(self.before, self.after)

def generate_uppercase_alphabet():
    alphabet = {}
    for c in ascii_uppercase:
        letter = Letter(c)
        alphabet[c] = letter
    return alphabet

def create_realtions_betwen_letters(data, alphabet):
    for line in data:
        res = re.search(r"(\w) must .* (\w) can", line)
        before = res.group(1)
        after = res.group(2)
        alphabet[before].after.append(alphabet[after])
        alphabet[after].before.append(alphabet[before])

    to_be_removed = []
    for l in alphabet:
        if alphabet[l].before == alphabet[l].after:
            to_be_removed.append(l)
    for i in to_be_removed:
        del alphabet[i]

def connect_root_with_alphabet(alphabet):
    root = Letter('.')
    for l in alphabet:
        if alphabet[l].before == []:
            alphabet[l].before.append(root)
            root.after.append(alphabet[l])
    alphabet['.'] = root

def add_to_pretendents(pretendents, descendants):
    pretendents = set(pretendents)
    descendants = set(descendants)
    pretendents |= descendants
    pretendents = list(pretendents)
    pretendents.sort(key=attrgetter('letter'))
    return pretendents

def find_letter_with_least_ancestors(pretendents):
    choice = '.'
    ancestors = 27 #more than alphabet;)
    for l in pretendents:
        if len(l.before) < ancestors:
            choice = l.letter
            ancestors = len(l.before)
    return choice

def remove_connection_with_descendants(letter):
    temp = []
    for l in letter.after:
        temp.append(l)
        if letter in l.before: l.before.remove(letter)
    for l in temp:
        letter.after.remove(l)

def add_to_result(letter, result):
    result.append(letter.letter)
    remove_connection_with_descendants(letter)

def print_dict(alphabet):
    for i in alphabet:
        print(alphabet[i])
        alphabet[i].print_relations()
    print("\n")

def resolve_order(alphabet, letter, pretendents, result):
    pretendents = add_to_pretendents(pretendents, alphabet[letter].after)
    ch = find_letter_with_least_ancestors(pretendents)
    pretendents = add_to_pretendents(pretendents, alphabet[ch].after)
    add_to_result(alphabet[ch], result)
    if alphabet[ch] in pretendents:
        pretendents.remove(alphabet[ch])
        resolve_order(alphabet, ch, pretendents, result)

def main(input_file):
    data = open(input_file).readlines()
    alphabet = generate_uppercase_alphabet()
    create_realtions_betwen_letters(data, alphabet)
    connect_root_with_alphabet(alphabet)

    pretendents = []
    result = []
    resolve_order(alphabet, '.', pretendents, result)

    print("Result\n",''.join(result[:-1]))

if __name__ == "__main__":
    main("input")

