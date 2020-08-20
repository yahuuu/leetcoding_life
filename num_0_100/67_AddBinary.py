# coding:utf-8
# Code date: 20200

# 字符串对应位置相加，如果是2就标记进位
# 我在处理不同长度的字符串时候，短的字符串相加时候用0
class Solution_org:
    def addBinary(self, a: str, b: str) -> str:
        if a == "" or b == "":
            return a or b
        na = len(a)-1
        nb = len(b)-1
        n = max(na, nb)
        add = 0  # 进位
        ls = []
        for i in range(n, -1, -1):
            if na>=0:
                ele1 = int(a[na])
            else:
                ele1 = 0

            if nb>=0:
                ele2 = int(b[nb])
            else:
                ele2 = 0
            _add = (ele1+ele2 + add) // 2
            tmp = (ele1+ele2 + add) % 2
            add = _add
            ls.append(str(tmp))
            na -= 1; nb -= 1
        if add:
            ls.append("1")
        return "".join(ls)[::-1]

# 另一种处理不同长度的方法，不对齐，是按照短的元素相加，长的部分就和进位相加
# 这两种思路大同小异，都是对应元素转int然后取%作为该元素， 进位用//
# 遗憾是时间win 我不满意，看看别人思路把。
# 官方用的是内建函数，很无语, 我的解法就是推荐
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "" or b == "":
            return a or b
        na = len(a)-1
        nb = len(b)-1
        n = min(na, nb)
        add = 0  # 进位
        ls = []
        for i in range(n, -1, -1):
            _add = (int(a[na])+int(b[nb])+ add) // 2
            tmp = (int(a[na])+int(b[nb]) + add) % 2
            add = _add
            ls.append(str(tmp))
            na -= 1; nb -= 1
        for ele in (a[0:na+1][::-1] or b[0:nb+1][::-1]):
            tmp = (int(ele) + add) % 2
            add = (int(ele) + add) //2
            ls.append(str(tmp))
        if add:
            ls.append("1")
        return "".join(ls)[::-1]

a = "100"; b = "110010"
# Output: "10101"
s = Solution()
res = s.addBinary(a, b)
print(res)
