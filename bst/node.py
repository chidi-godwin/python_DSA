class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parent = None


    def __repr__(self):
        return f"Node: {self.value}"
