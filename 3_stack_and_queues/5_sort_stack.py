from stack import Stack

class SortStack:
    def __init__(self):
        self.stack = Stack()
        self.tmp = Stack()

    def push(self, data):
        while not self.stack.is_empty():
            current = self.stack.pop()
            if current < data:
                self.tmp.push(current)
            else:
                self.stack.push(current)
                break

        self.stack.push(data)

        while not self.tmp.is_empty():
            current = self.tmp.pop()
            self.stack.push(current)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

def test_1():
    stack = SortStack()
    stack.push(3)
    stack.push(4)
    stack.push(1)
    stack.push(5)

    assert stack.pop() == 1
    assert stack.pop() == 3
    assert stack.pop() == 4
    assert stack.pop() == 5


