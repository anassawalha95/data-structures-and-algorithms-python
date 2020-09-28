# import sys
# sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
# from data_structures_and_algorithms_python.data_structures.stacks_and_queues.stacks_and_queues import Queue

class Node:
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right = None
        self.next = None


class Queue:
    """class Queue which implements Queue data structure with its common methods"""

    def __init__(self):
        """Initiate class"""

        self.front = None
        self.rear = None

    def is_empty(self):
        """method to check if Queue is empty"""

        if self.front == None:
            return True
        return False


    def enqueue(self, node):
        """Method that takes any value as an argument and adds a new node with that value to the back of the queue """

        new_node = node

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns the node’s value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """Method that returns the value of the node located in the front of the queue, without removing it from the queue."""

        if not self.is_empty():
            return self.front.value
        return None


class BinaryTree:
    def __init__(self):
        self.root = None
        
    def pre_order(self):
        """
        Method to returns the tree values using pre order - root >> left >> right
        """
        output = []
        def _walk(node):
            if not node:
                return
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)
        _walk(self.root)
        return output

    def in_order(self):
        """
        Method to returns the tree values using in order - left >> root >> right
        """
        output = []
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            output.append(node.value)
            _walk(node.right)
        _walk(self.root)
        return output
        
    def post_order(self):
        """
        Method to returns the tree values using post order - left >> right >> root
        """
        output = []
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            _walk(node.right)
            output.append(node.value)
        _walk(self.root)
        return output


    def find_maximum_value(self):
        """
        Method To Find The Maximum Value in The Tree
        """
        try:
            self.root.value

        except AttributeError as e:
            return 'Tree is empty'
        else:
            output = self.in_order()
            val = -10000
            for i in range(len(output)):
                if output[i] > val:
                    val = output[i]
            return val
        
    @staticmethod
    def breadth_first_traversal(bt):

        result = []
        
        if bt.root is None:
            return

        queue = Queue()
        queue.enqueue(bt.root)
        # y = 0
        while queue.peek():
            # y+=1
            # val = queue.peek()
            # if type(val) == type('str'):
            #     break
            node = queue.dequeue()
            result.append(node.value)

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        # print(y)
        return result
        


    
    def __str__(self):
        output = []
        def _walk(node):
            if not node:
                return
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)
        _walk(self.root)
        return f'tree {output}'


class BinarySearchTree(BinaryTree):

    def add(self, value):
        """
        Method to adds a new node with that value in the correct location in the binary search tree.
        """
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while (current):
                if current.value > value: # Got to left
                    if current.left == None: # if current is a leaf
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None: # if current is a leaf
                        current.right = Node(value)
                        break
                    current = current.right

    
    def contais(self, value):
        """
        Method that returns a boolean indicating whether or not the value is in the tree at least once. 
        """
        if not self.root:
            return 'value not found'
        else:
            current = self.root
            while (current):
                if current.value==value:
                    return True
                if current.value > value: 
                    if current.left == None: 
                        return 'value not found'
                    current = current.left
                else:
                    if current.right == None: 
                        return 'value not found'
                    current = current.right
    


if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.add(50)
    bst.add(30)
    bst.add(100)
    bst.add(25)
    bst.add(33)
    bst.add(70)
    bst.add(105)
    # print(bst.post_order())
    print(bst.contais(105))

    # bt = BinaryTree()
    # bt.root = Node(1)
    # bt.root.left = Node(2)
    # bt.root.right = Node(3)
    # bt.root.left.left = Node(4)
    # bt.root.left.right = Node(5)
    # print(bt.breadth_first_traversal(bt))
