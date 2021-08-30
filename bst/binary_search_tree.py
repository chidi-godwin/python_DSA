from node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_node(self, node: Node, data: float) -> Node:

        if data < node.data:
            if node.leftChild:
                self._insert_node(node.leftChild, data)
            else:
                node.leftChild = Node(data, node)
        else:
            if node.rightChild:
                self._insert_node(node.rightChild, data)
            else:
                node.rightChild = Node(data, node)

    def _search_node(self, node: Node, value: float):
        if not node:
            return

        if node.value == value:
            return node

        if value < node.value:
            return self._search_node(node.leftChild, value)
        else:
            return self._search_node(node.rightChild, value)

    def _inorder(self, node: Node):

        if not node:
            return

        self._inorder(node.leftChild)
        print(node.data)
        self._inorder(node.rightChild)

    def _get_max_value(self, node: Node) -> float:

        if not node.rightChild:
            return node.data
    
        return self._get_max_value(node.rightChild)

    def _get_min_value(self, node: Node):

        if not node.leftChild:
            return node.data
        
        return self._get_min_value(node.leftChild)

    def get_max(self) -> float:
        if self.root:
            return self._get_max_value(self.root)
        return None

    def get_min(self) -> float:

        if self.root:
            return self._get_min_value(self.root)
        
        return None

    def insert(self, value):
        if self.root:
            self._insert_node(self.root, value)
        else:
            self.root = Node(value, None)

    def search(self, value):
        if self.root:
            return self._search_node(self.root, value)
        raise Exception('List is empty')

    def traverse(self):
        if self.root:
            self._inorder(self.root)
        else:
            return "Empty"

    def __repr__(self):
        return f"root -> {self.root}"


if __name__ == "__main__":
    BST = BinarySearchTree()
    values = [17, 12, 19, 9, 10, 15, 25, 17, 7]

    for value in values:
        BST.insert(value)

    BST.traverse()
    print("max:", BST.get_max())
    print('min:', BST.get_min())

