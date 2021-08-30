class Node:
    def __init__(self, data: float, parent: object):
        self.data = data
        self.leftChild: Node = None
        self.rightChild: Node = None
        self.parent: Node = None


    def __repr__(self):
        return f"Node: {self.data}"
