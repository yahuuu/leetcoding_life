# -*- coding:utf-8 -*-
from time import time
from threading import Thread


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


class FactorizeThread(Thread):
    def __init__(self, number):
        Thread.__init__(self)
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


def test(numbers):
    start = time()
    for number in numbers:
        aa = list(factorize(number))
    end = time()
    print('Took %.3f seconds' % (end - start))


def test_thread(numbers):
    start = time()
    threads = []
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()
    end = time()
    print('Mutilthread Took %.3f seconds' % (end - start))


if __name__ == "__main__":
    numbers = [5, 6]

    test(numbers)
    test_thread(numbers)