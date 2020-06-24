#include<iostream>
#include<vector>
using namespace std;
#define ll long long

int main(){
  ll H, W, D;
  cin >> H >> W >> D;
  ll N = H*W;

  vector<ll> X(N), Y(N);
  for(ll h=0; h<H; ++h)
  for(ll w=0; w<W; ++w){
    ll A;
    cin >> A;
    X[A-1] = w;
    Y[A-1] = h;
  }

  vector<ll> S(N);
  for(ll d=0; d<D; ++d) {
    S[d] = 0;
    for(ll k = d+D; k<N; k+=D) { S[k] = S[k-D] + abs(X[k]-X[k-D]) + abs(Y[k]-Y[k-D]);  }
  }

  ll Q, L, R;
  cin >> Q;
  for(ll q=0; q<Q; ++q){
    cin >> L >> R;
    cout << S[R-1]-S[L-1] << endl;
  }
  

  return 0;
}
