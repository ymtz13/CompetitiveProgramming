#include<iostream>
#include<vector>
using namespace std;
#define ll long long

int main(){
  ll N, K;
  cin >> N >> K;
  vector<ll> A(N);
  for(ll i=0; i<N; ++i) cin >> A[i];

  vector<bool> tmp(K, false);
  vector<vector<bool>> dp_L(N, tmp), dp_R(N, tmp);
  dp_L[0][0] = dp_R[0][0] = true;

  for(ll i=0; i<N-1; ++i){
    dp_L[i+1] = dp_L[i];
    dp_R[i+1] = dp_R[i];
    ll aL = A[i], aR = A[N-1-i];
    if(aL<K){ for(ll j=0; j<K-aL; ++j) dp_L[i+1][j+aL] = dp_L[i][j]; }
    if(aR<K){ for(ll j=0; j<K-aR; ++j) dp_R[i+1][j+aR] = dp_R[i][j]; }
  }

  ll ans = 0;
  for(ll i=0; i<N; ++i) {
    vector<bool>& dl = dp_L[i];
    vector<bool>& dr = dp_R[N-1-i];

    bool noneed = true;
    ll ml = -K;
    for(ll j=0; j<K; ++j) {
      if (dl[j]) { ml = j; }
      if (dr[K-1-j] && j-ml<A[i]) {
        noneed = false;
        break;
      }
    }
    if (noneed) ++ans;
  }

  cout << ans << endl;

  return 0;
}
