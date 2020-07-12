# -*- coding:utf-8 -*-
# Created data: 20200711

# 建立树,深度优先遍历, 在最深层记录此时的终点.

class Solution(object):
    def findItinerary(self, tickets):
        from collections import defaultdict
        dic = defaultdict(list)
        # 先按照字母倒排序, 主要为了pop(-1)省时间
        tickets.sort(key=lambda x: x[1], reverse=True)
        # build
        for i, j in tickets:
            dic[i].append(j)
        # travel
        rt = []
        def helper(_source):
            while dic[_source]:
                next = dic[_source].pop(-1)
                helper(next)
            # 每层最深处记录
            rt.append(_source)

        helper("JFK")
        # 记录的是[ 终点,中间点, 起点], 所以倒顺序
        return rt[::-1]


if __name__ == "__main__":
    s = Solution()
    # tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print(s.findItinerary(tickets))