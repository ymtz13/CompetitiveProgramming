#include<iostream>
#include<vector>
using namespace std;
#define ll long long

ll N;
vector<ll> isVisited;
vector<vector<ll>> edge;

ll nodeid(ll x, ll y) { return min(x,y)*N+max(x,y); }

void visit(ll m) {
  if(isVisited[m]==-1) throw m;
  if(isVisited[m]>0) return;

  isVisited[m] = -1;
  ll layer=0;
  for(ll j=0; j<edge[m].size(); ++j){
    visit(edge[m][j]);
    layer = max(layer, isVisited[edge[m][j]]);
  }
  isVisited[m]=layer+1;
}

int main(){
  cin >> N;
  isVisited.resize(N*N, 0);
  edge.resize(N*N);
  
  for(ll i=0; i<N; ++i) {
    ll from, to;
    cin >> from;
    for(ll j=0; j<N-2; ++j) {
      cin >> to;
      edge[nodeid(i,from-1)].push_back(nodeid(i,to-1));
      from = to;
    }
  }

  for(ll i=0; i<edge.size(); ++i) {
    if(edge[i].size()==0) continue;
    cout << "(" << i/N+1 << "," << i%N+1 << ") ---> ";
    for(ll j=0; j<edge[i].size(); ++j) cout << "(" << edge[i][j]/N+1 << "," << edge[i][j]%N+1 << ")";
    cout << endl;
  }
  
  try{
    for(ll i=0; i<edge.size(); ++i) {
      if(edge[i].size()==0) continue;
      if(isVisited[i]==0) { visit(i); }
    }

  ll ans = 0;    
    for(ll i=0; i<edge.size(); ++i) {
      if(edge[i].size()==0) continue;
      ans = max(isVisited[i],ans);
    }
    cout << ans << endl;
    
  }catch(ll& e){
    cout << -1 << endl;
  }

  return 0;
}
