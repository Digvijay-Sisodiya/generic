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