"""
This is my docstring
"""

print('loading timing')

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple('Timing', 'repetitions elapsed average')

def timit(code, repeats=10):
    code = compile(code, filename = '<string>', mode = 'exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)


if __name__ == '__main__':
    # get repeats and code from command line
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', type=str, help = 'The python code string to timeit')
    parser.add_argument('-r', '--repeats', type = int, default=10, help = 'Number of times to repeat the test')
    args = parser.parse_args()
    print(f'timing: {args.code}')
    print(timit(code = str(args.code), repeats = args.repeats))