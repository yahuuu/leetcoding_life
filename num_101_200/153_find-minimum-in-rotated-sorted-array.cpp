// 这里的logN的方法不多，基本是二分法。

class Solution {
private:
    int helper(vector<int> &nums, int l, int r) {
        if (r-1 == l) {
            return min(nums[l], nums[r]);
        }
        if (r -2 == l) {
            return min(min(nums[l], nums[l+1]), nums[r]);
        }
        return 0;
    }

    int binarySearch(vector<int> &nums, int l, int r) {
        if (l + 1 == r || l + 2 == r) {
            return helper(nums, l, r);
        }
        int mid = (l + r) / 2;
        if (nums[mid] < nums.front()) {
            return binarySearch(nums, l, mid);
        } else if (nums[mid] > nums.back()) {
            return binarySearch(nums, mid, r);
        }
        return 0;
    }

public:
    int findMin(vector<int> &nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        if (nums.front() < nums.back()) {
            return nums[0];
        }
        auto res = binarySearch(nums, 0, nums.size() - 1);
        return res;
    }
};