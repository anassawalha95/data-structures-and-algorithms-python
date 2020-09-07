# Trees

A tree data structure can be defined recursively as a collection of nodes (starting at a root node), where each node is a data structure consisting of a value, together with a list of references to nodes (the "children"), with the constraints that no reference is duplicated, and none points to the root.

## Challenge

Create a Binary Tree Class and Binary Search Tree Class

## Approach & Efficiency

* I Used Depth First to traversals the tree.

* ***Depth First***is where we prioritize going through the depth (height) of the tree first.

* ***Binary Search Tree (BST)*** is a type of tree that does have some structure attached to it. In a BST, nodes are organized in a manner where all values that are smaller than the root are placed to the left, and all values that are larger than the root are placed to the right.


## API

* *preOrder method* - Return array of the tree values using this order: ***root >> left >> right***

* *inOrder method* - Return array of the tree values using this order: ***left >> root >> right***

* *postOrder method* - Return array of the tree values using this order: ***left >> right >> root***

* *add method* - Accepts a value, and adds a new node with that value in the correct location in the binary search tree.

* *contains method* - Accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once



# Find Maximum Value in a Tree

### Challenge Description

* Create an instance method for a BinaryTree class called find-maximum-value

### Approach & Efficiency

* I used the in-order method that I created before to retrive all the values in the tree then I did a loop to find the maximum value.

### Solution

![photo](/assets/tree-max-value.jpg)


# Breadth-first Traversal

### Challenge Description

* Write a breadth first traversal method which takes a Binary Tree as its unique input,traversing the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

### Solution

![photo](/assets/bridth-first.jpg)