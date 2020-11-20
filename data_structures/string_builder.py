class StringBuilder:
    def __init__(self):
        self.arr = []

    def append(self, value):
        self.arr.append(value)

    def build(self):
        "".join(self.arr)