#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int N; cin >> N;
    vector<int> v(N);
    for(int i = 0 ; i < N ; i++) cin >> v[i];
    sort(v.begin(), v.end());
    int ans = 0;
    for(auto i : v){
        if(i <= ans+1) ans += i;
        else break;
    }
    cout << ans+1;
}