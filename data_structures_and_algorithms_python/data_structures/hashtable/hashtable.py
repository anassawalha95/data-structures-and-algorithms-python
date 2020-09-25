class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def add(self,value):
        """
        Method to add to the linked-list
        """
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            current = self.head

            while current.next:
                 current= current.next

            current.next = node

class HashTable:

    def __init__(self,size=1024):
        self.map = [None]*size
        self.size = size

    def hash(self,key):
        """
        takes in an arbitrary key and returns an index in the collection.
        """
        hashed_total = 0

        for char in key:
            hashed_total += ord(char)

        return hashed_total * 19 % self.size

    def set(self,key,value):
        """
        takes in both the key and value.
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        """
        hash_key = self.hash(key)

        if self.map[hash_key] == None:
            self.map[hash_key] = LinkedList()
            self.map[hash_key].add((key,value))

        #here
        else:
            current = self.map[hash_key].head
            while current:
                if current.value[0] == key:
                    # temp = current.next
                    current.value =None
                    current.value = (key,value)
                    # new = list(current.value)
                    # new[1] = value
                    # current.value = tuple(new)
                    # break
                    # current.value[1] = value
                elif current.next == None:
                    self.map[hash_key].add((key,value))
                current = current.next

    def get(self,key):
        """
        takes in the key and returns the value from the table.
        """
        hash_key = self.hash(key)

        if self.map[hash_key] == None:
            return None
        else:
            current = self.map[hash_key].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def contain(self,key):
        """
        takes in the key and returns a boolean, indicating if the key exists in the table already.
        """
        hash_key = self.hash(key)

        if self.map[hash_key] == None:
            return False
        else:
            current = self.map[hash_key].head
            boolean_result = False
            while current:
                if current.value[0] == key:
                    boolean_result =  True
                current = current.next
        return boolean_result

if __name__ == "__main__":
    table = HashTable()
    table.set('listen','listen value')
    # table.set('silent','silent value')
    # print(table.hash('listen'))
    
    print(table.map[table.hash('listen')].head.value)
    # print(table.map[table.hash('silent')].head.next.value)

    # print(table.get('listen'))
    x = table.get('listen')
    print(x)
    # print(table.get('silent'))
    # print(table.get('aziz'))

    # table.get('listen')

    # print(table.contain('listen'))
    # print(table.contain('silent'))
    # print(table.contain('aziz'))

    # table.set('listen','listen value 2')
    # print(table.map[table.hash('listen')].head.value)

    # table.set('silent','silent value')
    # print(table.map[table.hash('silent')].head.next.value)