class Node:
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right = None

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
    print(bst.post_order())