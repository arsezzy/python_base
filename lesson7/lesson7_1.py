#!/usr/bin/python3

import re


class Matrix():

    def __init__(self, *args):
        self.matrix_str, = args

    def __add__(self, other):
        new_matrix_list = []
        for row_m1, row_m2 in zip(self.matrix_str, other.matrix_str):
            new_matrix_list.append(list(map(sum, zip(row_m1, row_m2))))
        return Matrix(new_matrix_list)

    def __str__(self):
        self.as_text = ""
        for el in self.matrix_str:
            self.as_text += str(el) + "\n"
        return re.sub(r"[][]", "", self.as_text)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(f"matrix1 is")
print(m1)
m2 = Matrix([[11, 12, 13], [14, 15, 16]])
print(f"matrix2 is")
print(m2)
print(f"Sum of matrix1 and matrix2 is ")
print(m1 + m2)

