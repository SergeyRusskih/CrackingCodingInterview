class AnimalShelter:

    def __init__(self):
        self.cats_tail = None
        self.cats_head = None
        self.dogs_tail = None
        self.dogs_head = None
        self.sequence = 0

    def enqueue(self, animal):
        animal.sequence = self.sequence
        if type(animal) is Cat:
            if not self.cats_head:
                self.cats_head = animal
                self.cats_tail = animal
            else:
                self.cats_head.next = animal
                self.cats_head = self.cats_head.next
        else:
            if not self.dogs_head:
                self.dogs_head = animal
                self.dogs_tail = animal
            else:
                self.dogs_head.next = animal
                self.dogs_head = self.cats_head.next

        self.sequence += 1
    
    def dequeueAny(self):
        if not self.cats_tail and not self.dogs_tail:
            raise ValueError
        elif not self.cats_tail:
            return self.dequeueDog()
        elif not self.dogs_tail:
            return self.dequeueCat()
        elif self.cats_tail.sequence > self.dogs_tail.sequence:
            self.dequeueDog()
        else:
            return self.dequeueCat()
      
    def dequeueCat(self):
        result = self.cats_tail
        self.cats_tail = self.cats_tail.next
        return result

    def dequeueDog(self):
        result = self.dogs_tail
        self.dogs_tail = self.dogs_tail.next
        return result

class Animal:
    def __init__(self):
        self.next = None
        self.sequence = None

class Cat(Animal):
    def __init__(self):
        super().__init__()

class Dog(Animal):
    def __init__(self):
        super().__init__()


def test_simple():
    shelter = AnimalShelter()
    shelter.enqueue(Cat())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())

    assert type(shelter.dequeueDog()) is Dog
    assert type(shelter.dequeueCat()) is Cat
    assert type(shelter.dequeueAny()) is Cat
    assert type(shelter.dequeueDog()) is Dog
    assert type(shelter.dequeueAny()) is Cat
