# coding:utf-8
# Code date: 20200815

# 两个字符串指针找前后点
class Solution1:
    def lengthOfLastWord(self, s:  str) -> int:
        s = s.strip()
        if not s: return 0
        n = len(s)-1
        begin = 0
        end = 0
        for i in range(n, -1, -1):
            if s[i] != " " and begin == 0:
                begin = i
            if begin != 0 and s[i] == " ":
                end = i+1
                break
        return begin-end+1


# 思路一样，只是不用.strip内置函数
class Solution:
    def lengthOfLastWord(self, s:  str) -> int:
        if not s:
            return 0
        r = l = 0
        move = False
        for i in range(len(s)-1, -1, -1):
            if r == 0 and s[i] != " ":
                r = i
                move = True
                if r == 0: return 1  # 只有一个元素
            if r != 0:
                if s[i] != " ":
                    l = i
                if s[i] == " ":
                    break

        if not move and r == 0:
            return 0
        return r-l+1

s = " aa halll"
solu = Solution()
res = solu.lengthOfLastWord(s)
print(res)
