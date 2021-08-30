class Node:
    def __init__(self, data: float, parent: object):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None


    def __repr__(self):
        return f"Node: {self.data}"
