#include<iostream>
#include<vector>
using namespace std;
#define ll long long
#define INF 999999999999999999

int main(){
  ll N, M, R;
  cin >> N >> M >> R;

  vector<ll> r(N);
  for(ll i=0; i<R; ++i) cin >> r[i];

  vector<ll> row(N, INF);
  vector<vector<ll>> D(N, row);

  ll A, B, C;
  for(ll m=0; m<M; ++m) {
    cin >> A >> B >> C;
    D[A-1][B-1] = D[B-1][A-1] = C;
  }

  // for(ll i=0; i<N; ++i){
  //   for(ll j=0; j<N; ++j) cout << D[i][j] << " ";  cout<<endl;
  // }

  
  for(ll k=0; k<N; ++k)
  for(ll j=0; j<N; ++j)
  for(ll i=j+1; i<N; ++i)
    D[i][j] = D[j][i] = min(D[i][j], D[i][k]+D[k][j]);

  // for(ll i=0; i<N; ++i){
  //   for(ll j=0; j<N; ++j) cout << D[i][j] << " ";  cout<<endl;
  // }
  
  ll ans = INF;
  vector<ll> stack(100, -1);
  vector<bool> remove(100, false);
  ll nstack = R;
  for(ll ir=0; ir<R; ++ir) stack[ir]=ir;
  
  vector<bool> visited(R, false);
  vector<ll> path(R);
  ll npath = 0;

  while(nstack>0) {
    //for(ll j=0; j<nstack; ++j) cout << stack[j] << " "; cout << endl;
    
    ll ir = stack[nstack-1];
    if(remove[nstack-1]) {
      visited[ir] = false;
      --npath;
      --nstack;
      continue;
    }
    path[npath++] = ir;
    visited[ir] = true;
    remove[nstack-1] = true;
    for(ll i=0; i<R; ++i) if(!visited[i]) {
        stack[nstack] = i;
        remove[nstack] = false;
        ++nstack;
    }

    
    if(npath==R){
      ll dist = 0;
      for(ll i=0; i<R-1; ++i) dist += D[r[path[i]]-1][r[path[i+1]]-1];
      ans = min(ans, dist);
    }
    
  }

  cout << ans << endl;
  
  return 0;
}
