import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.challenges.quick_sort.quick_sort import quick_sort

def test_merge_sort_one():
    lst = [8,4,23,42,16,15]
    quick_sort(lst)
    expected = [4,8,15,16,23,42]
    actual = lst
    assert actual == expected

def test_merge_sort_tow():
    lst = [20,18,12,8,5,-2]
    quick_sort(lst)
    expected = [-2, 5, 8, 12, 18, 20]
    actual = lst
    assert actual == expected

def test_merge_sort_three():
    lst = [5,12,7,5,5,7]
    quick_sort(lst)
    expected = [5, 5, 5, 7, 7, 12]
    actual = lst
    assert actual == expected

def test_merge_sort_four():
    lst = [2,3,5,7,13,11]
    quick_sort(lst)
    expected = [2, 3, 5, 7, 11, 13]
    actual = lst
    assert actual == expected