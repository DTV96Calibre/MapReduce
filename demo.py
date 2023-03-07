#!/usr/bin/env python
"""Demo code for performing MapReduce using python
"""
from multiprocessing import Pool
from functools import reduce

def f(x):
    return x*x
def add(x, y):
    return x + y

def main():
    """Run MapReduce demo"""
    # Spawn compute processes
    p = Pool(3)

    # Marshal data to compute processes
    # Unmarshal data from compute processes
    results = p.map(f, [1, 2 ,3])

    # Reduce pool results to single result
    total = reduce(add, results)
    print(total)

if __name__ == '__main__':
    main()
