from data_structures_and_algorithms_python.challenges.array_binary_search.array_binary_search import binarySearch



def test_binarySearch():
    arr = [ 2, 3, 4, 10, 40 ]
    actual = binarySearch(arr, 0, len(arr)-1, 10)
    expected = 3
    assert actual == expected