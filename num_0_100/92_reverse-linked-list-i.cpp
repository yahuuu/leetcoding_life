// @Time    : 2025/2/12
// @Author  : yahuuu


#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public:
        ListNode *reverseBetween(ListNode *head, int left, int right) {
            if (left == right) return head;
            ListNode fackNode = ListNode(-1) ;
            fackNode.next = head;
            ListNode *p = &fackNode;
            ListNode *c = head;
            ListNode *n = head->next;
            int num = 1;

            while (num < left) {
                p = c;
                c = n;
                n = n->next;
                num ++;
            }
            ListNode *record1 = p;
            ListNode *leftNode = c;
            while (num < right) {
                p = c;
                c = n;
                n = n->next;
                c->next = p;
                num ++;
            }
            leftNode->next = n;
            c->next = p;
            record1->next = c;
            return fackNode.next;
        }
};

void printList(ListNode* cur) {
    while (cur!= nullptr) {
        cout << cur->val<< endl;
        cur= cur->next;
    }
}

int main20250212() {
    ListNode node4 = ListNode(14, nullptr);
    ListNode node3 = ListNode(13, &node4);
    ListNode node2 = ListNode(12, &node3);
    ListNode node1 = ListNode(11, &node2);
    ListNode* head = &node1;
    Solution solu;
    ListNode* cur = solu.reverseBetween(head, 1, 4);
    printList(cur);
}

#endif //CTHINK_REVERSELIST_HPP
