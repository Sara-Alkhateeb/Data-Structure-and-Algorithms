import pytest
from s_q_pseudo.s_q_pseudo import PseudoQueue


def test_enqueue():
    q = PseudoQueue()
    q.enqueue(20)
    q.enqueue(15)
    q.enqueue(10)
    q.enqueue(5)
    assert str(q) == "[5]->[10]->[15]->[20]->None"


def test_dequeue():
    q = PseudoQueue()
    q.enqueue(20)
    q.enqueue(15)
    q.enqueue(10)
    q.enqueue(5)
    assert str(q) == "[5]->[10]->[15]->[20]->None"

def test_dequeue_value():
    q = PseudoQueue()
    q.enqueue(20)
    q.enqueue(15)
    q.enqueue(10)
    assert q.dequeue() == 20

def test_dequeue_empty_queue():
    q = PseudoQueue()
    assert q.dequeue() == "Pseudo Queue is empty"





