#include<iostream>
#include<vector>
using namespace std;
#define ll long long
#define INF 10000000000;

int main(){
  ll N, K;
  cin >> N >> K;
  vector<ll> H(N+1), C(N+1);
  H[0] = 0;
  C[1] = 0;
  for(ll i=1; i<N+1; ++i){
    cin >> H[i];
  }

  for(ll i=2; i<N+1; ++i) {
    ll m = INF;
    for(ll j=1; j<min(K+1, i); ++j) { m = min<ll>(C[i-j]+abs(H[i-j]-H[i]), m); }
    C[i] = m;
  }

  cout << C[N] << endl;

  return 0;
}
