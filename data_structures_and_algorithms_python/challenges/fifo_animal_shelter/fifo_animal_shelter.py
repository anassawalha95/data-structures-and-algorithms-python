import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.data_structures.stacks_and_queues.stacks_and_queues import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Dog:
    type = 'dog'
    def __init__(self,name):
        self.name = name

class Cat:
    type = 'cat'
    def __init__(self,name):
        self.name = name    

class AnimalShelter:

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, obj):
        try:
            if obj.type == 'cat':
                self.cats.enqueue(obj)
            elif obj.type == 'dog':
                self.dogs.enqueue(obj)
        except AttributeError as e:
            return 'You Should Add Cat or Dog Only'

    def dequeue(self,pref):
        try:
            if pref == 'cat':
                cat = self.cats.dequeue()
                return cat.name
            elif pref == 'dog':
                dog = self.dogs.dequeue()
                return dog.name
        except AttributeError as e:
            return None



if __name__ == "__main__":
    alex = Dog('alex')
    aln = Dog('Aln')
    sam = Dog('Sam')
    cray = Dog('Cray')
    soso = Cat('Soso')
    sno = Cat('Son')
    animals = AnimalShelter()
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(sam)
    animals.enqueue(cray)
    animals.enqueue(soso)
    animals.enqueue(sno)
    print(animals.enqueue('aaa'))
    # animals.dequeue()
    print(animals.dequeue('cat'))
    # print(animals.__str__())