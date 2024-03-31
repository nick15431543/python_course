import copy

class MatrixHash():
    def __hash__(self):
        """
        return sum of int(matrix[i][j])
        """
        res = 0
        for i in self.matrix:
            for j in i:
                res += int(j)
        return res

class StrMixin():
    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                s += str(self.matrix[i][j])
                s += ' '
            s += '\n'
        return s

class WriteToFile():
    def write_to_file(self, file):
        with open(file, 'w') as f:
            f.write(str(self))

class MyMatrix(MatrixHash, StrMixin, WriteToFile):
    def __init__(self, l=None):
        if l is None:
            self.matrix = [[]]
        else:
            mat = []
            for i in l:
                t = []
                for j in i:
                    t.append(j)
                mat.append(t)
            self.matrix = mat
    
    def shape(self):
        return (len(self.matrix), len(self.matrix[0]))


    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError
        res = copy.deepcopy(self.matrix)
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] += other.matrix[i][j]
        return MyMatrix(res)
    
    def __sub__(self, other):
        if self.shape() != other.shape():
            raise ValueError
        res = copy.deepcopy(self.matrix)
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] -= other.matrix[i][j]
        return MyMatrix(res)
    
    def __mul__(self, other):
        if self.shape() != other.shape():
            raise ValueError
        res = copy.deepcopy(self.matrix)
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] *= other.matrix[i][j]
        return MyMatrix(res)
    
    def __matmul__(self, other):
        if self.shape()[1] != other.shape()[0]:
            raise ValueError
        res = [[0] * other.shape()[1] for _ in range(self.shape()[0])]
        for i in range(self.shape()[0]):
            for j in range(other.shape()[1]):
                for k in range(self.shape()[1]):
                    res[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return MyMatrix(res)