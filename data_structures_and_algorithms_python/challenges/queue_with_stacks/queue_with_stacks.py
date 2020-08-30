import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.data_structures.stacks_and_queues.stacks_and_queues import Stack

class PseudoQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
        self.count = 0
    

    def enqueue(self,value):
            self.count +=1
            self.in_stack.push(value)

    def dequeue(self):
        if self.out_stack.is_empty:
            while self.count>0:
                self.out_stack.push(self.in_stack.pop())
                self.count-=1
            poped = self.out_stack.pop() 
        return poped
    
    # I used this method to see the data and compare the output
    def __str__(self):
        output = ''
        cur =self.in_stack.top
        while cur:
            output+= f' -> {{ {cur.value} }}'
            cur = cur.next     
        return output

if __name__ == "__main__":
    nums = PseudoQueue()
    # nums.enqueue(1)
    nums.enqueue(20)
    nums.enqueue(15)
    nums.enqueue(10)
    nums.enqueue(5)
    print(nums.dequeue())
    # print(nums.__str__())
    # print(nums.enqueue(None))
    # print(nums.dequeue())
    # print(nums.stack1.top.value)
    # nums.__str__()


