import unittest
from solution import Queue


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.enqueue(7)

    def test_isEmpty(self):
        for _ in range(7):
            self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_enqueue(self):
        self.assertEqual(self.queue.queue, [1, 2, 3, 4, 5, 6, 7, None, None, None])

    def test_dequeue(self):
        self.assertEqual(1, self.queue.dequeue())
        self.assertEqual(2, self.queue.dequeue())
        self.queue.enqueue(7)
        self.queue.enqueue(7)
        self.assertEqual(3, self.queue.dequeue())
        self.assertEqual(4, self.queue.dequeue())
        self.assertEqual(5, self.queue.dequeue())

if __name__ == "__main__":
    unittest.main()