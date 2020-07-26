# -*- coding:utf-8 -*-
# Created data: 20200725


from collections import defaultdict


class Solution(object):

    @profile
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

# ♠1
# python -m memory_profiler script.py
# ♠2
# from memory_profiler import profile
# python scrip.py
