# -*- coding:utf-8 -*-
# Created data:

# import sys
#
# line = sys.stdin.readline().strip()
# while line != "0 0":
#     line = list(map(int, line.split(" ")))
#     print(sum(line))
#     line = sys.stdin.readline().strip()

# import sys
# while 1:
#     line = sys.stdin.readline().strip()
#     if line == "0": break
#     line = list(map(int, line.split(" ")))
#     print(sum(line))

# import sys
#
# num = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip().split(" ")
# s.sort()
# for i in s:
#     print(i)


# import sys
#
# while 1:
#     s = sys.stdin.readline().strip()
#     if not s:
#         break
#     s.split(" ").sort()
#
#     print(" ".join(s))


s = input().strip()
dic = dict()
for char in s:
    dic[char] = dic.get(char, 0) +1

item = list(dic.items())
item.sort(key= lambda x:x[0])
item.sort(key=lambda x:x[-1], reverse=True)
print(item)
s = ""
for i in item:
    s += i[0]

print(s)