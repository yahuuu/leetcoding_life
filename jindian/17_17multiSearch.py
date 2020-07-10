# -*- coding:utf-8 -*-
# Created data:20200710


# class Solution:
#     def multiSearch(self, big, smalls):
#         # build trie tree
#         trie_tree = {}
#         for i, word in enumerate(smalls):
#             tree = trie_tree
#             for c in word:
#                 if c not in tree:
#                     tree[c] = {}
#                 tree = tree[c]
#             tree[-1] = i  # 单词结束标志，同时记录 small 单词索引
#         # search
#         print(trie_tree)
#         res = [[] for _ in range(len(smalls))]
#         for i in range(len(big)):
#             tree = trie_tree
#             for j in range(i, len(big)):
#                 if big[j] not in tree:
#                     break
#                 tree = tree[big[j]]
#                 if -1 in tree:
#                     res[tree[-1]].append(i)
#         return res




"""
用例如:
# big = "abcd"
# smalls = ["a","abc"]
smalls构造字典树, 结构:
trie.root = {"a": Node_0xx}
                  Node.word_idx = 0   # 第1个单词
                  Node.word_end = True
                    \
                    {"b": Node_0xx}
                          Node.word_end = False
                          # 不是叶子没有word_idx省内存呵呵
                              \
                            {"c": Node_0xx}
                                  Node.word_idx = 1  # 第2个单词
                                  Node.word_end = True
搜索普通遍历,时间复杂度O(n**2), n = len(big)
"""
class Node(object):
    # 节点
    def __init__(self):
        self.dic = {}
        self.word_end = False
        # self.word_idx = None # 挂在单词最后一个字符节点上

class Trie(object):
    def __init__(self):
        self.root = {}
    def insert_word(self, word, idx):
        # 空word ""
        if word=="" : return
        cur_dic = self.root
        for char in word:
            cur_dic.setdefault(char, Node())
            ob = cur_dic[char]
            cur_dic = ob.dic
        ob.word_end = True
        ob.word_idx = idx


class Solution:
    def multiSearch(self, big, smalls):
        self.build_tree(smalls)
        rt = [[] for _ in range(len(smalls))]
        for i in range(len(big)):
            cur = self.trie.root
            for j in range(i, len(big)):
            # for location, char in enumerate(big[i:]):
                if big[j] in cur:
                    ob = cur[big[j] ]
                    # _idx = ob.word_idx
                    _end = ob.word_end
                    cur = ob.dic
                    if _end: rt[ob.word_idx].append(i)
                else: break
        return rt

    def build_tree(self, smalls):
        self.trie = Trie()
        for idx, word in enumerate(smalls):
            self.trie.insert_word(word, idx)


s = Solution()
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
# big = "abcd"
# smalls = ["a","ab"]
print(s.multiSearch(big, smalls))