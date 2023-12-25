import numpy

import pandas as pd

def checking (matrix): # Проверка матрицы на правильность (на то, что она прямоугольная)

    columns_len = len (matrix [0]) # Высчитаываем длину строки матрицы

    for matr_str in matrix [1:]: # Проходимся по строкам матрицы
        if len (matr_str) != columns_len: # Если длина матрицы изменилась
            return False # Это - не матрица, поэтому возвращаем False
    
    return True # Если же ничего не было обнаружено, возвращаем True



def transposition_numpy (matrix):

    Matrix = numpy.array (matrix)
    return Matrix.transpose ()



def multiplying_numpy (martix_1, matrix_2):

    Matrix_1 = numpy.array (martix_1)
    Matrix_2 = numpy.array (matrix_2)

    return numpy.matmul (Matrix_1, Matrix_2)



def rank_numpy (matrix):

    Matrix = numpy.array (matrix)
    return numpy.linalg.matrix_rank (Matrix)



# Ввод с функциями


matrixes = [[1,4], [2, 5], [3, 5]]
print(transposition_numpy(matrixes))




my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)
