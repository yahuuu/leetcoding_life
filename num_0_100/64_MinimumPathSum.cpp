#include<iostream>
#include<vector>
//#include<limits.h>

using namespace std;


class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        for(int i=1; i<row; i++){
            grid[i][0] += grid[i-1][0];
        }
        for(int j=1; j<col; j++){
            grid[0][j] += grid[0][j-1];
        }
        for(int i=1; i<row; i++){
            for(int j=1; j<col; j++){
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        return grid[row-1][col-1];
    }
};

int main(void){
    int a[3][3] = {{1,3,1},
                   {1,5,1},
                   {4,2,1}};
    vector< vector<int> > grid;
    for(int i=0; i<3; i++){
        vector<int> v;
        for(int j=0; j<3; j++){
            v.push_back(a[i][j]);
        }
        grid.push_back(v);
    }
    Solution  solu ;
    int minPathSum = solu.minPathSum(grid);
    cout << minPathSum << endl;
    return 0;
}











