#include <bits/stdc++.h>
using namespace std;

int A[1005][1005];
int DP[1005][1005];

int mini(int a, int b, int c){ return min(min(a, b), c);}

int main(void){
    int n, m; scanf("%d %d",&n,&m);
    for(int i = 1; i <= n ;i++){
        for(int j = 1; j <= m ; j++) scanf("%1d", &A[i][j]); // 1자리씩 받기
    }

    int mx = 0;
    for(int i = 1; i <= n ;i++){
        for(int j = 1; j <= m ; j++){
            if(A[i][j]==1){
                // c++17에서는 min({})을 사용하면 됨
                DP[i][j] = 1 + mini(DP[i-1][j],DP[i][j-1],DP[i-1][j-1]); 
                mx = max(mx, DP[i][j]);
            }
        }
    }
    
    printf("%d",mx*mx);
}