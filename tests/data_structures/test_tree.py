import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.data_structures.tree.tree import BinaryTree, BinarySearchTree,Node

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

def test_post_order_traversal():
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

def test_find_max_value_empty():
    bt = BinaryTree()
    expected = 'Tree is empty'
    actual = bt.find_maximum_value()
    assert expected == actual

def test_find_max_value():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    expected = 11
    actual = bt.find_maximum_value()
    assert expected == actual

def test_breadth_first_binarytree_empty():
    bt = BinaryTree()
    assert BinaryTree.breadth_first_traversal(bt) == None

def test_breadth_first_binarytree_one_element():
    bt= BinaryTree()
    bt.root = Node(8)
    assert BinaryTree.breadth_first_traversal(bt) == [8]

def test_breadth_first_binarytree():
    bt= BinaryTree()
    bt.root = Node(2)
    bt.root.left = Node(7)
    bt.root.right = Node(5)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.right.right = Node(9)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right.left = Node(4)

    assert BinaryTree.breadth_first_traversal(bt) == [2,7,5,2,6,9,5,11,4]