import importlib
import sys

mod_name = 'math'

importlib.import_module(mod_name)

print('fractions' in sys.modules)

math2 = sys.modules.get('math')
print(math2.sqrt(2))

math2 = importlib.import_module(mod_name)

print('math2' in globals())

fractions = importlib.import_module('fractions')

print(fractions)

import numpy

print(numpy.__spec__)

print('\n')
for i in sys.meta_path:
    print(i)

import module1
print(module1.__spec__)


print(importlib.util.find_spec('decimal'))


with open('module1_new.py', 'w') as code_file:
    code_file.write('print("running module1_new.py")\n')
    code_file.write('a = 100\n')

print(importlib.util.find_spec('module1_new'))

import module1_new

print(module1_new.a)

import os

ext_module_path = os.environ['HOMEPATH']
print(ext_module_path)
file_abs_path = os.path.join(ext_module_path, 'module2_new.py')

with open(file_abs_path, 'w') as code_file:
    code_file.write('print("running module2_new.py")\n')
    code_file.write('x = "python"\n')


print(importlib.util.find_spec('module2_new'))

for i in sys.path:
    print(i)

sys.path.append(ext_module_path)


for i in sys.path:
    print(i)

print(importlib.util.find_spec('module2_new'))

import module2_new
print(module2_new.x)