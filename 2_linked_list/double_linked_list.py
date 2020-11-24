from node import Node
from super_list import SuperList

class DoubleLinkedList(SuperList):
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

    def delete(self, data):
        if self.tail.data == data:
            self.tail = self.tail.next
            self.size -= 1
            return

        if self.head.data == data:
            self.head = self.head.prev
            self.head.next = None
            self.size -= 1
            return

        next = self.tail
        while next and next.data != data:
            next = next.next

        if next:
            next.prev.next = next.next
            next.next.prev = next.prev

def test_add():
    linked_list = DoubleLinkedList(1)
    linked_list.add(2)
    linked_list.add(3)
    assert linked_list.size == 3

def test_delete():
    linked_list = DoubleLinkedList(1)
    linked_list.add(2)
    linked_list.add(3)

    linked_list.delete(3)

    result = DoubleLinkedList(1)
    result.add(2)

    assert linked_list == result

def test_delete_1():
    linked_list = DoubleLinkedList(1)
    linked_list.add(2)
    linked_list.add(3)

    linked_list.delete(2)

    result = DoubleLinkedList(1)
    result.add(3)

    assert linked_list == result 

def test_delete_2():
    linked_list = DoubleLinkedList(1)
    linked_list.add(2)
    linked_list.add(3)

    linked_list.delete(1)

    result = DoubleLinkedList(2)
    result.add(3)

    assert linked_list == result
