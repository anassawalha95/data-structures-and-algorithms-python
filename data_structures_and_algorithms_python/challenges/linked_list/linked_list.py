class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        value !=None
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curent = self.head
            while curent.next:
                curent = curent.next
            curent.next = new_node
    # I created show method to show the elemnts in the linkedlist as a list
    def show(self):
        elms =[]
        curent=self.head
        while curent:
            elms.append(curent.value)
            curent = curent.next
        print(elms)

    def includes(self,num):
        curent = self.head
        self.num = num
        while curent:
            if curent.value == num:
                return True
            curent=curent.next
        return False


    def __str__(self):
        curent = self.head
        output = ''
        while curent:
            output+=f"{{ {curent.value} }} -> "
            curent = curent.next
        output += 'NULL'
        return output

my_list = Linkedlist()
try:
    print(my_list)
    my_list.insert(0)
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    my_list.insert(4)

    my_list.show()
    print(my_list.includes(4))
    print(my_list.__str__())

    my_list2 = Linkedlist()
    print(my_list2)

    my_list2.insert('A')
    my_list2.insert('B')
    my_list2.insert('C')

    my_list2.show()
    print(my_list2.includes('D'))
    print(my_list2.__str__())
except:
    print('Value error make sure from the values that you are enterd')


