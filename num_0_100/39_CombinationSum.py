# -*- coding:utf-8 -*-
# Created data: 20200720

"""
思路
直接上回溯算法框架。解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：
1、路径：也就是已经做出的选择。
2、选择列表：也就是你当前可以做的选择。
3、结束条件：也就是到达决策树底层，无法再做选择的条件。

链接：
https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-tao-mo-ban-ji-ke-by-jeromememory/

"""

# 回溯是我的弱点，
# 这道题写的很痛苦
class Solution:
    def combinationSum(self, candidates, target):  # List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        candidates.sort()
        self.rt = list()

        def dfs(start, end, path, target):  # path是走过的路径
            if target == 0:  # 出栈条件
                # 递归该结束的点，放入返回的栈中
                self.rt.append(path.copy())  # 其他栈可能要用，所以深度拷贝
                return
            for idx in range(start, end):  # 当前可以做的选择
                residual = target - candidates[idx]
                if residual < 0:  # 无效路径
                    break
                path.append(candidates[idx])
                dfs(idx, end, path, residual)
                path.pop()  # 遍历前扔掉其他栈的最后路径

        path = list()  # 递归中用的临时栈
        dfs(start=0, end=len(candidates), path=path, target=target)
        return self.rt


from typing import List
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝是为了提速，在本题非必需
        candidates.sort()
        # 在遍历的过程中记录路径，它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])
            return

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()

"""
39.组合总和
40. 组合总和 II
46. 全排列
47. 全排列 II
78. 子集
90. 子集 II
"""

# 日常练习， 思路一致， 递归+回溯+剪枝
class Solution3(object):
    def combinationSum(self, candidates, target):
        rt = []
        if not candidates: return rt
        candidates.sort()
        n = len(candidates)
        def search(left, ls, residual):
            ls.append(candidates[left])
            residual -= candidates[left]
            if residual < 0:
                return
            if residual == 0:
                rt.append(ls.copy())
            # >0
            for i in range(left, n):
                if candidates[i] > residual:
                    break
                search(i, ls, residual)
                ls.pop(-1)

        for i in range(len(candidates)):
            search(i, [], target)
        return rt


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution3()
    result = solution.combinationSum(candidates, target)
    print(result)








































