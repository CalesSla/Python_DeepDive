import math
import fractions
import sys
import types

math.__name__
for k, v in math.__dict__.items():
    print(k, v)

f = math.__dict__['sqrt']

import fractions

sys.modules['fractions']


for k, v in fractions.__dict__.items():
    print(k, v)


mod = types.ModuleType('test', 'this is a test module')

isinstance(mod, types.ModuleType)

mod.pi = 3.14

mod.__dict__['pi']
mod.hello = lambda: 'hello'

mod.hello()

from collections import namedtuple

mod.Point = namedtuple('Point', ['x', 'y'])
p1 = mod.Point(1, 2)
p2 = mod.Point(2, 3)
p1

dir(mod)

def my_func(a, b):
    return a + b

mod.my_func = my_func

mod.my_func(1, 2)

PT = getattr(mod, 'Point')
PT(20,20)

print(sys.prefix)

print(sys.path)