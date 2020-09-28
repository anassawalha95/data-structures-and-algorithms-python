import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.data_structures.tree.tree import BinaryTree, Node


def tree_intersection(bt1,bt2):

    output = []
    
    def _walk(node1,node2):
        if not node1 or not node2:
            return None
        
        if node1.value == node2.value:
            output.append(node1.value)

        _walk(node1.left,node2.left)
        _walk(node1.right,node2.right)
    _walk(bt1.root,bt2.root)

    if len(output)<1:
        return None
    else:
        return output