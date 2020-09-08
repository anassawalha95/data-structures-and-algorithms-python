import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
import pytest
from data_structures_and_algorithms_python.challenges.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz, fizz_buzz_tree
from data_structures_and_algorithms_python.data_structures.tree.tree import BinaryTree, Node

@pytest.fixture
def my_tree():
    tree = BinaryTree()
    tree.root = Node(6)
    tree.root.left = Node(15)
    tree.root.right = Node(7)
    tree.root.left.left = Node(23)
    tree.root.left.right = Node(21)
    tree.root.right.right = Node(5)
    tree.root.left.left.left = Node(15)
    tree.root.right.right.left = Node(7)
    return tree

def test_fizz_buzz6(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.value == "Fizz"

def test_fizz_buzz15(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.left.value == "FizzBuzz"

def test_fizz_buzz7(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.right.value == "7"

def test_fizz_buzz23(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.left.left.value == "23"

def test_fizz_buzz21(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.left.right.value == "Fizz"


def test_fizz_buzz5(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.right.right.value == "Buzz"

def test_fizz_buzz15_samevalue(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.left.left.left.value == "FizzBuzz"

def test_fizz_buzz7_samevalue(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.right.right.left.value == "7"

def test_empty_tree():
    tree = BinaryTree()
    new_tree = fizz_buzz_tree(tree)
    assert new_tree.root == None