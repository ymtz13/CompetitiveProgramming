#include<iostream>
#include<vector>
using namespace std;
#define ll long long

int main(){
  ll N, M, Q;
  cin >> N >> M >> Q;

  vector<vector<ll>> X(N+1), S1(N+1), S2(N+1);
  vector<ll> row(N+1, 0);
  for(ll i=0; i<N+1; ++i) X[i] = S1[i] = S2[i] = row;
  
  for(ll m=0; m<M; ++m) {
    ll L, R;
    cin >> L >> R;
    ++X[L][R];
  }

  for(ll l=1; l<N+1; ++l) for(ll r=l; r<N+1; ++r) S1[l][r] = S1[l][r-1] + X[l][r];
  for(ll r=1; r<N+1; ++r) for(ll l=1; l<N+1; ++l) S2[l][r] = S2[l-1][r] + S1[l][r];

  for(ll iq=0; iq<Q; ++iq) {
    ll p,q;
    cin >> p >> q;
    cout << S2[q][q]-S2[p-1][q]-S2[q][p-1]+S2[p-1][p-1] << endl;
  }
  
  return 0;
}
