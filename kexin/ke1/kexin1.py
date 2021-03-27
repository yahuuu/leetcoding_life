class Solution:
    def get_optimal_strategy(self, first_group, second_group):
        tmpa = sorted(first_group)
        tmpb = sorted(second_group)
        dict_b = {idx:ele for idx, ele in enumerate(second_group)}
        if not ((tmpa[1] > tmpb[0]) and (tmpa[2] > tmpb[1])):
            return "empty"
        ret = self.helper(first_group, second_group)
        #
        return ret

    def helper(self, first_a, second_b):
        first_a.sort(reverse=False)  # small to big
        record_a_used = [0, 0, 0]   # 4 recode
        ret = []
        for idx, ele_b in enumerate(second_b):
            for i in range(3):
                if ele_b < first_a[i] and (record_a_used[i] != 1):
                    ret.append(first_a[i])
                    record_a_used[i] = 1
                    break
            else:
                for i in range(3):
                    if record_a_used[i] == 0:
                        ret.append(first_a[i])
                        record_a_used[i] = 1
                        break
        return ret


if __name__ == "__main__":
    first_group = list(map(int, input().strip().split(",")))
    second_group = list(map(int, input().strip().split(",")))
    function = Solution()
    results = function.get_optimal_strategy(first_group, second_group)
    if results == "result":
        print(results)
    else:
        print(",".join(map(str, results)))
