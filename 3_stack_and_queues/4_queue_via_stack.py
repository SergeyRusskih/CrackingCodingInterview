from stack import Stack

class QueueViaStack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def add(self, data):
        if not self.stack2.is_empty():
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())

        self.stack1.push(data)

    def remove(self):
        if not self.stack1.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())


        return self.stack2.pop()

    def is_empty(self):
        return self.stack2.is_empty() and self.stack1.is_empty()


def test_is_empty():
    queue = QueueViaStack()
    queue.add(1)
    queue.remove()

    assert queue.is_empty()

def test_is_not_empty():
    queue = QueueViaStack()
    queue.add(1)

    assert not queue.is_empty()

def test_remove():
    queue = QueueViaStack()
    queue.add(1)
    queue.add(2)

    result = queue.remove()
    assert result == 1