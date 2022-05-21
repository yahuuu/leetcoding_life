class Solution {
public:
    void sortColors(vector<int> &nums) {
        for (auto ele : nums) {
            if (tmp.empty()) {
                tmp.push(ele);
                continue;
            }
            stack<int> tmp1;
            while (!tmp.empty() && ele > tmp.top()) {
                tmp1.push(tmp.top());
                tmp.pop();
            }
            tmp.push(ele);
            while (!tmp1.empty()) {
                tmp.push(tmp1.top());
                tmp1.pop();
            }
        }
        vector<int> res;
        int len = tmp.size();
        for(int i=0;i<len;i++) {
            res.push_back(tmp.top());
            tmp.pop();
        }
        nums = res;
        cout<< endl;
    }
private:
    stack<int> tmp;
};
