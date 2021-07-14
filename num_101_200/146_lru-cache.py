# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 下午10:13
# @Author  : yahuuu
# @FileName: 146_lru-cache.py
# @Software: PyCharm

# 实现 LRUCache 类：
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字已经存在，则变更其数据值；
# 如果关键字不存在，则插入该组「关键字-值」。
# 当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        pass

    def get(self, key: int) -> int:
        if self.cache.get(key, None) is None:
            return -1
        value = self.cache[key]
        self.cache.pop(key)  # 为了放在队列尾部
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, None) is not None:
            self.cache.move_to_end(key) # 查过就认为是最新的
            self.cache[key] = value
            return
        self.cache[key] = value
        if self.capacity < len(self.cache):
            self.cache.popitem(last=False)



# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
lRUCache = LRUCache(2)
lRUCache.put(1, 0) # // 缓存是 {1=1}
print(lRUCache.cache)
lRUCache.put(2, 2) # // 缓存是 {1=1}
print(lRUCache.cache)
print(lRUCache.get(1))    # // 返回 -1 (未找到)
lRUCache.put(3, 3) # // 缓存是 {1=1}
print(lRUCache.cache)
print(lRUCache.get(2))    # // 返回 -1 (未找到)
lRUCache.put(4, 4) # // 缓存是 {1=1}
print(lRUCache.cache)
print(lRUCache.get(1))    # // 返回 -1 (未找到)
print(lRUCache.get(3))    # // 返回 -1 (未找到)
print(lRUCache.get(4))    # // 返回 -1 (未找到)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)