from node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_node(self, node: Node, value: float) -> Node:
        if not node:
            return Node(value)

        if value < node.value:
            node.leftChild = self._insert_node(node.leftChild, value)
        else:
            node.rightChild = self._insert_node(node.rightChild, value)

        return node

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
        print(node.value)
        self._inorder(node.rightChild)

    def insert(self, value):
        if self.root:
            self._insert_node(self.root, value)
        else:
            self.root = Node(value)

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
    bst = BinarySearchTree()
    values = [17, 12, 19, 9, 10, 15, 25, 17, 7]

    for value in values:
        BST.insert(value)

    BST.traverse()
    print(BST.search(10))
