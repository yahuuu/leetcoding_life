# -*- coding:utf-8 -*-
# Created data:
import time


# 4 class.functions
def timers(origin_func):
    def wrapper(self, *args, **kwargs):
        try:
            t1 = time.time()
            u = origin_func(self, *args, **kwargs)
            print(time.time() - t1)
            return u
        except Exception as e:
            print(e)
    return wrapper


# 4 functions
def timer(func):
    def inner(self, *args, **kwargs):
        t1 = time.time()
        func()
        print(time.time()-t1)
    return inner