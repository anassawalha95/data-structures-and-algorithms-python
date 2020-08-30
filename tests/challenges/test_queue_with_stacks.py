import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_enqueue():
    nums = PseudoQueue()
    nums.enqueue(20)
    nums.enqueue(15)
    nums.enqueue(10)
    nums.enqueue(5)
    expected = ' -> { 5 } -> { 10 } -> { 15 } -> { 20 }'
    actual = nums.__str__()
    assert expected == actual


def test_dequeue():
    nums = PseudoQueue()
    nums.enqueue(20)
    nums.enqueue(15)
    nums.enqueue(10)
    nums.enqueue(5)
    expected = 20
    assert expected == nums.dequeue()

def test_dequeue_2():
    nums = PseudoQueue()
    nums.enqueue(15)
    nums.enqueue(10)
    nums.enqueue(5)
    expected = 15
    assert expected == nums.dequeue()