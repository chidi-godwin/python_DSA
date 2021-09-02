from .node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _delete_node(self, node: Node, data):

        if not node:
            return
        
        if data < node.data:
            self.delete(node.leftChild, data)
        elif data > node.data:
            self.delete(node.rightChild, data)
        else:
            if not node.rightChild and not node.leftChild:
                print(f"Removing leaf node......{node.data}")

                parent = node.parent

                if parent:
                    if node == parent.leftChild:
                        parent.leftChild = None
                    elif node == parent.rightChild:
                        parent.rightChild = None
                else:
                    self.root = None
                
                del node
            elif node.rightChild and not node.leftChild:
                print(f"Removing node with  single right child")
                parent = node.parent

                if parent:
                    parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild

                del node
            elif node.leftChild and not node.rightChild:
                print(f"Removing node with  single left child")
                parent = node.parent

                if parent:
                    parent.leftChild = node.leftChild
                else:
                    self.root = node.leftChild

                del node
            else:
                print("Removing node two children")
                predecessor = self._get_max_value(node.leftChild)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                parent = predecessor.parent
                parent.rightChild = None

                del predecessor


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

    def _search_node(self, node: Node, data: float):
        if not node:
            return

        if node.data == data:
            return node

        if data < node.data:
            return self._search_node(node.leftChild, data)
        else:
            return self._search_node(node.rightChild, data)

    def _inorder(self, node: Node):

        if not node:
            return

        self._inorder(node.leftChild)
        print(node.data)
        self._inorder(node.rightChild)

    def _get_max_value(self, node: Node) -> Node:

        if not node.rightChild:
            return node
    
        return self._get_max_value(node.rightChild)

    def _get_min_value(self, node: Node) -> Node:

        if not node.leftChild:
            return node
        
        return self._get_min_value(node.leftChild)


    def get_max(self) -> float:
        if self.root:
            return self._get_max_value(self.root)
        return

    def get_min(self) -> float:

        if self.root:
            return self._get_min_value(self.root)
        
        return None

    def delete(self, data):
        if not self.root:
            return
        self._delete_node(self.root, data)

    def insert(self, data):
        if self.root:
            self._insert_node(self.root, data)
        else:
            self.root = Node(data, None)

    def search(self, data):
        if self.root:
            return self._search_node(self.root, data)
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
    values = [17, 12, 19, 9, 10, 15, 25, 7,  8]

    for value in values:
        BST.insert(value)

    BST.traverse()
    print("max:", BST.get_max())
    print('min:', BST.get_min())
    BST.delete(17)
