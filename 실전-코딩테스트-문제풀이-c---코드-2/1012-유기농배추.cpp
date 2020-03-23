#include <bits/stdc++.h>
using namespace std;

int B[52][52], ck[52][52];
int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};

void dfs(int x, int y){
    if(ck[x][y]) return;
    ck[x][y] = 1;
    for(int i = 0 ; i < 4 ; i++){
        int xx = x+dx[i], yy = y+dy[i];
        if(!B[xx][yy] || ck[xx][yy]) continue;
        dfs(xx, yy);

    } 
}

void process(){
    memset(B, 0, sizeof(B));
    memset(ck, 0, sizeof(ck));
    int M, N, K; cin >> M >> N >> K;
    while(K--){
        int x, y; cin >> x >> y;
        B[y+1][x+1] = 1;
    }
    int ans = 0;
    for(int i = 1 ; i <= N; i++){
        for(int j = 1 ; j <= M ; j++){
            if(!B[i][j] || ck[i][j]) continue;
            dfs(i, j);
            ans += 1;
        }
    }
    cout << ans << '\n';
}

int main() {
    // 빠른 입출력
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) process();
}