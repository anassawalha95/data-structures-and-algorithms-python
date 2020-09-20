import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort_one():
    lst = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = insertion_sort(lst)

def test_insertion_sort_tow():
    lst = [20,18,12,8,5,-2]
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertion_sort(lst)

def test_insertion_sort_three():
    lst = [5,12,7,5,5,7]
    expected = [5, 5, 5, 7, 7, 12]
    actual = insertion_sort(lst)

def test_insertion_sort_four():
    lst = [2,3,5,7,13,11]
    expected = [2, 3, 5, 7, 11, 13]
    actual = insertion_sort(lst)