#include<iostream>
#include<vector>
using namespace std;
#define ll long long

int main(){
  ll H, N;
  cin >> H >> N;

  vector<ll> A(N), B(N);
  for(ll i=0; i<N; ++i) cin >> A[i] >> B[i];

  ll M = H+10010;
  ll INF = 1000000000;
  vector<ll> dp(M, INF);
  dp[0] = 0;
  for(ll x=1; x<M; ++x) {
    for(ll j=0; j<N; ++j) {
      if(x-A[j]<0) continue;
      dp[x] = min(dp[x], dp[x-A[j]]+B[j]);
    }
  }

  ll ans = INF;
  for(ll x=H; x<M; ++x) ans = min(ans, dp[x]);
  cout << ans << endl;

}
