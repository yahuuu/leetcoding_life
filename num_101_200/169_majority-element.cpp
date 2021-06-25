// Created by alex on 2021/6/25.
// https://leetcode-cn.com/problems/majority-element/submissions/

#include <vector>
#include <map>
#include <iostream>

using namespace std;
typedef std::map<int, int> MapIntInt;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        vectorSize = nums.size();
        vector<int>::const_iterator iter;
        for ( iter = nums.begin(); iter != nums.end(); iter++) {
            mapInt[*iter] += 1;
            if (mapInt[*iter] > vectorSize / 2)
                maxEle = *iter;
        }
        return maxEle;
    }
private:
    MapIntInt  mapInt;
    int maxCount;
    int maxEle;
    int vectorSize;
};


int main() {
    vector<int> vec{3, 3, 2};
    Solution solu;
    int maxEle = solu.majorityElement(vec);
    cout << maxEle << endl;
}