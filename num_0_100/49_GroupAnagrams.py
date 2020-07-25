# -*- coding:utf-8 -*-
# Created data: 20200725

# 题解的思路：
# 维护一个hashmap用来统计
# 这里学到一个不常用的语法，
# sorted("abc") 直接输出['a', 'b', 'c']
# 时间复杂度 O(N* klogk)
# 空间复杂度 O(N * k)   # k是字符串长度

# 优化的思路, 从时间复杂度下手， hashmap思路不变
# 主要优化掉排序的时间复杂度， hashmap来统计

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

# 排序优化掉后 时间复杂度，O(N*2K)  VS O(N*k*lgk)在长字符串统计上有时间优势
# 不过这道题的用例一点不占速度
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
        return list(hashmap1.values())


strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
rt = s.groupAnagrams(strs)
print(rt)
