// 用深度搜索，时间会超时
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
private:
    vector<string> res;

    void dfs(string str, vector<int> cache) {
        if (cache.empty()) {
            res.push_back(str);
            return;
        }
        int max_first_ = -1;
        for (auto ele: cache) {
            int tmp = ele;
            while (tmp > 9) {
                tmp /= 10;
            }
            if (tmp > max_first_) {
                max_first_ = tmp;
            }
        }
        int idx_ = -1;
        vector<vector<int>> equalFirstNum{};
        for (auto ele: cache) {
            idx_++; // begin开始 , +值
            int tmp = ele;
            while (tmp > 9) {
                tmp /= 10;
            }
            if (tmp == max_first_) {
                equalFirstNum.push_back({ele, idx_});
            }
        }
        for (auto ele: equalFirstNum) {
            string tmpStr = str + to_string(ele.front());
//            str += to_string(ele.front());
            int idx = ele.back();
            vector<int> tmp{cache};
            tmp.erase(tmp.begin() + idx);
            dfs(tmpStr, tmp);
        }
    }

public:
    string largestNumber(vector<int> &nums) {
        dfs("", nums);
        int vectorLen = res.size();
        string max_num_str = res.front();
        for (int i = 1; i < vectorLen; i++)
            if (max_num_str < res[i]) {
                max_num_str = res[i];
            };
#if 0
        for(auto ele: res) {
            cout << ele <<endl;
        }
#endif
        if (max_num_str[0] == '0') {
            return "0";
        }
        return max_num_str;
    }
};