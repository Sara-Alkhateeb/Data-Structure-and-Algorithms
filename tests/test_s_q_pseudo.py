import pytest
import unittest
from s_q_pseudo.s_q_pseudo import PseudoQueue

class TestPseudoQueue(unittest.TestCase):
    def setUp(self):
        self.queue = PseudoQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(str(self.queue), "[1]")

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        # self.queue.enqueue(3)
        self.queue.dequeue()
        # self.assertEqual(value, 1)
        self.assertEqual(str(self.queue), "[1]")

    def test_dequeue_empty_queue(self):
        with self.assertRaises(Exception):
            self.queue.dequeue()

if __name__ == '__main__':
    unittest.main()



