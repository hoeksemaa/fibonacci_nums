import time
import numpy as np

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Function '{func.__name__}' took {runtime:.6f} seconds to run.")
        return result
    return wrapper

@timeit
def simple_linear(target):
    n0 = 0
    n1 = 1
    index = 1
    temp = 0
    while index != target:
        temp = n1
        n1 = n0 + n1
        n0 = temp
        index += 1

@timeit
# recursive exceeds stack depth hilariously fast; will not benchmark
def simple_recursive(target):
    # base case
    if target == 0:
        return 0
    if target == 1:
        return 1
    # recursive case
    else:
        return simple_recursive(target-1) + simple_recursive(target-2)

"""
# this one also trips on its stack-depth feet too
def memoization(target):
    # this cache is shared with all copies of the inner fn!!
    cache = {}

    def memoized(index):
        # use value from cache if it's there
        if index in cache:
            return cache[index]
        
        # return 0 or 1 as base cases
        if index == 0 or index == 1:
            return index

        # get value and cache it
        value = memoized(index - 1) + memoized(index - 2)
        cache[index] = value
        return value

    return memoized(target)
"""

@timeit
# takes fucking forever; bricks laptop at target = 1000000
def memoization(target):
    cache = {}  # Cache for storing computed Fibonacci values

    for i in range(target+1):
        if i == 0 or i == 1:
            cache[i] = i
        else:
            cache[i] = cache[i-1] + cache[i-2]

    return cache[target]

@timeit
def matrix_exponentiation(target):
    matrix = np.array([[0, 1], [1, 1]], dtype=np.object)
    result = np.linalg.matrix_power(matrix, target)
    answer = matrix[0, 1]

def main():
    base = 100000
    for i in range(20):
        n = base * (i+1)
        print(f"> testing fibonacci # {n}.")
        simple_linear(n)
        matrix_exponentiation(n)

if __name__ == "__main__":
    main()
