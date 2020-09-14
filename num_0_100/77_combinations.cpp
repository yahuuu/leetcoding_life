#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <vector>
//#include <algorithm>

using namespace std;

void getCombination(int n, int k, int idx, int layers, vector<int>& solution,
                    vector< vector<int> >& result );
vector<vector<int> > combine1(int n, int k);

vector<vector<int> > combine(int n, int k) {
    cout << "recusive method!" << endl;
    return combine1(n, k);
}

vector<vector<int> > combine1(int n, int k) {
    vector<vector<int> > result;
    vector<int> solution;
    int idx = 1;
    int layers = 0;
    getCombination(n, k, idx, layers, solution, result);
    return result;
}

void getCombination(int n, int k, int idx, int layers, vector<int>& solution,
                    vector< vector<int> >& result ){
    if (layers==k){
        vector<int> v = solution;
        result.push_back(v);
        return;
    }
    for(int i=idx; i<n+1; i++){
        solution.push_back(i);
        layers += 1;
        getCombination(n, k, i+1, layers, solution, result);
        solution.pop_back();
        layers -= 1;
    }
}

void printResult(vector<vector<int> >& result){
    for(uint i=0; i<result.size(); i++){
        cout << "{";
        for(uint j=0; j<result[i].size(); j++){
            cout << " " << result[i][j];
        }
        cout << " }" <<endl;
    }
}

int main_combinations(void){
    srand(time(NULL));
    int n = 4, k =2;
    vector<vector<int> > r = combine(n, k);
    printResult(r);
    return 0;
}
