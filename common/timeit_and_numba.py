import numba as nb
from numba import jit
import numpy as np
from timeit import timeit

@jit('f8(f8[:])')
def sum1d(array):
    s = 0.0
    n = array.shape[0]
    for i in range(n):
        s += array[i]
    return s

array = np.random.random(10000)

# print(timeit(sum1d(array), number=100))
# print(timeit(np.sum(array), number=100))
# print(timeit(sum(array), number=100))
t1 = timeit('sum1d', "from __main__ import sum1d", number=1000)
print(t1)
t2 = timeit('np.sum(array)', "from __main__ import array, np", number=1000)
print(t2)
t3 = timeit('sum(array)', "from __main__ import array", number=1000)
print(t3)
