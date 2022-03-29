import unittest
from extraSolution import UnrolledLinkedList


class TestQueue(unittest.TestCase):
    def test_1(self) -> None:
        self.queue = UnrolledLinkedList()
        for i in range(1, 10):
            self.queue.insert(i-1, i)

        print(self.queue.get(3))

        self.queue.printList()
        self.queue.insert(1, 10)
        self.queue.insert(8, 11)
        self.queue.printList()
        self.queue.remove(2)
        self.queue.printList()
        self.queue.remove(3)
        self.queue.printList()


if __name__ == "__main__":
    unittest.main()