# from data_structures.linked_list.linked_list import Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.max = 10000
        self.top = None

    def push(self,*value):
        '''
        used to add nodes to top of the stack:
            input --> value to create node from it then add to the top of the stack.
        '''
        for i in value:
            node= Node(i)
            temp = self.top
            self.top = node
            self.top.next = temp

    def pop(self):
        '''
        it only pop the first node in the top of the stack..
        '''
        try:
            poped = self.top.value
            temp = self.top.next 
            self.top = temp
            return poped
        except AttributeError as e:
            return "Stack is empty"

    def peek(self):
        '''
        return the first node value of the top of the stack:
            output -- the top value of the stack
        '''
        try:
            return self.top.value
        except AttributeError as e:
            return "Stack is empty"

    def is_empty(self):
        '''
        cheak if the stack is empty or not:
            output -- boleen
        '''
        if self.top:
            return False
        else:
            return True

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, *value):
        '''
        used to add nodes to rear of the queue:
            input --> value to create node from it then add to the queue..
        '''
        for i in value:
            node = Node(i)
            if not self.front and not self.rear:
                self.front = node
                self.rear = node

            old_rear = self.rear
            self.rear = node
            old_rear.next = self.rear


    def dequeue(self):
        '''
        it only pop the first node in the front of the queue.
        '''
        try:
            self.front.value
        except AttributeError:
            return "Queue Is Empty"
        else:
            temp = self.front
            tempp = temp.next
            self.front = tempp
            return temp.value


    def peek(self):
        '''
        return the first node value of the front of the queue:
            output -- the front value of the queue
        '''
        try:
            return self.front.value
        except AttributeError as e:
            return f"Empty Queue!!!\nDevs Details: {e}"
        except Exception as e:
            return f"Some other exception happened!!! {e}"

    def is_empty(self):
        '''
        cheak if the queue is empty or not:
            output -- boleen
        '''
        if self.front:
            return False
        else:
            return True


if __name__ == "__main__":
    # letters = Stack()
    # letters.push('A','B','C')
    # letters.push('B')
    # letters.push('C')
    # print(letters.pop())
    # print(letters.peek())

    numbers = Queue()
    numbers.enqueue(4,2,2,3)
    # numbers.enqueue(2)
    # numbers.enqueue(3)
    # print(numbers.peek())
    # print(numbers.dequeue())
    print(numbers.peek())