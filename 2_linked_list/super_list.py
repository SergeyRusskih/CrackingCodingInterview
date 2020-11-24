class SuperList:
    def __eq__(self, other):
        self_head = self.head
        other_head = other.head
        while self_head != None and other_head != None:
            if self_head.data != other_head.data:
                return False
            self_head = self_head.next
            other_head = other_head.next
        if self_head == None and other_head == None:
            return True
        return False