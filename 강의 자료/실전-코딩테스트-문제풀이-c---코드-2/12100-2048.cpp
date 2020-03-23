#include <bits/stdc++.h>
using namespace std;

int N; 
vector<vector<int>> Board;

vector<vector<int>> rotate90(vector<vector<int>> B){
    vector<vector<int>> NB(N, vector<int>(N,0));
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            NB[j][N-i-1] = B[i][j];
        }
    }
    return NB;
}

vector<int> convert(vector<int> lst){
    vector<int> new_list, new_list2;
    for(auto i : lst) if(i) new_list.push_back(i);
    for(int i = 1 ; i < new_list.size() ; i++){
        if(new_list[i-1] == new_list[i]){
            new_list[i-1] *= 2;
            new_list[i] = 0;
        }
    }
    for(auto i : new_list) if(i) new_list2.push_back(i);
    // 길이를 맞추는 부분
    for(int i = 0 ; new_list2.size() != N ; i++) new_list2.push_back(0);
    return new_list2;
}

int dfs(vector<vector<int>> B, int count){
    int ret = 0;
    // max는 반복문으로
    for(int i = 0 ; i < N*N ; i++) ret = max(ret, B[i/N][i%N]);
    if(!count) return ret;
    for(int i = 0 ; i < 4 ; i++){
        vector<vector<int>> X(N);
        for(int j = 0 ; j < N ; j++) X[j] = convert(B[j]);
        if (X != B) ret = max(ret, dfs(X, count-1));
        B = rotate90(B);
    }
    return ret;
}

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> N;
    // vector 초기화는 알아둘것
    Board.resize(N, vector<int>(N,0));
    for(int i = 0 ; i < N ; i ++){
        for(int j = 0 ; j < N ; j++) cin >> Board[i][j];
    }
    cout << dfs(Board, 5);
}