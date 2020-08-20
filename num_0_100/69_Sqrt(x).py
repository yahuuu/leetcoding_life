# coding:utf-8
# Code date: 20200

# 求解根号后的整数
# 我的思路： 二分法找目标数值,一定是在0和输入x之间
# 时间复杂度 O(logN)
# 这道题和其他dfs不同的点： 在使用二分法时候，不能直接递归mid+1
# 难点在于控制边界,这道题的边界我是用debug找到的
class Solution:
    def mySqrt(self, x): #  int) -> int:
        if x == 0 or x == 1: return x
        def helper(left, right):
            if left+1 == right:  # 出栈条件,减少为入栈相邻的两个元素
                return left # right if right*right < x else left
            mid = (left+right)//2
            _rlt = mid*mid -x
            if _rlt < 0:  # mid*mid < x:
                # 这里特别注意mid边界， 否则递归直接扔掉正确数值, 毕竟直接开方是整数的几率很少
                return helper(mid, right)
            elif _rlt > 0:  # mid*mid > x:
                return helper(left, mid)
            else:  # mid * mid == x
                return mid
        return helper(0, x)

# 2牛顿法： 牛顿法的时间复杂度也是O（logN)
# Todo
s = Solution()
res = s.mySqrt(15)
print(res)