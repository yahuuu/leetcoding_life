#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/30
# @Author  : yahuuu

#include <vector>
#include <iostream>
#include <queue>

using namespace std;
/*
struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
*/
class Solution {
public:
    ListNode *reverseBetween(ListNode *head, int left, int right) {
        if (head->next == nullptr || left == right) {
            return head;
        }
        int i = 0;
        ListNode *ptr = head;
        if (left > 0) {
            for (; i < left - 1; i++) {
                que_m.push(ptr);
                ptr = ptr->next;
            }
        }
        for (; i < right; i++) {
            vec_.push_back(ptr);
            ptr = ptr->next;
        }
        while (ptr) {
            que_m.push(ptr);
            ptr = ptr->next;
        }
        // rebuild
        ListNode *newHeader = nullptr;
        if (left > 1) {
            newHeader = que_m.front();
            que_m.pop();
        } else {
            newHeader = vec_.back();
            vec_.pop_back();
        }
        ptr = newHeader;
        int j = 1;
        for (; j < left-1; j++) {
            ptr->next = que_m.front();
            que_m.pop();
            ptr = ptr->next;
        }
        while (!vec_.empty()) {
            ptr->next = vec_.back();
            vec_.pop_back();
            ptr = ptr->next;
        }
        while (!que_m.empty()) {
            ptr->next = que_m.front();
            que_m.pop();
            ptr = ptr->next;
        }
        ptr->next = nullptr;
        return newHeader;
    }

private:
    queue<ListNode *> que_m;
    vector<ListNode *> vec_;
};

/*
int main() {
    ListNode header = ListNode(1);
    ListNode *ptr = &header;
    for (int i = 2; i < 6; i++) {
//        ListNode newNode = ListNode(i); // 之前在这里写了个bug，一直使用局部的变量。
        ptr->next = new ListNode(i);
        ptr = ptr->next;
    }
    Solution solution{};
    ptr = solution.reverseBetween(&header, 1, 5);
    while (ptr) {
        cout << ptr->val << " " ;
        ptr = ptr->next;
    }
    return 0;
}
*/