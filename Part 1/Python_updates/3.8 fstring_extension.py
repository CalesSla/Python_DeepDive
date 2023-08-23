# f-string extension
a, b = 'hello', 'world'
print(f'a = {a}, b = {b}')

# new alternative syntax
a, b = 'hello', 'world'
print(f'{a=}, {b=}')

# Specify the type in the f-string
a, b = 'hello', 'world'
print(f'{a=:s}, {b=:s}')

# f-string formats for other data types
from datetime import datetime
from math import pi

d = datetime.utcnow()
e = pi

print(f'{d=}, {e=}')
print(f'{d=:%Y-%m-%d %H:%M:%S}, {e=:.2f}')

# More f-string examples
sentence = ['Python', 'rocks!']
print(f'{1+2=}, {" ".join(sentence)=}')