# -*- coding:utf-8 -*-
# Created data: 20200713

class Solution(object):
    def merge(self, intervals): # List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals

        intervals.sort(key=lambda x: x[0])
        print(intervals)
        rt = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > rt[-1][1]:
                rt.append(intervals[i])
            else:
                rt[-1][1] = max(rt[-1][1], intervals[i][1])
        return rt


s = Solution()
print(s.merge([[1,3],[8,10],[2,6],[15,18]]) )