#include <iostream>
#include <unordered_map>
#include <memory>
#include <cmath>

using namespace std;

template <typename T>
class Helper {
private:
    T t_;
    unordered_map<T, int> umap;
public:
    Helper() = delete;
    explicit Helper(T t): t_(t) {
        }
    bool check() {
        while(t_ != 1 && !umap[t_]) {
            umap[t_] += 1;
            t_ = nextNumber(t_);
        }
        return t_ == 1;
    };
private:
    T nextNumber(T t){
        int n = 1;
        long long sum = 0;
        while (t>0) {
            int remainder = t % 10;
            t /= 10;
            sum += pow(remainder, 2);
        }
        return sum;
    }


};

class Solution {
private:
   shared_ptr<Helper<int>> ptrClass ;
public:
    bool isHappy(int n) {
       ptrClass = make_shared<Helper<int>>(n);
       auto res = ptrClass->check();
       return res;
    }
};

int main() {
    Solution solu;
    auto res = solu.isHappy(2);
    cout << boolalpha;
    cout << res << endl;
}