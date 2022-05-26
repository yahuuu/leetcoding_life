#include <iostream>
#include <set>
#include <stack>
#include <vector>
#include <string>

using namespace std;

class Solution {
private:
    typedef enum RETNUM {
        BIG = 1,
        EQUAL = 0,
        SMALL = -1
    }RETNUM;
public:
    int compareVersion(string version1, string version2) {
        string tmp = "";
        int l = 0;
        int r=0;
        for (; r<version1.size(); r++) {
            if (version1[r] == '.') {
                tmp = version1.substr(l, r-l);
                t1.push_back(stoi(tmp));
                l = r+1;
            }
        }
        tmp= version1.substr(l, r-l);
        t1.push_back(stoi(tmp));
        l = 0;
        for (r=0; r<version2.size(); r++) {
            if (version2[r] == '.') {
                tmp = version2.substr(l, r-l);
                t2.push_back(stoi(tmp));
                l = r+1;
            }
        }
        tmp = version2.substr(l, r-l);
        t2.push_back(stoi(tmp));
        int maxVectorLen = max(t1.size(), t2.size());
        for (int i=0; i<maxVectorLen; i++) {
            if (getSubVersion(t1, i) > getSubVersion(t2, i)) {
                return BIG;
            }
            if (getSubVersion(t1, i) < getSubVersion(t2, i)) {
                return SMALL;
            }
        }
        return EQUAL;
    }
private:
    vector<int> t1{}, t2{};
private:
    int getSubVersion(vector<int> &t, int idx) {
        if (idx > t.size()-1 ) {
            return 0;
        }
        return t[idx];
    }
};

int main() {
    string s1 = "1.1.2";
    string s2 = "2";
    Solution solution{};
    auto res = solution.compareVersion(s1, s2);
    cout << res << endl;
    return 0;
}