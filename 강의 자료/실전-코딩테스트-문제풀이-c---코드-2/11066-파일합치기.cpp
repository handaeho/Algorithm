#include <bits/stdc++.h>
using namespace std;

int a[501], s[501], d[501][501];

// 재귀 풀이
int go(int i, int j) {
    if (i == j) return 0;
    if (d[i][j] != -1) return d[i][j];
    int &ans = d[i][j];
    for (int k=i; k<=j-1; k++) {
        int temp = go(i, k) + go(k+1, j) + s[j] - s[i-1]; // 점화식
        if (ans == -1 || ans > temp) ans = temp;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--){
        // 배열 초기화
        memset(d,-1,sizeof(d));
        memset(s,0,sizeof(s));
        int n; cin >> n;
        for (int i = 1 ; i <=n ; i++) {
            cin >> a[i];
            s[i] = s[i-1] + a[i];
        }
        cout << go(1, n) << '\n';
    }
}