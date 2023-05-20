import numpy as np

def matrix_multiply(matrix1, matrix2):
    """
    - Python code for matrix multiplication using nested loops
    - Time Complexity : O(n^3), where n refers to the size of the matrices being multiplied.
    """
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Number of columns in matrix1 must be equal to the number of rows in matrix2.")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def matrix_multiply_using_numpy():
    return np.dot(matrix1, matrix2)


# matrix1 = [[1, 2, 3],
#            [4, 5, 6]]
# matrix2 = [[7, 8],
#            [9, 10],
#            [11, 12]]
# result = matrix_multiply(matrix1, matrix2)
# print(result)
# res = matrix_multiply_using_numpy(matrix1, matrix2)
# print(result)
