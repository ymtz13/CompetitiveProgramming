#include<iostream>
using namespace std;
#define ll long long

int main(){
  ll N, M;
  cin >> N >> M;
  ll K = 1<<N;
  
  ll dp[K][M+1];
  for(ll k=0; k<K; ++k) for(ll m=0; m<M+1; ++m) dp[k][m] = (k>0) ? LLONG_MAX : 0;

  for(ll m=0; m<M; ++m){
    ll a, b;
    cin >> a >> b;

    ll x=0, c;
    for(ll i=0; i<b; ++i){
      cin >> c;
      x += 1<<(c-1);
    }

    for(ll k=0; k<K; ++k){
      dp[k][m+1] = dp[k][m];
    }
      
    for(ll k=0; k<K; ++k){
      if(dp[k][m]!=LLONG_MAX){
        dp[k|x][m+1] = min(dp[k|x][m+1], dp[k][m]+a);
      }
    }
  }

  if(dp[K-1][M]!=LLONG_MAX){
    cout << dp[K-1][M] << endl;
  }else{
    cout << -1 << endl;
  }
  

  return 0;
}
