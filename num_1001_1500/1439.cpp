// 还是剪枝暴力法
//

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int kthSmallest(vector<vector<int>> &mat, int k) {
        int col = mat[0].size();
        int row = mat.size();
        vector<int> vec = mat[0];
        for (int r = 1; r < row; ++r) {
            vector<int> tmpVector = {};
            for (int j = 0; j < vec.size(); ++j) {
                for (int c = 0; c < col; ++c) {
                    tmpVector.emplace_back(vec[j] + mat[r][c]);
                }
            }
            sort(tmpVector.begin(), tmpVector.end());
//            vec.assign(tmpVector.begin(), tmpVector.begin()+min(k, (int)tmpVector.size()));
            vec = vector<int>(tmpVector.begin(), tmpVector.begin() + min(k, (int) tmpVector.size()));
        }
        return vec[k - 1];
    }
};

//
//int main() {
//    int k = 7;
//    vector<vector<int>> mat = {{1, 10, 10},
//                               {1, 4,  5},
//                               {2, 3,  6}};
//    Solution solution = Solution();
//    int res = solution.kthSmallest(mat, k);
//    cout << res << endl;
//    return 0;
//}