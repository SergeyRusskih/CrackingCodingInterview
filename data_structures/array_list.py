class ArrayList():

    def __init__(self):
        self.arr = [0] * 10
        self.factor = 2
        self.index = 0

    def add(self, item):
        if self.index < len(self.arr):
            self.arr[self.index] = item
            self.index += 1
        else:
            new_arr = [0] * (len(self.arr) * self.factor)
            for i, item in enumerate(self.arr):
                new_arr[i] = item
            self.arr = new_arr