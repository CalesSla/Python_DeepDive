import timing

code = '[x**3 for x in range(100)]'
print(code)
result = timing.timit(code, repeats=100)
print(result)