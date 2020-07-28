#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<vector>

using namespace std;


class Solution
{
public:
    vector<int> plusOne(vector<int>& digits)
    {
        int num=1;
        for(int i=digits.size()-1; i>=0; i--){
           num += digits[i];
           digits[i]=num%10;
           num/=10;
           if(!num){
               break;
           }

        }
        if(num==1)
        {
            digits.resize(digits.size()+1, 0);
            digits[0]=1;
        }
        return digits;
    }
};


int main(){
    vector<int> v ;
    v.push_back(1);
    v.push_back(3);
    v.push_back(2);
    v.push_back(4);
    Solution stu;
    vector<int> vec = stu.plusOne(v);

    for(uint i=0; i<vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << endl;
    return 0;
}
