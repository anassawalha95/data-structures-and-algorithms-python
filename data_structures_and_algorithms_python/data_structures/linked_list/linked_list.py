class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        if value is None:
            raise Exception('Please insert vlaue as argument')
        else:
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                curent = self.head
                while curent.next:
                    curent = curent.next
                curent.next = new_node

    def append(self,value):
        """
        method to add the value to the end of the linkedlist
        """
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
        """
        method to add a new node with the given newValue immediately before the first value node
        """
    
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
        """
        Method to add a new node with the given newValue immediately after the first value node
        """
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
        if num is None:
            raise Exception('Please insert vlaue as argument')
        else:
            curent = self.head
            self.num = num
            while curent:
                if curent.value == num:
                    return True
                curent=curent.next
            return False

    def kth_from_end(self, k):
        """
        method for the Linked List class which takes a number, k, as a parameter. 
        Return the node’s value that is k from the end of the linked list
        """
        try:
            
            n = -1
            curr = self.head
            while curr:
                curr = curr.next
                n = n + 1
            if n >= k:
                curr = self.head
                for i in range(n - k):
                    curr = curr.next

            return curr.value
        except:
            return "The Value Nott Found"

    def __str__(self):
        curent = self.head
        output = ''
        while curent:
            output+=f"{{ {curent.value} }} -> "
            curent = curent.next
        output += 'NULL'
        return output

        
#**********************************************************************
def reverse_ls(list_one): 
    prev = None
    current = list_one.head
    lis=[]
    checklis=[]
    while(current is not None): 
        lis.append(current.value)
        next = current.next
        current.next = prev 
        prev = current 
        checklis.append(prev.value)
        current = next
    list_one.head = prev 
    print(lis)
    print(checklis)
    if lis==checklis:
        return True

list_one = Linkedlist()
list_one.append('m')
list_one.append('o')
list_one.append('o')
list_one.append('m')
list_one.insert(None)
print(reverse_ls(list_one))
# print(check_val())
# print(my_list)
# print(my_list.insert_before(3,5))
# print(my_list.__str__())
# my_list.insert_after(3,5)
# print(my_list.__str__())
# print(my_list.kth_from_end(1))        
