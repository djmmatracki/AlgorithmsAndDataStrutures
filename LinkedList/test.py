import unittest
from main import LinkedList


class LinkedListTests(unittest.TestCase):
    
    def setUp(self):
        self.linked = LinkedList()
        self.linked.addToEnd(1)
        self.linked.addToEnd(2)
        self.linked.addToEnd(3)
        self.linked.addToEnd(4)
        self.linked.addToEnd(5)
        self.linked.addToEnd(6)

    def test_create(self):
        linked = LinkedList()
        self.assertEqual(linked.head, None)
    
    def test_loadList(self):
        self.assertEqual(self.linked.toList(), [1, 2, 3, 4, 5, 6])
    
    def test_destroy(self):
        self.linked.destroy()
        self.assertEqual(self.linked.head, None)
    
    def test_add(self):
        self.linked.add(6)
        self.assertEqual(self.linked.toList(), [6, 1, 2, 3, 4, 5, 6])
    
    def test_remove(self):
        self.linked.remove()
        self.assertEqual(self.linked.toList(), [2, 3, 4, 5, 6])
    
    def test_isEmpty(self):
        linked = LinkedList()
        self.assertFalse(self.linked.is_empty())
        self.assertTrue(linked.is_empty())
    
    def test_length(self):
        self.assertEqual(self.linked.length(), 6)

    def test_get(self):
        self.assertEqual(self.linked.get(), 1)
    
    def test_take(self):
        newList = self.linked.take(3)
        self.assertEqual(newList.toList(), [1, 2, 3])

    def test_drop(self):
        newList = self.linked.drop(3)
        self.assertEqual(newList.toList(), [4, 5, 6])


if __name__ == "__main__":
    unittest.main()