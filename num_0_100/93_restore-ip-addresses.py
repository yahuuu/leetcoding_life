class Solution(object):
    def __init__(self):
        self.res = list()
        self.n = 0

    def check_range(self, sub_str):
        if 0 <= int(sub_str) <= 255:
            return True
        return False

    def backtracking(self, s, idx, ls, ip_idx):
        if idx == self.n and len(ls) == 4 and ip_idx == 4:
            # print(ls, ip_idx)
            self.res.append(".".join(ls))
        if idx >= self.n:
            return
        if not ls:
            tmp = s[idx]
        elif ip_idx == len(ls): # 新进ip
            tmp = s[idx]
        elif ls[-1] == "0":
            return
        else:
            tmp = ls[-1] + s[idx]
        if not self.check_range(tmp):  # 数据不在0-255
            return
        if len(ls) == ip_idx + 1:
            ls.pop(-1)
        ls.append(tmp)
        # ls 只初始化一次，ls[:]是深拷贝，不会影响上层栈的数据
        self.backtracking(s, idx + 1, ls[:], ip_idx + 1)  # 增加ip索引
        # 回溯, 也算是dfs吧，毕竟回溯是要恢复状态，我这里全是临时变量。
        self.backtracking(s, idx + 1, ls[:], ip_idx)  # ~增加ip索引

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s.isalnum():
            return []
        self.n = len(s)
        if self.n < 4:
            return []
        self.backtracking(s, 0, [], 0)
        return self.res
