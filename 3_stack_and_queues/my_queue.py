class MyQueue:
    def __init__(self):
        self.tail = None
        self.head = None

    def add(self, data):
        node = Node(data)
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            node.next = self.tail
            self.tail.prev = node
            self.tail = node

    def remove(self):
        if not self.head:
            raise ValueError
        data = self.head.data
        self.head = self.head.prev
        if self.head:
            self.head.next = None
        return data
        
    def is_empty(self):
        return not self.head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def test_is_empty():
    queue = MyQueue()
    queue.add(1)
    queue.remove()

    assert queue.is_empty()


def test_is_not_empty():
    queue = MyQueue()
    queue.add(1)

    assert not queue.is_empty()

def test_remove():
    queue = MyQueue()
    queue.add(1)
    queue.add(2)

    result = queue.remove()
    assert result == 1