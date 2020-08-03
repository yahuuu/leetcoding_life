# coding:utf-8
# Code Date: 20200803

# time win: 5.1%, mem win: 68.06%
class Solution1(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str 1234
        :rtype: str
        """
        sum = 0
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1

        num1 = num1[::-1]
        num2 = num2[::-1]
        i, j = 0, 0
        n1 = len(num1)
        n2 = len(num2)
        while i<n1 or j<n2:
            while i < n1:
                sum += 10**i*int(num1[i])
                i += 1
            while j < n2:
                sum += 10**j*int(num2[j])
                j += 1
        return sum

# time win: 88% , mem win 5%
# 上边的解法用到乘法和次幂，下面改成除法和取余，效率高了很多
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str 1234
        :rtype: str
        """
        sum = 0
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1
        n1 = len(num1)
        n2 = len(num2)
        num1 = [int(ele) for ele in num1][::-1]
        num2 = [int(ele) for ele in num2][::-1]
        add = 0
        res = []
        for i in range(min(n1, n2)):
            if add == 1:
                sum = (1+num1[i]+num2[i])
            else:
                sum = (num1[i]+num2[i])
            add = (sum)//10
            res.append((sum)%10)
        last = num1[i + 1:] + num2[i + 1:]

        for j in range(len(last)):
            if add == 0:
                break
            else:
                sum = last[j] + 1
                last[j] = (sum) % 10
                add = (sum)//10
        if add == 1:
            last.append(1)

        res.extend(last)
        return "".join([str(ele) for ele in res[::-1]])


num1 = "118"
num2 = "5"
s = Solution()
res = s.addStrings(num1, num2)
print(res)