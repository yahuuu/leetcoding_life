# -*- coding:utf-8 -*-
# Created data: 20200725

from collections import defaultdict

class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == "":
            return []
        hashmap = defaultdict(list)
        for eles in strs:   # O(N)
            hashmap[tuple(sorted(eles))].append(eles) # O(klogk)
        return list(hashmap.values())


class Solution(object):

    def groupAnagrams(self, strs):
        if strs == "":
            return []
        hashmap1 = defaultdict(list)
        for ele in strs:  # O(N)
            dic2 = dict().fromkeys(range(26), 0)  # O(k)
            for char in ele:  # O(k)
                dic2[ord(char)-ord('a')] = \
                    dic2.get(ord(char)-ord('a'), 0) +1
            val= tuple(dic2.values())
            hashmap1[val].append(ele)
        Solution1().groupAnagrams(strs)
        return list(hashmap1.values())


strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
# ♠1
# kernprof -l -v scrip.py
# ♠2
from line_profiler import LineProfiler
lp = LineProfiler()
lp.add_function(Solution1.groupAnagrams) # 被引用函数需要声明才显示细节
lp_wrapper = lp(Solution().groupAnagrams)  # 被显示的函数
lp_wrapper(strs)  # 参数传入
lp.print_stats()  # 打印喽

