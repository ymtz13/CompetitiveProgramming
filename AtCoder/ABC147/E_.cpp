#include<iostream>
#include<vector>
#include<set>
using namespace std;
#define ll long long
#define MAX 15000

int main(){
  ll H, W;
  cin >> H >> W;
  vector<ll> row(W);
  vector<vector<ll>> M(H, row);

  
  vector<bool> dp2(MAX, false);
  vector<vector<bool>> dp1(W, dp2);
  vector<vector<vector<bool>>> dp(H, dp1);
  
  for(ll h=0; h<H; ++h) for(ll w=0; w<W; ++w) cin >> M[h][w];

  
  ll B;
  for(ll h=0; h<H; ++h) for(ll w=0; w<W; ++w) {
    cin >> B;
    M[h][w] = abs(M[h][w]-B);
  }

  /*
  for(ll h=0; h<H; ++h){
    for(ll w=0; w<W; ++w) cout << M[h][w] << " "; cout<<endl;
  }
  */

  dp[0][0][M[0][0]] = true;
  for(ll h=0; h<H; ++h) for(ll w=0; w<W; ++w) {
    vector<bool>& pn = dp[h][w];
    ll v = M[h][w];
      
    if(h>0){
      vector<bool>& pp = dp[h-1][w];
      for(ll i=0; i<MAX; ++i) if(pp[i]) pn[i+v] = pn[abs(i-v)] = true;
    }
    if(w>0){
      vector<bool>& pp = dp[h][w-1];
      for(ll i=0; i<MAX; ++i) if(pp[i]) pn[i+v] = pn[abs(i-v)] = true;
    }
  }

  ll ans=0;
  for(; !dp[H-1][W-1][ans]; ++ans);
    
  cout << ans << endl;
  return 0;
}
