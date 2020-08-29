import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.data_structures.stacks_and_queues.stacks_and_queues import Stack, Queue

# #****Staks_tests****

def test_push():
    nums = Stack()
    nums.push(1)
    expected = nums.top.value
    assert expected == 1

def test_push_muliple():
    nums = Stack()
    nums.push(5,6,10)
    expected = nums.top.value
    assert expected == 10

def test_pop():
    nums = Stack()
    nums.push(1)
    nums.push(2)
    nums.push(3)
    expected = nums.pop()
    assert expected == 3

def test_empty_S():
    nums = Stack()
    nums.push(1)
    nums.push(2)
    nums.push(3)
    nums.pop()
    nums.pop()
    nums.pop()
    expected = True
    assert expected == nums.is_empty()

def test_peek_S():
    nums = Stack()
    nums.push(1)
    nums.push(2)
    expected = 2
    assert expected == nums.peek()

def test_exception_S():
    nums = Stack()
    expected = "Stack is empty"
    assert expected == nums.pop()

# #****Queues_tests****

def test_enqueue():
    letters = Queue()
    letters.enqueue('A')
    letters.enqueue('B')
    letters.enqueue('C')
    expected = 'A'
    assert expected == letters.front.value

def test_enqueue_muliple():
    letters = Queue()
    letters.enqueue('w','x','y','z')
    expected = 'w'
    assert expected == letters.peek()

def test_dequeue():
    letters = Queue()
    letters.enqueue('A')
    letters.enqueue('B')
    letters.enqueue('C')
    expected = 'A'
    actual = letters.dequeue()
    assert expected == actual

def test_peek_Q():
    letters = Queue()
    letters.enqueue('A')
    letters.enqueue('B')
    letters.enqueue('C')
    expected = 'A'
    actual = letters.peek()
    assert expected == actual

def test_empty_Q():
    letters = Queue()
    letters.enqueue('A')
    letters.enqueue('B')
    letters.enqueue('C')
    letters.dequeue()
    letters.dequeue()
    letters.dequeue()
    expected = True
    assert expected == letters.is_empty()

def test_exception_Q():
    letters = Queue()
    expected = "Queue Is Empty"
    assert expected == letters.dequeue()