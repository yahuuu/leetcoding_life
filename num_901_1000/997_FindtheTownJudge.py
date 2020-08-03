# -*- coding:utf-8 -*-
# Created data: 20200710


# https://leetcode-cn.com/problems/find-the-town-judge/
# 用字典统计, 信任-1,  被信任+1

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        dict = {i:0 for i in range(1,N+1)}
        for a, b in trust:
            dict[b] += 1
            dict[a] -= 1
        for i in range(1,N+1):
            if dict[i] == N-1:
                return i
        return -1

class Solution1(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        dict = {i:0 for i in range(1,N+1)}
        for a, b in trust:
            dict[b] += 1
            dict[a] -= 1
        dict = {i:j for j,i in dict.items() if i==N-1}
        return dict.get(N-1, -1)


if __name__ == "__main__":
    s = Solution1()
    N = 4
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    # N = 3
    # trust = [[1, 2], [2, 3]]
    rt = s.findJudge(N, trust)
    print(rt)
