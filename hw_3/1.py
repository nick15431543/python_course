from my_matrix import MyMatrix
import numpy as np
np.random.seed(0)
m1 = MyMatrix(np.random.randint(0, 10, (10, 10)))
m2 = MyMatrix(np.random.randint(0, 10, (10, 10)))
with open('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.1/matrix+.txt', 'w') as f:
    res = (m1 + m2).matrix
    for i in res:
        for j in i:
            f.write(str(j))
            f.write(' ')
        f.write('\n')
with open('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.1/matrix*.txt', 'w') as f:
    res = (m1 * m2).matrix
    for i in res:
        for j in i:
            f.write(str(j))
            f.write(' ')
        f.write('\n')
with open('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.1/matrix@.txt', 'w') as f:
    res = (m1 @ m2).matrix
    for i in res:
        for j in i:
            f.write(str(j))
            f.write(' ')
        f.write('\n')