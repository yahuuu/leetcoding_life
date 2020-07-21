# -*- coding:utf-8 -*-
# Created data: 20200716


# 1 , 90%
# 大意是在文章中反转部分字符

import sys

line = sys.stdin.readline().strip()
start = int(sys.stdin.readline().strip())
stop = int(sys.stdin.readline().strip())
# line = "i am one boy."
# line = "hello  world".strip()
# start = 0
# stop = 3
print(line)

def solution(line, start, stop):
    if line == "": return "EMPTY"
    line = line.split(" ")
    line = [i for i in line if i != ""]
    print(line)
    if len(line) == 1: return "EMPTY"
    set_line = set(line)
    if len(set_line) == set(""): return "EMPTY"
    start = max(0, start)
    stop = min(len(line)-1, stop)
    while start < stop:
        line[start], line[stop] = line[stop], line[start]
        start += 1
        stop -= 1
    return " ".join(line)

#
print(solution(line, start, stop))

"""
"""

# 2
# 查找子串在父串中的第一个索引
import sys
t = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
# t = "AVERDXIVYERDIAN"
# p = "RDXI"
def solution(t, p):
    if not p: return "No"
    for i in range(len(t) - len(p)+1):
        for j in range(len(p)):
            if p[j] != t[j+i]:
                break
        else:
            return i+1
    return "No"

print(solution(t, p))

"""
"""

# 3
# 大意是先找交集, 然后交集合并为并集
import sys
ls = []
while 1:
    line = sys.stdin.readline().strip()
    if not line: break
    line = line.split(" ")
    _ls = list(map(int, line ))
    # print(ls)
    ls.append(_ls)

ls.sort(key= lambda x: x[0])

def solution(ls):
    tmp_ls = []
    for i in range(0, len(ls)-1, 1):
        for j in range(i+1, len(ls)):
            if ls[i][1] < ls[j][0]:
                pass
            elif ls[i][1] == ls[j][0]:
                tmp_ls.append([ls[i][1], ls[i][1]])
            else:
                tmp_ls.append([ min(ls[i][1], ls[j][0]),  min(ls[i][1], ls[j][1]) ])
    return tmp_ls

tmp_ls = solution(ls)
# print(tmp_ls)

def print_ls(tmp_ls):
    rt_ls = []
    tmp_ls.sort(key=lambda x: x[0])
    for k in tmp_ls:
        if rt_ls == []:
            rt_ls.append(k)
        if k[0] > rt_ls[-1][1]:
            rt_ls.append(k)
        else: # only ==
            rt_ls[-1][1] = max(k[1], rt_ls[-1][1])
    # return rt_ls
    if not rt_ls:
        print("None")
        return
    for i, j in  rt_ls:
        print("{} {}".format(i, j))

print_ls(tmp_ls)

