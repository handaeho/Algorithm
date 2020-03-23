#include <bits/stdc++.h>
using namespace std;
const int MX = 1e4;

int dx[4] = {1, 0, -1, 0}, dy[4] = {0, -1, 0, 1};

int arr_min(vector<vector<int>> v){
    int ret = MX;
    for(auto i : v){
        int tmp = 0;
        for(auto j : i) tmp += j;
        ret = min(tmp, ret);
    }
    return ret;
}

vector<vector<int>> rotate(vector<vector<int>> a, vector<int> q){
    int r = q[0], c = q[1], s = q[2];
    r--, c--;
    auto ret = a;
    for(int d = 1 ; d <= s ; d++){
        int rr = r-d, cc = c+d;
        for(int i = 0 ; i < 4 ; i++){
            for(int dd = 0 ; dd < 2*d ; dd++){
                ret[rr+dx[i]][cc+dy[i]] = a[rr][cc];
                rr += dx[i]; cc += dy[i];
            }
        }
    }
    return ret;
}

int dfs(vector<vector<int>> a, vector<vector<int>> q, int st, int k){
    if(st == (1<<k) -1) return arr_min(a);
    int ret = MX;
    for(int i = 0 ; i < k ; i++){
        if((st & (1 << i)) == 0) ret = min(ret, dfs(rotate(a, q[i]), q, st | 1<<i, k));
    }
    return ret;
}

int main(){
    int N, M, K; cin >> N >> M >> K;
    vector<vector<int>> A(N, vector<int>(M)), Q(K, vector<int>(3));
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++) cin >> A[i][j];
    }
    for(int i = 0 ; i < K ; i++){
        for(int j = 0 ; j < 3 ; j++) cin >> Q[i][j];
    }
    cout << dfs(A, Q, 0, K);
}