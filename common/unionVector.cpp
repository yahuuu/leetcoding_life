#include<iostream>
#include<vector>
#include <cstring>
#include <set>
#include <algorithm>
#include <iterator>
#include <unistd.h>
using namespace std;

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define VERTICES 6
int find_root(int x, int parent[])  // 找到根节点
{
    int x_root = x;
    while (parent[x_root] != -1)
    {
        x_root = parent[x_root];
    }
    return x_root;
}
int union_vertices(int x, int y, int parent[])  // 让两个集合合并
{
    int x_root = find_root(x, parent);
    int y_root = find_root(y, parent);
    if (x_root == y_root)
        return 0;
    else
    {
        parent[x_root] = y_root;
        return 1;
    }
}
int main(void)
{
    int parent[VERTICES] = { 0 };
    memset(parent, -1, sizeof(parent));   // 初始化
    int edges[5][2] = { {0,1},{1,2},{1,3},{2,4},{3,5} }; // 边集

    for (int i = 0; i < 5; i++)
    {
        int x = edges[i][0];
        int y = edges[i][1];
        if (union_vertices(x, y, parent) == 0)
        {
            printf("Cycle detected!\n");
            exit(0);
        }
    }
    printf("No cycle found.\n");

    system("pause");
    return 0;
}