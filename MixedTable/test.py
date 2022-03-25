import unittest
from solution import MixedTable


class TestMixedTable(unittest.TestCase):

    def setUp(self) -> None:
        self.table = MixedTable(size=13)

    def test_insert(self):
        self.table.insert(("a", 1))

        for i in range(1, 16):
            if i == 6:
                self.table.insert((18, chr(64+i)))
            elif i == 7:
                self.table.insert((31, chr(64+i)))
            else:
                self.table.insert((i, chr(64+i)))
        print(self.table)
        print(self.table.get(5))
        print(self.table.get(14))
        self.table.insert((5, 'Z'))
        self.table.remove(5)
        print(self.table)
        print(self.table.get(31))
        self.table.insert(('W', 'test'))


if __name__ == "__main__":
    unittest.main()