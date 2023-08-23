from .calculator import Calc

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def say_hello(name):
    print(f'Hello, {name}!')