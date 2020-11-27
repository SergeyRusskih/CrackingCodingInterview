from node import Node
from super_list import SuperList

class SinglyLinkedList(SuperList):
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def add_node(self, data):
        self.head.next = Node(data)
        self.head = self.head.next

    def delete_node(self, data):
        next = self.tail
        if next.data == data:
            self.tail = self.tail.next
            return

        while next and next.next and next.next.data != data:
            next = next.next
        
        if next.next:
            next.next = next.next.next

def test_delete_node():
    list1 = SinglyLinkedList(0)
    list1.add_node(1)
    list1.add_node(2)

    list2 = SinglyLinkedList(0)
    list2.add_node(2)

    list1.delete_node(1)

    assert list1.__eq__(list2)