
def det2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def choMethod(matrix):
    n = len(matrix)

    if n == 2:
        return det2x2(matrix)
    
    nMatrix = [[0 for _ in range(n-1)] for _ in range(n-1)]
    for i in range(n-1):
        for j in range(n-1):
            nMatrix[i][j] = matrix[0][0] * matrix[i+1][j+1] - matrix[0][j+1] * matrix[i+1][0]

    return choMethod(nMatrix) / (matrix[0][0]**(n-2))

m = [
    [5, 1, 1, 2, 3],
    [4, 2, 1, 7, 3],
    [2, 1, 2, 4, 7],
    [9, 1, 0, 7, 0],
    [1, 4, 7, 2, 2]
]

print(choMethod(m))