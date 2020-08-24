from data_structures_and_algorithms_python.data_structures.linked_list.linked_list import Node, Linkedlist


def test_empty_linked_list():
    a = Linkedlist()
    expected = None
    actual = print(a)
    assert expected == actual

def test_insert_to_linked_list():
    nums = Linkedlist()
    nums.insert(0)
    nums.insert(1)
    nums.insert(2)
    nums.insert(3)
    expected = "{ 0 } -> { 1 } -> { 2 } -> { 3 } -> NULL"
    actual = nums.__str__()
    assert expected == actual

def test_includes_true_linked_list():
    nums = Linkedlist()
    nums.insert(0)
    nums.insert(1)
    nums.insert(2)
    nums.insert(3)
    expected = True
    actual = nums.includes(3)
    assert expected == actual

def test_includes_false_linked_list():
    nums = Linkedlist()
    nums.insert(0)
    nums.insert(1)
    nums.insert(2)
    nums.insert(3)
    expected = False
    actual = nums.includes(10)
    assert expected == actual

def test_head_linked_list():
    nums = Linkedlist()
    nums.insert(0)
    nums.insert(1)
    nums.insert(2)
    nums.insert(3)
    assert nums.head.value == 0

def test_insert_after():
    ll = Linkedlist()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert_after(1,5)
    actual = ll.__str__()
    expected =  "{ 1 } -> { 5 } -> { 2 } -> { 3 } -> NULL"
    assert actual == expected


def test_insert_before():
    ll = Linkedlist()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert_before(2,5)
    actual = ll.__str__()
    expected =  "{ 1 } -> { 5 } -> { 2 } -> { 3 } -> NULL"
    assert actual == expected


def test_append():
    ll = Linkedlist()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.__str__()
    expected =  "{ 1 } -> { 2 } -> { 3 } -> NULL"
    assert actual == expected

def test_kth_from_end_0():
    ll = Linkedlist()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = 2
    actual =ll.kth_from_end(0)
    assert expected == actual

def test_kth_from_end_2():
    ll = Linkedlist()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = 3
    actual =ll.kth_from_end(2)
    assert expected == actual

def test_kth_from_end_6():
    ll = Linkedlist()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "The Value Nott Found"
    actual =ll.kth_from_end(6)
    assert expected == actual