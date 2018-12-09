from day7 import *

def test_parse():
    assert 1

def test_finding_ancestors():
    a = Letter('A')
    b = Letter('B')
    b.before.append(a)
    lst = []
    lst += [a, b]
    assert 'A' == find_letter_with_least_ancestors(lst)

def test_finding_ancestors():
    a = Letter('A')
    b = Letter('B')
    c = Letter('C')
    b.before.append(a)
    a.after.append(b)
    a.after.append(c)
    c.before.append(a)
    b.after.append(c)
    c.before.append(b)
    a.print_relations()
    b.print_relations()
    c.print_relations()
    lst = dict()
    lst['A'] = a; lst['B'] = b; lst['C'] = c
    remove_connection_with_descendants(lst['A'])
    a.print_relations()
    b.print_relations()
    c.print_relations()


