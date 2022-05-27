#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ret = 0;
        for (int i = 0; i < 32; i++) {
            if (n & (1 << i)) {
                ret++;
            }
        }
        return ret;
    }
};

int main() {
    uint32_t n = 11;
    Solution solution{};
    auto res = solution.hammingWeight(n);
    cout << res << endl;
    return 0;
}