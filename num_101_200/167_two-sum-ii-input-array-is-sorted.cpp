//
// Created by yahuuu on 2021/7/4.
//

#include <vector>
#include <iostream>

using std::vector;
using std::cout;
using std::endl;
using iter = vector<int>::const_iterator ;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
//        if (numbers.size() == 2 && numbers)
//        }
        for (iter it=numbers.begin(); it != numbers.end(); it++) {
            if (*it > target)
                return vector<int> {};
            bool rlt = binaryS(numbers, idx, target);
            if (rlt) {
                return vector<int> {idx+1, mid+1};
            }
            idx += 1;
        }
        return {-1, -1};
    }
private:
    int left;
    int right;
    int idx=0;
    int mid;
    bool binaryS(vector<int> vec, int idx, int target) {
        left = idx+1;
        right = vec.size()-1;
        while (left <= right) {
            mid = (left + right) / 2;
            if (vec[mid] == target-vec[idx]) {
                return true;
            } else if (vec[mid] < target-vec[idx]) {
                left = mid+1;
            } else if (vec[mid] > target-vec[idx])
                right = mid-1;
        }
        return false;
    }
};

int main() {
   vector<int> vec = {1,2,3,4,4,9,56,90};
   Solution solu;
   vector<int> result =  solu.twoSum(vec, 8);
   cout << result[0] << "," << result[1] << endl;
}