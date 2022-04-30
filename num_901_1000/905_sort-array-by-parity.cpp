#include <vector>
#include <deque>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> sortArrayByParity(vector<int> &nums) {
        deque<int> que{};
        for (auto &num : nums) {
            if (0 == num % 2) {
                que.push_front(num);
                continue;
            }
            que.push_back(num);
        }
//        vector<int> res = vector<int>();
//        vector<int> res{};
//        for (int i = 0; i < que.size(); i++) {
//            res.push_back(que[i]);
//        }
        vector<int> res({que.begin(), que.end()});
        return res;
    }
};