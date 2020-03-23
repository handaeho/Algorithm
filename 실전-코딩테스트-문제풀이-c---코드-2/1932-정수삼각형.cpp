#include <bits/stdc++.h>
using namespace std; 

int A[1005][1005];

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int N; cin >> N;
    // 입력과 동시에 DP 처리
    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= i ; j++){
            int x; cin >> x;
            A[i][j] = max(A[i-1][j-1], A[i-1][j]) + x;
        }
    }
    // python의 max함수와 거의 유사
    cout << *max_element(A[N]+1, A[N]+N+1);
}