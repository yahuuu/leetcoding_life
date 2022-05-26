#include <iostream>
#include <set>
#include <stack>
#include <vector>

using namespace std;

class Solution1 {
public:
    void rotate(vector<int> &nums, int k) {
        int len = nums.size();
        int begins = (k) % len;
        vector<int> tmp{};
        for (int i = len - begins; i < len; i++) {
            tmp.push_back(nums[i]);
        }
        for (int i = 0; i < len - begins; i++) {
            tmp.push_back(nums[i]);
        }
        nums = tmp;
    }
};

class Solution2 {
public:
    void rotate(vector<int> &nums, int k) {
        int len = nums.size();
        int kk = k % len;
        int tmp;
        for (int i = 0; i < kk; i++) {
            tmp = nums.back();
            for (int j = len - 2; j >= 0; j--) {
                nums[j + 1] = nums[j];
            }
            nums[0] = tmp;
        }
    }
};


int main() {
    vector<int> nums = {1, 2, 3, 4};
    int k = 2;
    Solution1 solution{};
    solution.rotate(nums, k);
    for (auto ele : nums) {
        cout << ele << endl;
    }
    return 0;
}
