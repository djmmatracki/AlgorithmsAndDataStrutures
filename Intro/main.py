from typing import Optional, Type, List, Tuple


class Matrix:
    def __init__(self, matrix, value: int=0) -> None:

        if isinstance(matrix, list):
            self._matrix = matrix
            return
        
        if isinstance(matrix, tuple) and len(matrix) == 2:
            rows, cols = matrix
            self._matrix = [[value for _ in range(cols)] for _ in range(rows)]
            return

        raise ValueError("Wrong initialization!")


    def __add__(self, other):
        # Adds two matrices and returns a new one
        if self.size() != other.size():
            raise ValueError("Wrong matrix size")

        rows, cols = self.size()
        return Matrix([[self._matrix[j][i] + other[j][i] for i in range(cols)] for j in range(rows)])

    def __mul__(self, other):
        # Multiply matrices
        rows1, cols1 = self.size()
        rows2, cols2 = other.size()

        if rows1 != cols2 or rows2 != cols1:
            raise ValueError("Wrong number of rows and cols.")

        result = [[0 for _ in range(rows1)] for _ in range(cols2)]

        for j in range(rows1):
            for i in range(cols1):
                rowSum = 0
                for k in range(rows1):
                    rowSum += self._matrix[i][k] * other[k][i]
                result[j][i] = rowSum
        return Matrix(result)
            

    def __getitem__(self, index):
        # Get row
        return self._matrix[index]


    def __str__(self) -> str:
        # Return string matrix
        cols, rows = self.size()
        stringRep = ""

        for i in range(cols):
            for j in range(rows):
                stringRep += f"{self._matrix[i][j]} "
            stringRep += "\n"

        return stringRep

    def size(self) -> tuple:
        return len(self._matrix), len(self._matrix[0])



def transponse(matrix):
    rows, cols = matrix.size()
    return Matrix([[matrix[i][j] for i in range(cols)] for j in range(rows)])
