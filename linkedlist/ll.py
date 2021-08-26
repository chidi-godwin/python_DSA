from .node import Node, DoubleNode

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data) -> None:

        if not self.head:
            self.head = Node(data)
            return
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def insert_end(self, data) -> None:
        
        if not self.head:
            self.head = Node(data)
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)

    
    def traverse(self):
        print(self.head.__str__())

    
    def search(self, data) -> Node:

        current_node = self.head

        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

    def delete(self, data):

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head.next
        previous_node = self.head

        while current_node:
            if current_node.data == data:
                previous_node.next = current_node.next

            previous_node = current_node
            current_node = current_node.next
    
    def __str__(self) -> str:
        return self.head.__str__()

