from my_matrix import MyMatrix
import numpy as np

a = MyMatrix([[1, 2], [1, 2]])
b = d = MyMatrix([[3, 4], [3, 4]])
c = MyMatrix([[1.5, 2], [1, 2]])

(a@b).write_to_file('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.3/AB.txt')
(c@d).write_to_file('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.3/CD.txt')
with open('/Users/nikitakocherin/workspace/python_course/hw_3/artifacts/3.3/hash.txt', 'w') as f:
    s = str(hash(a@b)) + ' ' + str(hash(c@d))
    f.write(s)

