#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(0); cin.tie(0);
  string a; cin >> a;
  string c;
  if(a.size() == 1){ 
      cout << 1;
      return 0;
  }
  for(int i = 0 ; i < a.size() ; i++) c += '1';
  if(c<=a) cout << a.size();
  else cout << a.size()-1;
}
