class Solution {
public:
    vector<int> grayCode(int n) {
        if (n == 1) {
            return code1;
        }
        for (int i = 1; i < n; i++) {
            int vectorSize = code1.size();
            vector<int> tmp = code1;
            int addFactor = (1 << i);
            for (int j = vectorSize - 1; j > -1; j--) {
                code1.push_back(tmp[j] + addFactor);
            }
        }
        return code1;
    }

private:
    vector<int> code1 = {0, 1};
};


int binaryFunc(int chushu) {
    int yushu = 0;
    int i = 0;
    int result = 0;
    for (; chushu != 0;) {
        yushu = chushu % 2;
        chushu /= 2;
        result += (yushu * pow(10, i));
        i++;
    }
    return result;
}