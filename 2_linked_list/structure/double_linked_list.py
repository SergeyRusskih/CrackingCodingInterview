from .node import Node

class DoubleLinkedList:


    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def add(self, data):
        next = self.head
        while next.next:
            next = next.next

        next.next = Node(data)
        next.next.prev = next
        self.head = next.next
        self.size += 1


def test_add():
    linked_list = DoubleLinkedList(1)
    linked_list.add(2)
    linked_list.add(3)
    assert linked_list.size == 3
