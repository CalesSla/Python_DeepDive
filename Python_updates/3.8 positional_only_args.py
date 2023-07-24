# Keyword-only arguments after *
def my_func(a, b, *, c):
    return a + b + c
print(my_func(1, 2, c=3))

# Positional-only parameters before /
def my_func(a, b, / , c):
    return a + b + c
print(my_func(1, 2, c=3))

# Positional-only parameters before / and keyword-only arguments after *
def my_func(a, b, /, *, c):
    return a + b + c
print(my_func(1, 2, c=3))
print('\n')
