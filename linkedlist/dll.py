from node import DoubleNode as Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, data) -> None:

        if not self.head:
            self.head = Node(data)
            self.tail = self.head
            return

        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    
    def insert_end(self, data) -> Node:

        if not self.head:
            self.head = Node(data)
            self.tail = self.head
            return
        
        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def traverse(self):
        print(self.head.__str__())
    
    def search(self, data) -> Node:

        current_node = self.head

        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

    
    def delete(self, data):

        if self.tail.data == data:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return

        if self.head.data == data:
            self.head.next.prev = None
            self.head = self.head.next
            return

        current_node = self.head

        while current_node:
            if current_node.data == data:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                del current_node
                return

            current_node = current_node.next

    def __str__(self) -> str:
        return self.head.__str__()



if __name__ == "__main__":
    dl = DoublyLinkedList()

    for i in range(5, 0, -1):
        dl.insert(i)
    for i in range(6, 11):
        dl.insert_end(i)

    dl.traverse()

