import numpy as np

from my_matrix_with_mixins import MyMatrix


np.random.seed(0)
m1 = MyMatrix(np.random.randint(0, 10, (10, 10)))
m2 = MyMatrix(np.random.randint(0, 10, (10, 10)))
(m1 + m2).write_to_file('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.2/matrix+.txt')
(m1 * m2).write_to_file('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.2/matrix*.txt')
(m1 @ m2).write_to_file('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.2/matrix@.txt')