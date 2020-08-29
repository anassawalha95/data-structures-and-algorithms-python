# from data_structures_and_algorithms_python.data_structures.linked_list.linked_list import Linkedlist, Node
from data_structures_and_algorithms_python.data_structures.linked_list.linked_list import Linkedlist
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
#     llist = LinkedList() 
#     llist1 = LinkedList() 
#     llist2 = LinkedList() 
#     llist1.append(3) 
#     llist1.append(2) 
#     llist1.append(1) 
#     llist2.append(8) 
#     llist2.append(7) 
#     llist2.append(6)
#     llist.zip_lists(llist1,llist2)
#     print(llist.__str__())

def zip_lists(ll1,ll2):
    if not ll1:
        return ll2
    if not ll2:
        return ll1

    output = Linkedlist()
    current1 = ll1.head
    current2 = ll2.head

    while current1:
        output.append(current1.value)
        if current2:
            output.append(current2.value)
            current2 = current2.next
        current1 = current1.next

    while current2:
        output.append(current2.value)
        current2 = current2.next

if __name__ == "__main__":
    ll1 = Linkedlist()
    ll1.append(1)
    ll1.append(3)
    ll1.append(2)
    ll2 = Linkedlist()
    ll2.append(1)
    ll2.append(3)
    ll2.append(2)
    zip_lists(ll1,ll2)

