from day8 import *

def test_node_no_childern_return_sum_of_data():
    _, sum = sum_metadata([0, 3, 1, 2, 3])
    assert 6 == sum

def test_node_1_child_return_sum_of_both():
    _, sum = sum_metadata([1, 3, 0, 1, 1, 1, 2, 3])
    assert 7 == sum

def test_2_children():
    _, sum = sum_metadata([2, 3, 0, 1, 1, 0, 1, 1, 1, 2, 3])
    assert 8 == sum

