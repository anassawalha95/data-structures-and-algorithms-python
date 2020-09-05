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
