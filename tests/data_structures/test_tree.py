import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.data_structures.tree.tree import BinaryTree, BinarySearchTree

def test_empty_binary_tree():
    bt = BinaryTree()
    assert bt.root == None

def test_single_root_tree():
    bst = BinarySearchTree()
    bst.add(50)
    expected = 50
    actual = bst.root.value
    assert expected == actual

def test_add_left_child_and_right_child():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(100)
    bst.add(25)
    expected = 100
    actual = bst.root.right.value
    assert expected == actual

def test_pre_order_traversal():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(100)
    bst.add(30)
    bst.add(25)
    bst.add(33)
    bst.add(70)
    bst.add(105)
    expected = [50, 30, 25, 33, 100, 70, 105]
    actual = bst.pre_order()
    assert expected == actual

def test_in_order_traversal():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(100)
    bst.add(30)
    bst.add(25)
    bst.add(33)
    bst.add(70)
    bst.add(105)
    expected = [25, 30, 33, 50, 70, 100, 105]
    actual = bst.in_order()
    assert expected == actual

def test_pos_torder_traversal():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(100)
    bst.add(30)
    bst.add(25)
    bst.add(33)
    bst.add(70)
    bst.add(105)
    expected = [25, 33, 30, 70, 105, 100, 50]
    actual = bst.post_order()
    assert expected == actual