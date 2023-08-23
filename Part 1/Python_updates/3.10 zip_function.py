# Zip function update and zip_longest function
l1 = ['a', 'b', 'c']
l2 = [10, 20, 30, 40, 50]

print(list(zip(l1, l2)))

from itertools import zip_longest
print(list(zip_longest(l1, l2, fillvalue='???')))


# Strict parameter of zip function
l1 = (i**2 for i in range(4))
l2 = (i**3 for i in range(3))
print(list(zip(l1, l2)))

result = list(zip(l1, l2, strict=True))
print(result)