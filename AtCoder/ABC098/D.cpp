#include<iostream>
#include<vector>
using namespace std;
#define ll long long

int main(){
  ll N; cin >> N;
  vector<ll> A(N);
  for(ll i=0; i<N; ++i) cin >> A[i];

  ll r=0, sl=0, sl_xor=0, sr=A[0], sr_xor=A[0];
  ll ans = 0;
  for(ll l=0; l<N; ++l){
    for(; r<N && (sr-sl==(sr_xor^sl_xor)); ++r) { sr+=A[r+1]; sr_xor^=A[r+1]; }
    ans += r-l;
    sl += A[l];
    sl_xor ^= A[l];
  }

  cout << ans << endl;

  return 0;
}
