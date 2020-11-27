class Stack:
    def __init__(self):
        self.tail = None

    def pop(self):
        if not self.tail:
            raise ValueError

        current = self.tail
        self.tail = current.Next
        return current.data

    def peek(self):
        return self.tail.data

    def push(self, data):
        node = Node(data)
        if not self.tail:
            self.tail = node
        else:
            node.Next = self.tail
            self.tail = node

    def is_empty(self):
        return not self.tail

class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None


def test_is_not_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)

    assert not stack.is_empty()

def test_is_empty():
    stack = Stack()
    stack.push(1)
    stack.push(3)

    stack.pop()
    stack.pop()

    assert stack.is_empty()

def test_peek():
    stack = Stack()
    stack.push(4)

    assert stack.peek() == 4
    assert not stack.is_empty()

def test_pop():
    stack = Stack()
    stack.push(4)

    assert stack.pop() == 4
    assert stack.is_empty()
