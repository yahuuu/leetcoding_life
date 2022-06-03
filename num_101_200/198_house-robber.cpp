#include <iostream>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

// 递归的方法必须要用缓存优化下重复计算，否则时间超限制
class Solution_my {
public:
    int rob(vector<int>& nums) {
        if(nums.size()==0) return 0;
        if (nums.size()==1) return nums.front();
        int res = helper(nums.size()-1, nums);
        return res;
    }
private:
    unordered_map<int, int> umap;
private:
    int helper(int k, vector<int>& nums) {
        if (k==0) {
            return nums[k];
        }
        else if(k==1) {
            return max(nums[0], nums[1]);
        }
        else {
            if (umap.count(k) !=0) {
               return umap[k];
            }
            // 当前偷或者当前不偷
            int resK= max(nums[k]+helper(k-2, nums), helper(k-1, nums));
            umap[k] = resK;
            return resK;
        }
    }
};
// 递归是一种从高向低的计算方法，可以考虑倒过来用for循环实现
// for循环逻辑一样，但是没有那么多的递归出入栈，消耗的时间少很多。
class Solution {
public:
    int rob(vector<int> &nums) {
        if (nums.empty()) {return 0;}
        if (nums.size() == 1) {
            return nums.front();
        }
        if (nums.size() == 2) {
            return max(nums[0], nums[1]);
        }
        int k_2_res= nums.front();
        int k_1_res = max(nums[0], nums[1]);
        int maxNow;
        for (int i= 2; i<nums.size(); i++) {
//            cout << "r1:" << r1 << "r2:" << r2 << "maxNow:" << maxNow << endl;
            maxNow= max(nums[i]+k_2_res, k_1_res);
            k_2_res = k_1_res;
            k_1_res = maxNow;
        }
        return maxNow;
    }
private:
        vector<int> tmp{};
};

int main() {
    vector<int> nums{2, 7, 9, 3, 1};
    Solution solution{};
    auto res = solution.rob(nums);
    cout << res << endl;
    return 0;
}