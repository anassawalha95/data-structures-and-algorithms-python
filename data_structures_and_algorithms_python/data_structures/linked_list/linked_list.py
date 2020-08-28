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
        curent = self.head
        self.num = num
        while curent:
            if curent.value == num:
                return True
            curent=curent.next
        return False

    def kth_from_end(self, k):
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
print(reverse_ls(list_one))
# print(check_val())
# print(my_list)
# print(my_list.insert_before(3,5))
# print(my_list.__str__())
# my_list.insert_after(3,5)
# print(my_list.__str__())
# print(my_list.kth_from_end(1))



# def zip_lists(list1,list2):
#         """
#         akes two linked lists as arguments. Zip the two linked lists together into one so that
#         the nodes alternate between the two lists and return a reference to the head of the zipped list. 
#         """
#         try:
#             nodes_counter_li1 = 0
#             nodes_counter_li2 = 0
#             current = list1.head
#             while current != None:
#                 current = current.next
#                 nodes_counter_li1 = nodes_counter_li1 + 1 

#             current = list2.head
#             while current != None:
#                 current = current.next
#                 nodes_counter_li2 = nodes_counter_li2 + 1 

#             if nodes_counter_li1>nodes_counter_li2:
#                 curr = list1.head 
#                 list2_curr = list2.head 
#                 while curr != None and list2_curr != None: 
#                     list1_next = curr.next
#                     list2_next = list2_curr.next
        
#                     list2_curr.next = list1_next 
#                     curr.next = list2_curr 

#                     curr = list1_next 
#                     list2_curr = list2_next 

#                 list2.head = list2_curr 
#                 return list1
#             else:
#                 curr = list2.head 
#                 list1_curr = list1.head 
#                 while curr != None and list1_curr != None: 
#                     list2_next = curr.next
#                     list1_next = list1_curr.next
        
#                     list1_curr.next = list2_next 
#                     curr.next = list1_curr 

#                     curr = list2_next 
#                     list1_curr = list1_next 

#                 list1.head = list1_curr 
#                 return list2
#         except Exception as err:
#             print(f'error line 247 __str__ {err}')


# if __name__ == "__main__":
#     llist = Linkedlist() 
#     llist1 = Linkedlist() 
#     llist2 = Linkedlist() 
#     llist1.append(3) 
#     llist1.append(2) 
#     llist1.append(1) 
#     llist2.append(8) 
#     llist2.append(7) 
#     llist2.append(6)
    # zip_lists(llist1,llist2)
