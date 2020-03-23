#include <bits/stdc++.h>
using namespace std; 

int DP[305][305];

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int N, M; cin >> N >> M;
    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= M ; j++){
            int x; cin >> x;
            DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + x; 
        }
    }
    int k; cin >> k;
    while(k--){
        int a, b, c, d; cin >> a >> b >> c >> d;
        cout << DP[c][d] - DP[a-1][d] - DP[c][b-1] + DP[a-1][b-1] << '\n';
    }
}