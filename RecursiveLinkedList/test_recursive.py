import unittest
from recursiveLinked import length, addToEnd, removeFromEnd, take, drop
from main import LinkedList


class RecursiveLinkedTest(unittest.TestCase):
    
    def setUp(self):
        self.linked = LinkedList()
        self.linked.addToEnd(1)
        self.linked.addToEnd(2)
        self.linked.addToEnd(3)
        self.linked.addToEnd(4)
        self.linked.addToEnd(5)
        self.linked.addToEnd(6)

    def test_length(self):
        self.assertEqual(length(self.linked.head), 6)
    
    def test_addToEnd(self):
        addToEnd(self.linked.head, 6)
        self.assertEqual(length(self.linked.head), 7)
    
    def test_removeFromEnd(self):
        addToEnd(self.linked.head, 6)
        removeFromEnd(self.linked.head)
        self.assertEqual(length(self.linked.head), 6)
    
    def test_take(self):
        l = take(self.linked.head, 3)
    
    def test_drop(self):
        l = drop(self.linked.head, 3)
        l.printList()


if __name__ == "__main__":
    unittest.main()