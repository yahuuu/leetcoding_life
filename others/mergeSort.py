# -*- coding:utf-8 -*-
# Created data: 20200724

# once AC
def merge_sort(ls):
    if len(ls) <= 1: return ls
    def splitls(sub_ls):
        if len(sub_ls) == 1:
            return sub_ls
        mid = len(sub_ls) // 2
        left = splitls(sub_ls[:mid])
        right =splitls(sub_ls[mid:])
        rt = []
        # for i in range(max(len(left), len(right))):
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                rt.append(left[i])
                i += 1
                # left.pop(0)  # O(N)
            else:
                rt.append(right[j])
                j += 1
        rt.extend( left[i:])
        rt.extend(right[j:])
        return rt
    return splitls(ls)


if __name__ == "__main__":
    import random
    # ls = [1,3,2,5,6,0]
    ls = [random.randint(0,30) for _ in range(10)]
    rt = merge_sort(ls)
    print(rt)
