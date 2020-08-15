# coding:utf-8
# Code date: 20200815

from typing import List

class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        关于上面的注释，list插入， 这样当然会增加时间复杂度,新建一个list做缓存
        """
        _ls = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ele = nums1[i]
                i += 1
            elif nums1[i] == nums2[j]:
                ele = nums1[i]
                i += 1
                j += 1
            else:
                ele = nums2[j]
                j += 1

            if not _ls:
                _ls.append(ele)
            elif _ls[-1] != ele:
                _ls.append(ele)  # 否， 扔
        last_ls = (nums1[i:m] or nums2[j:n])
        for ele in last_ls:
            if ele != _ls[-1]:
                _ls.append(ele)


        nums1 = _ls  # 换了一块内存
        # nums1.append(1)  # 内存不变
        print(_ls)
        return _ls

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        真的在nums1上操作
        """
        i = 0
        for j in range(n):
            if nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                i += 1 # nums1 增加元素了
                m += 1
                nums1.pop(-1)

            else:  # >=
                # 在nums1中找合适位置插入
                while nums2[j] > nums1[i] and i < m:
                    i += 1
                nums1.insert(i, nums2[j])
                m += 1
                nums1.pop(-1)
#

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]; m = 3
    nums2 = [2, 5, 6]; n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)
