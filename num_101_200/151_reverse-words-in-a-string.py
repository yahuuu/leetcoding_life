# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 上午10:58
# @Author  : yahuuu
# @FileName: 151_reverse-words-in-a-string.py
# @Software: PyCharm

class Solution:
    def strip_space(self):
        self.s = self.s.strip()
        self.s = list(self.s)

    def reverse_str(self, i, j):
        # i = 0; j = num-1
        while i < j:
            self.s[i], self.s[j] = self.s[j], self.s[i]
            i += 1
            j -= 1

    def reverse_ele(self):
        num = len(self.s)
        self.ls = list()
        for idx in range(num):
           if idx == 0:
               self.ls.append(0)
           elif self.s[idx-1] == " " and self.s[idx] != " ":
               self.ls.append(idx)
           if idx == num-1:
               self.ls.append(idx)
           elif self.s[idx] != " "  and self.s[idx+1] == " ":
               self.ls.append(idx)
        self._temp = list()
        for i in range(len(self.ls)//2):
            self.reverse_str(self.ls[i*2], self.ls[i*2+1])
            self._temp.append("".join(self.s[self.ls[i*2]: self.ls[i*2+1]+1]))
        self.res = " ".join(self._temp)


    def reverseWords(self, s: str) -> str:
        self.s = s
        self.strip_space()
        self.reverse_str(0, len(self.s)-1)
        self.reverse_ele()
        return self.res

if __name__ == '__main__':
    s = "  Bob    Loves  Alice   "
    solu = Solution()
    res = solu.reverseWords(s)
    print(res)