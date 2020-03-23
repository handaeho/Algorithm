#include <bits/stdc++.h>
using namespace std;

int P[100];
priority_queue<int, vector<int>, greater<int>> PQ;

int main(){
    int K, N; cin >> K >> N;
    for(int i = 0; i < K; i++){
        cin >> P[i];
        PQ.push(P[i]);
    }

    int prev = -1;
    for(int i = 0; i < N-1 ; i++){
        int curr = PQ.top(); PQ.pop();
        for(int j = 0 ; j < K ; j++){
            long long temp = 1LL * curr * P[j];
            if(temp < (1LL<<31)) PQ.push(temp);
            else break;
        }
        prev = curr;
        while(prev == PQ.top()) PQ.pop();
    }
    cout << PQ.top();
}