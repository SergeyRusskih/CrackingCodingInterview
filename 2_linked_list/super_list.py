class SuperList:
    def __eq__(self, other):
        self_next = self.tail
        other_next = other.tail
        while self_next != None and other_next != None:
            if self_next.data != other_next.data:
                return False
            self_next = self_next.next
            other_next = other_next.next
        if self_next == None and other_next == None:
            return True
        return False