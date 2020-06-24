#include<iostream>
#include<vector>
using namespace std;
#define ll long long

vector<vector<ll>> E;
vector<ll> X;

void dfs(ll i, ll par){
  X[i] += X[par];
  for(int j=0; j<E[i].size(); ++j){
    if(E[i][j] == par) continue;
    dfs(E[i][j], i);
  }
}

int main(){
  ll N, Q;
  cin >> N >> Q;

  for(int i=0; i<=N; ++i){
    E.emplace_back();
    X.emplace_back(0);
  }
  
  for(int i=0; i<N-1; ++i){
    ll a, b;
    cin >> a >> b;
    E[a].emplace_back(b);
    E[b].emplace_back(a);
  }

  for(int i=0; i<Q; ++i){
    ll p, x;
    cin >> p >> x;
    X[p] += x;
  }

  dfs(1,0);
  for(int i=1; i<=N; ++i) cout << X[i] << " ";
  cout << endl;
  
  return 0;
}
