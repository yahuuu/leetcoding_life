#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>> &matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        set<int> rows_zero = {};
        set<int> cols_zero = {};
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    rows_zero.insert(i);
                    cols_zero.insert(j);
                }
            }
        }
        // 先处理行
        for (auto r : rows_zero) {
            for (int c = 0; c < cols; c++) {
                matrix[r][c] = 0;
            }
        }
        // 再处理列
        for (auto c : cols_zero) {
            for (int r = 0; r < rows; r++) {
                matrix[r][c] = 0;
            }
        }
        cout << endl;
    }
private:
};

int main(void) {
    vector<vector<int>> matrix = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
    Solution solution{};
    solution.setZeroes(matrix);
    return 0;
}

/*线程之间共享资源stdout*/