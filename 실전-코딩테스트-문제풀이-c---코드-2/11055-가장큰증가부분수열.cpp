#include <bits/stdc++.h>
using namespace std; 

int A[1005], DP[1005];

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int N; cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> A[i];
        DP[i] = A[i];
    }
    for(int i = 1 ; i < N ; i++){
        for(int j = 0 ; j < i ; j++){
            if(A[i] > A[j]){
                DP[i] = max(A[i]+DP[j], DP[i]);
            }
        }
    }
    cout << *max_element(DP, DP+N);
}