class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"""{self.data} -> {self.next}"""

class DoubleNode(Node):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.prev = None

    def __str__(self) -> str:
        return f"{self.data} <--> {self.next}"


if __name__ == "__main__":
    node = Node(3)
    node.next = Node(4)
    node.next.next = Node(5)
    node.next.next.next = Node(6)

    print(node)