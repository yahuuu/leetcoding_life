# -*- coding:utf-8 -*-
# Created data:20200713

# 原本参考知乎公众号的文章,结果发现有错误
# 基本原理是栈, 不同之处是要存入下标,同时,为了避免()(()()的情况,
#                                              | 此处未出栈

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack = [-1]
        max_long = 0
        _max = 0
        for idx, i in enumerate(s):
            if i == "(":
                stack.append(idx)
            else:
                # )出栈
                stack.pop(-1)
                if not stack:
                    # 栈为空, 此时来),下标入栈
                    stack.append(idx)
                else:
                    # 判断是否有剩余的(未出栈
                    if len(stack)==1:
                        _max = idx - stack[0]
                    # 有注意要减掉未出栈的(下标
                    else:
                        _max = idx - stack[-1]
                    max_long = max(max_long, _max)
        return max_long

#    0123456
s = "()((())"
# [-1] 初始状态
# ( 入栈下标
# ) 弹出, 栈长度为1, idx和-1 做差, 更新最大长度2
# ( 入栈下标
# ( 入栈下标
# ( 入栈下标
# ) 弹出, 栈长度为1, idx=5和3, 而不是-1 做差, 更新最大长度2
# ) 弹出, 栈长度为1, idx=6和2, 而不是-1 做差, 更新最大长度4
# Done!

so = Solution()
print(so.longestValidParentheses(s))