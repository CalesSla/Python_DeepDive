# namedtuple defaults
from collections import namedtuple
NT = namedtuple('NT', 'a b c', defaults = (10,20,30))
nt = NT()
print(nt)

# Same defaults for each parameter
NT = namedtuple('NT', 'a b c d e f', defaults = ('xyz',) * 6)
nt = NT()
print(nt)
print(nt._field_defaults)
print('\n')