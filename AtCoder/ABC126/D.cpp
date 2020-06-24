#include<iostream>
#include<vector>
using namespace std;
#define ll long long

vector<vector<ll>> e;
vector<vector<ll>> dist;
vector<ll> d;

void dfs(ll i, ll _d) {
  d[i] = _d;
  for(ll ic=0; ic<e[i].size(); ++ic){
    ll c = e[i][ic];
    if(d[c]!=-1) continue;
    dfs(c, _d+dist[i][c]);
  }
}

int main(){
  ll N, buf;
  cin >> N;
  for(ll i=0; i<N; ++i) {
    vector<ll> x,y;
    e.push_back(x);
    dist.push_back(y);
    for(ll j=0; j<N; ++j) dist[i].push_back(-1);
    d.push_back(-1);
  }

  for(ll i=0; i<N-1; ++i){
    ll u, v, w;
    cin >> u >> v >> w;
    e[u-1].push_back(v-1);
    e[v-1].push_back(u-1);
    dist[u-1][v-1] = dist[v-1][u-1] = w;
  }

  dfs(0,0);
  for(ll i=0; i<N; ++i) cout << d[i]%2 << endl;

  return 0;
}
