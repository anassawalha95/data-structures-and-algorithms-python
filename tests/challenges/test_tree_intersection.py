import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.challenges.tree_intersection.tree_intersection import tree_intersection
from data_structures_and_algorithms_python.data_structures.tree.tree import BinaryTree, Node

def test_tree_intersection_one():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    bt1 = BinaryTree()
    bt1.root = Node(1)
    bt1.root.left = Node(8)
    bt1.root.right = Node(9)
    bt1.root.left.left = Node(6)
    bt1.root.left.right = Node(5)

    expected = [1,5]
    assert expected == tree_intersection(bt,bt1)

def test_tree_intersection_tow():
    bt = BinaryTree()
    bt.root = Node(10)
    bt.root.left = Node(6)
    bt.root.right = Node(7)
    bt.root.left.left = Node(5)
    bt.root.left.right = Node(5)
    bt.root.left.right.left = Node(50)

    bt1 = BinaryTree()
    bt1.root = Node(10)
    bt1.root.left = Node(8)
    bt1.root.right = Node(9)
    bt1.root.left.left = Node(6)
    bt1.root.left.right = Node(5)
    bt1.root.left.right.left = Node(50)
    expected = [10,5,50]
    assert expected == tree_intersection(bt,bt1)

def test_tree_intersection_three():
    bt = BinaryTree()
    bt.root = Node(10)
    bt.root.left = Node(6)
    bt.root.right = Node(7)
    bt.root.left.left = Node(5)
    bt.root.left.right = Node(5)
    bt.root.left.right.left = Node(50)

    bt1 = BinaryTree()
    bt1.root = Node(11)
    bt1.root.left = Node(8)
    bt1.root.right = Node(9)
    bt1.root.left.left = Node(6)
    bt1.root.left.right = Node(12)
    bt1.root.left.right.left = Node(0)
    expected = None
    assert expected == tree_intersection(bt,bt1)

def test_tree_intersection_four():
    bt = BinaryTree()
    bt.root = Node(10)
    bt.root.left = Node(6)
    bt.root.right = Node(7)
    bt.root.left.left = Node(5)
    bt.root.left.right = Node(5)
    bt.root.left.right.left = Node(50)

    bt1 = BinaryTree()
    bt1.root = Node(11)
    expected = None
    assert expected == tree_intersection(bt,bt1)


def test_tree_intersection_five():
    bt = BinaryTree()
    bt.root = Node(10)
    bt.root.left = Node(6)
    bt.root.right = Node(7)
    bt.root.left.left = Node(5)
    bt.root.left.right = Node(5)
    bt.root.left.right.left = Node(50)

    bt1 = BinaryTree()
    bt1.root = Node(10)
    expected = [10]
    assert expected == tree_intersection(bt,bt1)