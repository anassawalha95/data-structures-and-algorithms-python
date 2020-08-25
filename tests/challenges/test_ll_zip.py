from data_structures_and_algorithms_python.data_structures.linked_list.linked_list import Node, Linkedlist
from data_structures_and_algorithms_python.challenges.ll_zip.ll_zip import zipLists

def test_zipLists1():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert llist.zipLists(llist1,llist2).__str__() =="<8 -><3 -><7 -><2 -><6 -><1 ->None"

def test_zipLists2():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
    llist1.append(0) 
    llist1.append(0) 
  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert llist.zipLists(llist1,llist2).__str__() =="<3 -><8 -><2 -><7 -><1 -><6 -><0 -><0 ->None"

def test_zipLists3():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 

  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    llist2.append(5) 
    llist2.append(5)
    assert llist.zipLists(llist1,llist2).__str__() =="<8 -><3 -><7 -><2 -><6 -><1 -><5 -><5 ->None"