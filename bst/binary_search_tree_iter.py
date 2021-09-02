from .node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def _insert_node(self, node: Node, value):

        current = node
        parent: Node = None

        while current:
            parent = current

            if value < current.value:
                current = current.leftChild
            else:
                current = current.rightChild
        
        if value < parent.value:
            parent.leftChild = Node(value)
        else:
            parent.rightChild = Node(value)    


    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            return self._insert_node(self.root, value)
