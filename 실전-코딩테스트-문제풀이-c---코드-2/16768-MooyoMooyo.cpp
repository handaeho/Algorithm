#include <bits/stdc++.h>
using namespace std;

const int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};
int N, K, grid[105][12];
bool ck[105][12], ck2[105][12];

int dfs1(int x, int y){
    int ret = 1;
    ck[x][y] = true;
    for(int i = 0 ; i < 4 ; i++){
        int xx = x + dx[i], yy = y + dy[i];
        if(!xx||xx>N||!yy||yy>10||ck[xx][yy]) continue;
        if(grid[xx][yy] == grid[x][y]) ret += dfs1(xx, yy);
    }
    return ret;
}

void dfs2(int x, int y){
    ck2[x][y] = true;
    for(int i = 0 ; i < 4 ; i++){
        int xx = x + dx[i], yy = y + dy[i];
        if(!xx||xx>N||!yy||yy>10||ck2[xx][yy]) continue;
        if(grid[xx][yy] == grid[x][y]) dfs2(xx, yy);
    }
    grid[x][y] = 0;
}

void down(){
    for(int i = 1 ; i <= 10 ; i++){
        vector<int> tmp;
        for(int j = 1 ; j <= N ; j++) if(grid[j][i]) tmp.push_back(grid[j][i]);
        for(int j = 1 ; j <= N-tmp.size() ; j++) grid[j][i] = 0; 
        for(int j = 0 ; j < tmp.size() ; j++) grid[N-tmp.size()+j+1][i] = tmp[j]; 
    }
}

int main(){
    scanf("%d %d",&N, &K);
    for(int i = 1 ; i <= N ; i++) for(int j = 1 ; j <= 10 ; j++) scanf("%1d",&grid[i][j]);

    while(true){
        bool exist = true;
        memset(ck, false, sizeof(ck));
        memset(ck2, false, sizeof(ck2));
        for(int i = 1 ; i <= N ; i++){
            for(int j = 1 ; j <= 10 ; j++){
                if(ck[i][j]||!grid[i][j]) continue;
                int ret = dfs1(i, j);
                if(ret>=K){
                    dfs2(i, j);
                    exist = false;
                }
            }
        }
        if(exist) break;
        down();
    }  

    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= 10 ; j++) printf("%d",grid[i][j]);
        puts("");
    }
}