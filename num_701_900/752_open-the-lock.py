# coding=utf-8

from typing import List
from collections import deque

"""
想清楚每一次拨动会出现的八种情况。
根据java改写的。
"""

class Solution:
    def up_lock(self, now: str, index: int):
        ls = [int(i) for i in now]
        ls[index] = ls[index] + 1 if ls[index] != 9 else 0
        return "".join([str(i) for i in ls])

    def down_lock(self, now, index):
        ls = [int(i) for i in now]
        ls[index] = ls[index] - 1 if ls[index] != 0 else 9
        return "".join([str(i) for i in ls])

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        doubleque = deque()
        step = 0
        doubleque.append("0000")
        visited.add("0000")
        while doubleque:
            num = len(doubleque)
            for _ in range(num):
                now_number = doubleque.popleft()
                if now_number == target:
                    return step
                if now_number in deadends:
                    continue
                for j in range(4):
                    up_num = self.up_lock(now_number, j)
                    if up_num not in visited:
                        doubleque.append(up_num)
                        visited.add(up_num)
                    down_num = self.down_lock(now_number, j)
                    if down_num not in visited:
                        doubleque.append(down_num)
                        visited.add(down_num)
            step += 1
        return -1


if __name__ == '__main__':
    solu = Solution()
    # ret = solu.openLock(["0201","0101","0102","1212","2002"], "0202")
    ret = solu.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888")
    # ret = solu.openLock(["8888"], "0008")
    print(ret)

