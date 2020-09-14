#include<iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

namespace sametreespace {

    class Solution {
    public:
        Solution(){
        srand(time(NULL));
        }
        bool isSameTree(TreeNode *p, TreeNode *q) {
    //        if (random()%2){
        if (1){
            return isSameTree1(p, q);
        }
    //        return isSameTree2(p, q);
        }

        bool isSameTree1(TreeNode *p, TreeNode *q) {
        if(!p && !q) return true;
        if(!p || !q) return false;
        if(p->val != q->val) return false;
        return (isSameTree(p->left, q->left) &&
            isSameTree(p->right, q->right));
        }
    //    bool isSameTree2(TreeNode *p, TreeNode *q) {
    //        queue<TreeNode*> q1, q2;
    //        q1.push(p);
    //        q2.push(q);
    //        while (q1.size()>0 && q2.size()>0 ){
    //            TreeNode* p1 = q1.front();
    //            q1.pop();
    //            TreeNode* p2 = q2.front();
    //            q2.pop();
    //            if (!p1 && !p2) continue;
    //            if (!p1 || !p2)  return false;
    //            if ( p1->val != p2->val) {
    //                return false;
    //            }
    //            q1.push(p1->left);
    //            q2.push(p2->left);
    //            q1.push(p1->right);
    //            q2.push(p2->right);
    //        }
    //        return true;
    //    }
    };
};


void sameTreeMain(void){
    TreeNode root1(1);
    TreeNode root2(1);
    TreeNode t2(2);
    TreeNode t3(3);
    TreeNode t4(4);
    TreeNode t5(5);

    root1.left = &t2;
    root1.right = &t3;
    root2.left = &t2;
    root2.right = &t3;
    t2.left = &t4;
    t2.right = &t5;
    sametreespace::Solution solu;
    std::cout << solu.isSameTree(&root1, &root2) << std::endl;
}
