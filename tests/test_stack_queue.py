import pytest
from stack_and_queue.stack_and_queue import Stack, Queue

#Stack Tests:

def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.top.value == 1

def test_stack_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top.value == 2

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1

def test_stack_empty_after_pops():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True

def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2

def test_stack_instantiate_empty():
    stack = Stack()
    assert stack.is_empty() == True

def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(Exception):
     stack.pop()

def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(Exception):
     stack.peek()

#Queue Tests:

def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front.value == 1

def test_queue_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front.value == 1

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1

def test_queue_empty_after_dequeues():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True

def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1

def test_queue_instantiate_empty():
    queue = Queue()
    assert queue.is_empty() == True

def test_queue_dequeue_empty():
    queue = Queue()
    with pytest.raises(Exception):
     queue.dequeue()

def test_queue_peek_empty():
    queue = Queue()
    with pytest.raises(Exception):
     queue.peek()