
print('====================================================================')

print(f'Running main.py - module name: {__name__}')

import module1

module1.pprint_dict('main.globals', globals())

del globals()['module1']

print('importing module1 again')
import module1

print('====================================================================')