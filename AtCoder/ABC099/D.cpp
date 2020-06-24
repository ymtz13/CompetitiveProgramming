#include<iostream>
#include<map>
#include<vector>
using namespace std;
#define ll long long

int main() {
  ll N, C;
  cin >> N >> C;

  vector<vector<ll>> D(C+1);
  for(ll i=1; i<C+1; ++i) {
    vector<ll> row(C+1, 0);
    for(ll j=1; j<C+1; ++j) cin >> row[j];
    D[i] = row;
  }

  vector<map<ll, ll>> E(3);
  for(ll i=0; i<N; ++i){
    for(ll j=0; j<N; ++j){
      ll c;
      cin >> c;
      map<ll, ll>& e = E[(i+j)%3];
      if(e.find(c)!=e.end()) {++e[c];} else {e[c]=1;}
    }
  }

  ll ans = 10000000000;
  
  for(ll c1=1; c1<=C; ++c1)
  for(ll c2=1; c2<=C; ++c2)
  for(ll c3=1; c3<=C; ++c3) {
    if (c1==c2 || c2==c3 || c3==c1) continue;

    ll cost = 0;

    for(auto itr = E[0].begin(); itr!=E[0].end(); ++itr)  cost += D[itr->first][c1] * (itr->second);
    for(auto itr = E[1].begin(); itr!=E[1].end(); ++itr)  cost += D[itr->first][c2] * (itr->second);
    for(auto itr = E[2].begin(); itr!=E[2].end(); ++itr)  cost += D[itr->first][c3] * (itr->second);
    
    if(cost < ans) ans = cost;

  }

  cout << ans << endl;

  return 0;
}
