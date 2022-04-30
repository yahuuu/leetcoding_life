class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        target_set = set()
        res = ""
        len_res = float("inf")
        for i in range(len(t)):
            target_set.add(t[i])
        l = 0
        r = 0
        while r < len(s):
            tmp_str = s[l:r+1]
            if (set(tmp_str) & target_set) != target_set:
                r+=1
            else:
                while True:
                    l += 1
                    tmp_str = s[l:r + 1]
                    if (set(tmp_str) & target_set) != target_set:
                        if len_res > (r+1-(l-1) +1):
                            res = s[l-1:r+1]
                            len_res = len(res)
                        break
                r+=1
        return res

if __name__ == '__main__':
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "A"
    t = "AA"
    solu = Solution()
    res = solu.minWindow(s, t)
    print(res)
