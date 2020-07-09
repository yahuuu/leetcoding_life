# -*- coding:utf-8 -*-


class Solution:
    def minDepth(self, root): #TreeNode) -> int:
        if root == None: return 0
        def inner_search(cur, deep):
            if not cur: return deep
            # 向左树搜索，如果左边是空，那么要赋值+无穷，令左边搜索结果无效
            # 如果返回此时深度deep那么next_deep会取错误的深度,如：
            #    1
            #   /  \
            #  2   null
            #  这颗树的深度是2 ，不是1
            left_deep = inner_search(cur.left, deep+1) if cur.left else float("inf")
            right_deep = inner_search(cur.right, deep+1) if cur.right else float("inf")
            # 寻找浅的路径
            next_deep = min(left_deep, right_deep)
            # 如果是+无穷，该节点是叶子，替换此时深度
            return next_deep if next_deep!=float("inf") else deep

        return inner_search(root, 1)


