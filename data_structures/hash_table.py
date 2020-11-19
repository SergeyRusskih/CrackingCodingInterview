class HashTable:

    def __init__(self):
        self.arr_size = 10
        self.arr = [0] * self.arr_size
        for i in range(len(self.arr)):
            self.arr[i] = []

    def add(self, value):
        self.arr[self.get_position(value)].append(value)

    def find(self, value):
        values = self.arr[self.get_position(value)]
        for item in values:
            if item == value:
                return item

        raise ValueError

    def get_position(self, value):
        return hash(value) // self.arr_size

