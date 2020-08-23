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

    def append(self,value):
        value !=None
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curent = self.head
            while curent.next:
                curent = curent.next
            curent.next = new_node

    def insert_before(self,value, new_val):
        new_val1 =Node(new_val)
        if self.head.value == value:
            new_val1.next = self.head
            self.head = new_val1
        else:
            curent = self.head
            while True:
                try:
                    curent.next.value
                except:
                    return 'Value Not Exist'
                else:
                    if curent.next.value == value:
                        old = curent.next
                        new_val1.next = old
                        curent.next = new_val1
                    else:
                        curent = curent.next
                        continue
                break



    def insert_after(self,value, new_val):
        new_val1 =Node(new_val)
        if self.head.value == value:
            new_val1.next = self.head.next
            self.head.next = new_val1
        else:
            curent = self.head
            while True:
                try:
                    curent.next.value
                except:
                    return print('Value Not Exist')
                else:
                    if curent.next.value == value:
                        curent = curent.next
                        old = curent.next
                        new_val1.next = old
                        curent.next = new_val1
                    else:
                        curent = curent.next
                        continue
                break
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

print(my_list)
my_list.insert(0)
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
print(my_list.insert_before(3,5))
print(my_list.__str__())
my_list.insert_after(3,5)
print(my_list.__str__())



