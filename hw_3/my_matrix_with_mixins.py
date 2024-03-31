import numpy as np

import numbers

class StrMixin():
    def __str__(self):
        s = ''
        for i in range(len(self.value)):
            for j in range(len(self.value[0])):
                s += str(self.value[i][j])
                s += ' '
            s += '\n'
        return s

class WriteToFile():
    def write_to_file(self, file):
        with open(file, 'w') as f:
            f.write(str(self))


class MyMatrix(np.lib.mixins.NDArrayOperatorsMixin, StrMixin, WriteToFile):
    def __init__(self, value):
        self.value = value
        self._HANDLED_TYPES = (np.ndarray, numbers.Number, list)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(
                x, self._HANDLED_TYPES + (MyMatrix,)
            ):
                return NotImplemented
        inputs = tuple(x.value if isinstance(x, MyMatrix) else x
                    for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, MyMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
 
    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.value)
    
    @property
    def params(self):
        return self.value

    @params.setter
    def params(self, new_params):
        self.value = new_params