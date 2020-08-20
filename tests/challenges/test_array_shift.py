from data_structures_and_algorithms_python.challenges.array_shift.array_shift import insertShiftArray 


def test_insertShiftArray():
    actual = insertShiftArray([2,4,6,8], 5)
    expected = [2,4,5,6,8]
    assert actual == expected

def test_insertShiftArray_1():
    actual = insertShiftArray([4,8,15,23,42], 16)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_insertShiftArray_2():
    actual = insertShiftArray([3,6,9,11],7)
    expected = [3,6,7,9,11]
    assert actual == expected

def test_insertShiftArray_3():
    actual = insertShiftArray([1,2,4,5], 3)
    expected = [1,2,3,4,5]
    assert actual == expected

def test_insertShiftArray_4():
    actual = insertShiftArray([1,2,3,4,7,8,9], 5)
    expected = [1,2,3,4,5,7,8,9]
    assert actual == expected

def test_insertShiftArray_5():
    actual = insertShiftArray([1,2,4,5,6], 3)
    expected = [1,2,4,3,5,6]
    assert actual == expected