#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int> &nums) {
        for (auto ele: nums) {
            int tmp = umap.count(ele);
            if (tmp == 0) {
                umap.emplace(ele, 1);
                continue;
            }
            umap[ele] += 1;
        }
        int res = 0;
        for (pair<const int, int> ele: umap) {
            if (ele.second == 1) {
                res = ele.first;
            }
        }
        return res;
    }
private:
    unordered_map<int, int> umap;
};
