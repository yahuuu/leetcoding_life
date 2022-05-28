#include <iostream>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int res = 0;
        int i = columnTitle.size()-1;
        long mul = 1;
        for (; i >=0; i--) {
            int ele = columnTitle[i] - 'A' + 1;
            res += ele * mul;
            mul *= 26;
        }
        return res;
    }
};

int main() {
    string columnTitle = "FXSHRXW";
    Solution solution{};
    auto res = solution.titleToNumber(columnTitle);
    cout << res << endl;
    return 0;
}