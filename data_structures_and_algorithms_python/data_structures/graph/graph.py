import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.data_structures.graph.queue import Queue
# from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """
        Method to add new node to the graph
        """
        node = Node(value)
        self._adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=1):
        """
        Method to add an edge between tow nodes in the graph
        """

        if start_node not in self._adjacency_list:
            raise KeyError('Start Node not in Graph')

        if end_node not in self._adjacency_list:
            raise KeyError('End Node not in Graph')

        adjacencies = self._adjacency_list[start_node]

        adjacencies.append((end_node,weight))

    def get_nodes(self):
        """
        Method to Returns all of the nodes in the graph as a collection
        """
        return self._adjacency_list.keys()

    def get_neighbors(self, node):
        """
        Method to Returns a collection of nodes connected to the given node with the weights of their connections
        """
        return self._adjacency_list[node]

    def size(self):
        """
        Method to Returns the total number of nodes in the graph
        """
        return len(self._adjacency_list)

    def breadth_first(self, start_node):
        """
        Method to do breadth-first traversal on a graph.
        """
        output = []
        q = Queue()

        if start_node not in self._adjacency_list:
            raise ValueError

        q.enqueue(start_node)

        while len(q):
            cur = q.dequeue()
            output.append(cur)

            neighbors = self._adjacency_list[cur]
            for n in neighbors:
                if not n[0].visited:
                    n[0].visited = True
                q.enqueue(n[0])

        for node in self._adjacency_list:
            node.visited = False
        
        return output


# if __name__ == "__main__":
    
#     g = Graph()

#     a = g.add_node('a')
#     b = g.add_node('b')
#     c = g.add_node('c')
    

#     g.add_edge(a,b,4)
#     g.add_edge(b,c,6)

#     # print(g.get_nodes())
#     print(g.get_neighbors(a))
#     # print(g.size())
