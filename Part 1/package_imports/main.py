import common.validators as validators
from common.validators import *
import common.models as models
import common.helpers as helpers


validators.is_boolean('True')
validators.is_date('2019-01-01')
validators.is_json('{"a": 1}')
validators.is_numeric('1')

print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)

# print('\n\n***** common *****')
# for k in common.__dict__.keys(): 
#     print(k)

# print('\n\n***** numeric *****')
# for k in validators.numeric.__dict__.keys():
#     print(k)

# print('\n\n***** validators *****')
# for k in validators.__dict__.keys():
#     print(k) 

# print('\n\n***** models *****')
# for k in models.__dict__.keys():
#     print(k) 

# print('\n\n***** posts (package) *****')
# for k in models.__dict__.keys():
#     print(k) 

calc = helpers.say_hello('Slava')
print(helpers.factorial(5))






# import my_package.my_subp1 as my_subp1
# import my_package.my_subp2 as my_subp2
# from my_package.my_subp1 import *
# from my_package.my_subp2 import *

# print('\n\n***** self *****')
# for k in dict(globals()).keys():
#     print(k)
