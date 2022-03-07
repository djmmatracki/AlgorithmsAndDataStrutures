import unittest
from main import Matrix

def assertMatrix(first, second):
    rows, cols = first.size()

    for i in range(rows):
        for j in range(cols):
            if first[i][j] != second[i][j]:
                return False
    return True


class TestMatrix(unittest.TestCase):
    
    def setUp(self) -> None:
        self.matrix = [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]]
        

    def test_init(self):
        myMat = Matrix(matrix=self.matrix)
        self.assertEqual(myMat[0], [1, 2, 3])

    def test_str(self):
        res = "1 2 3 \n1 2 3 \n1 2 3 \n"
        myMat = Matrix(matrix=self.matrix)
        self.assertEqual(str(myMat), res)

    def test_add(self):
        res = Matrix(matrix=self.matrix) + Matrix(matrix=self.matrix)
        self.assertTrue(assertMatrix(res, [[2, 4, 6], [2, 4, 6], [2, 4, 6]]))

    def test_mul(self):
        res = Matrix(matrix=self.matrix) * Matrix(matrix=self.matrix)
        self.assertTrue(assertMatrix(res, [[6, 12, 18], [6, 12, 18], [6, 12, 18]]))


if __name__ == "__main__":
    unittest.main()