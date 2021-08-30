class Node:
    def __init__(self, data: float, parent):
        self.data = data
        self.leftChild: Node = None
        self.rightChild: Node = None
        self.parent: Node = parent


    def __repr__(self):
        return f"Node: {self.data}"
