# Dictionary unpacking
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 30, 'd': 400}
print({**d1, **d2})
print('\n')


# Dictionary with ChainMap
from collections import ChainMap

merged = ChainMap(d1, d2)
print(merged)
print(merged['a'], merged['b'], merged['c'], merged['d'])
print('\n')



def func(**kwargs):
    for item in kwargs.items():
        print(item)

func(b = 100, a = 200, y = 'hello', p = 'python')

from collections import namedtuple

def defaulted_namedtuple(class_name, **fields):
    Struct = namedtuple('Struct', fields.keys())
    Struct.__new__.__defaults__ = tuple(fields.values())
    return Struct

Vector2D = defaulted_namedtuple('Vector2D', x1 = None, y1 = None, x2 = None, y2 = None, origin_x = 0, origin_y = 0)
print(Vector2D._fields)

v1 = Vector2D(10, 10, 20, 20, origin_x = 0, origin_y = 0)

print('\n')

m = [(1,2,3), (4,5,6)]
print(list(zip(*m)))