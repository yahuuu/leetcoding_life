# -*- coding:utf-8 -*-
# Created data: 20200715

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # ls = ['1', '11', '21', '1211', '111221']
        if n==1: return "1"
        char= "1"
        for _ in range(1, n, 1):
            # 尽量少用内存,只用长度2的list缓存
            tmp = ["", ""]
            _char = ""
            for i in range(0, len(char)):
                if char[i] == tmp[0]:
                    tmp[1] += 1
                else:
                    _char += "{0}{1}".format(tmp[1], tmp[0])# num, element
                    tmp[0] = char[i]  # element update
                    tmp[1] = 1  # count
            _char += "{0}{1}".format(tmp[1], tmp[0])  # num, element
            char = _char
        return char


s = Solution()
rt = s.countAndSay(5)
print(rt)
