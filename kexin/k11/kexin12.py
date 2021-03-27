# coding:utf-8

class Solution:

    def helper(self, begin_idx, num_len, return_lgth):
        if begin_idx == self.end+1:
            return return_lgth
        if begin_idx > self.end+1:
            return -1
        if not self.encoded_string[begin_idx].isdigit():
            return -1
        if (self.end - begin_idx) < int(self.encoded_string[begin_idx:begin_idx + 1 + num_len]):
            return -1
        if self.encoded_string[begin_idx] == "0" :
            if begin_idx < self.end:
                return -1
            if begin_idx == self.end:
                return return_lgth

        return_lgth += int(self.encoded_string[begin_idx:begin_idx + 1 + num_len])
        re1 = self.helper(begin_idx + 1 + int(self.encoded_string[begin_idx: (begin_idx+1+num_len)]), num_len=0, return_lgth=return_lgth)
        re2 = -1
        if (begin_idx + 1) <= self.end and self.encoded_string[begin_idx + 1].isdigit():
            num_len += 1
            re2 = self.helper(begin_idx + 1 + num_len + int(self.encoded_string[begin_idx: (begin_idx+1+num_len)]), num_len=num_len, return_lgth=return_lgth)

        return re1 if (re2 == -1) else -1

    def get_length(self, encoded_string: str) -> int:
        self.end = len(encoded_string) - 1
        if self.end == 0 and encoded_string != "0":
            return -1
        if self.end == 0 and encoded_string == "0":
            return 1
        self.encoded_string = encoded_string
        re = self.helper(0, 0, 0)
        return re


if __name__ == "__main__":
    first_input = input()
    print(first_input)
    funct = Solution()
    print(funct.get_length(first_input))
