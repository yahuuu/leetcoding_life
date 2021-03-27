# encoding:utf-8

import time

def fibonacci():

    a, b = 0, 1
    while a < 10000000000:
        yield a
        a, b = b, a+b

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10000000000:
            raise StopIteration()
        return self.a


if __name__ == "__main__":
    t1 = time.time()
    for _ in range(100000):
        for n in fibonacci():  # yield
        # for n in Fib():      # iter
            pass
    print(time.time()-t1)
