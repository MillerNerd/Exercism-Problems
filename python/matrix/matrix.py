import numpy as np


class Matrix:
    def __init__(self, matrix_string):
        self.arr2d = []
        self.arr1d = matrix_string.split('\n')
        for i in range(len(self.arr1d)):
            self.arr2d.append(list(map(int, self.arr1d[i].split())))

    def row(self, index):
        return self.arr2d[index-1]

    def column(self, index):
        return [i[index-1] for i in self.arr2d]
