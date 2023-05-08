import pytest
import unittest
from s_q_pseudo.s_q_pseudo import PseudoQueue

class TestPseudoQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = PseudoQueue()
        queue.enqueue(10)
        queue.enqueue(15)
        queue.enqueue(20)
        queue.enqueue(5)
        self.assertEqual(str(queue), "[5]->[10]->[15]->[20]")
        
        queue2 = PseudoQueue()
        queue2.enqueue(5)
        self.assertEqual(str(queue2), "[5]")

if __name__ == '__main__':
    unittest.main()


