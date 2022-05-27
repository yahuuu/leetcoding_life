#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i=0; i<32; i++) {
            res = (res << 1) + (n >> i & 1);
        }
        return res;
    }
};

int main() {
    uint32_t n = 12;
    Solution solution{};
    auto res = solution.reverseBits(n);
    cout << res << endl;
    cout << "高位 --> 低位:" << endl;
    for(int i =0; i<32; i++ ) {
        cout << ((res >> i)&1) << " ";
    }
    return 0;
}

// int 固定 32 位，循环次数不随输入样本发生改变。复杂度为 O(1)O(1)
