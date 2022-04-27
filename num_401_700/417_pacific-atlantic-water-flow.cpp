#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/27
# @Author  : yahuuu



#include <vector>
#include <iostream>

using namespace std;

class Solution {
private:
    vector<vector<int>> heights;
    bool PacificFlag[200][200][2] = {false};
    int rows = 0;
    int cols = 0;

    void helper(int r, int c, int flagIndex, int lastVal) {
        if (r<0 || r>rows-1 || c<0 || c>cols-1) {
            return;
        }
        if (this->heights[r][c]<lastVal) {
            return;
        }
        this->PacificFlag[r][c][flagIndex] = true;
        int tmp = heights[r][c];
        this->heights[r][c] = -1;
        this->helper(r+1, c, flagIndex, tmp);
        this->helper(r-1, c, flagIndex, tmp);
        this->helper(r, c+1, flagIndex, tmp);
        this->helper(r, c-1, flagIndex, tmp);
    }

    vector<vector<int>> getDoubleFlagPoints() {
        vector<vector<int>> res{};
        for (int i = 0; i < rows; i++) {
            for (int j=0; j<cols; j++) {
                if (this->PacificFlag[i][j][0]==true&&this->PacificFlag[i][j][1]==true) {
                    res.push_back({i, j});
                }
            }
        }
        return res;
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>> &heights) {
        if (heights.empty()) {
            return vector<vector<int>>();
        }
        this->heights = heights;
        this->rows = heights.size();
        this->cols = heights[0].size();
//      left+up corner pacific ocean
        int defaultHeight = 0;
        for (int i = 0; i < cols; i++) {
            helper(0, i, 0, defaultHeight);
        }
        for (int i = 0; i < rows; i++) {
            helper(i, 0, 0, defaultHeight);
        }
        this->heights = heights; // 重新初始化，太平洋的岸边走过的路径已经置为-1，重新赋值高度。
//      right+down corner pacific ocean
        for (int i = 0; i < cols; i++) {
            helper(rows - 1, i, 1, defaultHeight);
        }
        for (int i = 0; i < rows; i++) {
            helper(i, cols - 1, 1, defaultHeight);
        }
        return getDoubleFlagPoints();

    }
};

/*
int main() {
    vector<vector<int>> heights = {{1, 2, 2, 3, 5},
                                   {3, 2, 3, 4, 4},
                                   {2, 4, 5, 3, 1},
                                   {6, 7, 1, 4, 5},
                                   {5, 1, 1, 2, 4}};
    vector<vector<int>> heights = {{2, 1},
                                   {1, 2}};
    Solution solu = Solution();
    auto points = solu.pacificAtlantic(heights);
    for(int r=0; r<points.size(); r++) {
        for (int c=0; c<2; c++) {
            std::cout << points[r][c] << " ";
        }
        std::cout << endl;
    }
    return 0;
}
 */