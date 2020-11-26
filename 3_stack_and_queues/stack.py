class Stack:
    def __init__(self):
        self.arr = []

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[len(self.arr)-1]

    def push(self, data):
        self.arr.append(data)

    def isEmpty(self):
        return len(self.arr) == 0