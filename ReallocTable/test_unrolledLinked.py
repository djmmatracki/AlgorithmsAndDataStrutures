import unittest
from extraSolution import UnrolledLinkedList


class TestQueue(unittest.TestCase):
    def test_1(self) -> None:
        self.queue = UnrolledLinkedList()
        self.queue.insert(0, 1)
        self.queue.insert(0, 1)
        self.queue.insert(0, 1)
        self.queue.insert(0, 1)
        self.queue.insert(0, 1)
        self.queue.insert(0, 1)
        self.queue.insert(0, 2)
        self.queue.insert(0, 4)
        self.queue.insert(0, 3)
        self.queue.printList()


if __name__ == "__main__":
    unittest.main()