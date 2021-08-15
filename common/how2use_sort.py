# -*- coding: utf-8 -*-
# @Time    : 2021/8/14 下午7:38
# @Author  : yahuuu
# @FileName: how2use_sort.py
# @Software: PyCharm

"""
关于为什么要练习这么简单的接口，
公司最近有可信考试，最近考的系统的题目比较多，
系统大多是在处理字符串，考试时间有限没有必要接口造轮子。
"""
a = [1, -1, 2, -3]
# 绝对值
a.sort(key=abs, reverse=True)
print(a)
# 默认排序字符串按照ascii值大小排序
a = ['abc', 'abc', 'Cba', 'bAc']
a.sort()
print(a)

# 如果忽略大小写来排序字符串
sorted(['abc', 'Abc', 'Cba', 'bAc'], key=str.lower)

a = "apple,big"
# 转小写
print(a.lower())
# 转大写
print(a.upper())
# 单词第一个字母大写
print(a.title())
# 首字母大写
print(a.capitalize())

a = [('Zdam', 92), ('Bart', 66), ('Bob', 92), ('Lisa', 88)]
# 先按照成绩讲序，再按照名字字母升序
a.sort(key=lambda x: (-x[1], x[0]), reverse=False)
print(a)

# 重点， 自定义函数
# 只针简单列表， 针对一个key对一个条件
def by_lower(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    return 0


a = [1, 0, 3, 2, 4]
from functools import cmp_to_key
a = sorted(a, key=cmp_to_key(by_lower))
print(a)

# 自定义函数加深
def by_mul(x, y):
    # 先按照第一个条件
    if x[2] < y[2]:
        return -1
    elif x[3] < y[3]:
        return -1
    return 0

a = [["T123", 123, 8, 1], ["T124", 124, 8, 2], ["T125", 125, 9, 2]]
# 即便是多个条件也是从小到大的排序, 改成从大到小
# Tip: lambda根据多个条件
# 有一点需要注意，lambda的x实际上是key
b = sorted(a, key=lambda x: (x[2], x[3]), reverse=True)
# print(b) # [['T125', 125, 9, 2], ['T124', 124, 8, 2], ['T123', 123, 8, 1]]
# 如果需要一个正排序，一个倒排序，加上 - 或者 not
a = [["Tz125", 125, 8, 2], ["Ta123", 123, 8, 1], ["Tb124", 124, 8, 2]]
# 一个倒序 + 一个升序
c = sorted(a, key=lambda x: (-x[2], x[0]))
print("c ", c)
a = sorted(a, key=cmp_to_key(by_mul))
# print(a)

class SortStr(object):
    def __init__(self, obj):
        self.obj = obj
    def __lt__(self, other):
        return other.obj < self.obj

a = [["bb", 2], ["ba", 2], ["Ta", 3], ["Tz", 3]]


class Reversinator():
    def __init__(self, ob):
        self.object = ob
    # < 小于号方法
    # def __lt__(self, other):
    #     return self.object > other.object
    # 未定义__gt__方法时，进行” > ”比较也是调用__lt__方法，只是对调用值求反
    def __gt__(self, other):
        # 在内部调用符号　> 时候，　直接返回这里的值　T or F
        return self.object > other.object


# !!!
# 如果自定的函数，　则not 在函数中不起作用需要自定义一个特殊类。
# 如果not 不起作用,演示如何定义一个字符串比较的类
def get_elem(elem):
    # return (-elem[1], Reversinator(elem[0]))
    return (-elem[1], Reversinator(elem[0]))

d = sorted(a, key=get_elem)
print(d)

# 总结:
# lambda x：x 这里的x是传入的key
# 自定义的排序条件函数需要用cmp_to_key来转化为key类,　这也是py2和py3的区别
# lambda x : (,,,)多个条件，　并且可以用 - 或者 not 来转负条件
