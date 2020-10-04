# Graphs


## Challenge

Implement the graph, which should be represented as an adjacency list, and should include the following methods: add_node(), add_edge(), get_nodes(), get_neighbors(), size()

## Approach & Efficiency

- add_node() time Big O(1), space Big O(1)

- add_edge() time Big O(1), space Big O(1)

- get_nodes() time Big O(1), space Big O(1)

- get_neighbors() time Big O(1), space Big O(1)

- size() time Big O(1), space Big O(1)

## API

- class Node():

    - Class to create Node with the given value

- class Graph():

    - class to implement Graph object with the given methods:

- add_node(): add new node to the graph

- add_edge(): add an edge between tow nodes in the graph

- get_nodes(): Returns all of the nodes in the graph as a collection

- get_neighbors(): Returns a collection of nodes connected to the given node with the weights of their connections

- size(): Returns the total number of nodes in the graph


# Breadth-first method

### Challenge

Implement a breadth-first traversal on a graph.

### Approach & Efficiency

    breadth_first time Big O(n), space Big O(n)

### Solution
 ![photo](/assets/breadth-first-graph.jpg)