#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define ll long long

ll N, K;

bool check(ll m, vector<ll>& A, vector<ll>& F) {
  ll cost = 0, B;
  for(ll i=0; i<N; ++i){
    B = m/F[i];
    cost += max<ll>(A[i]-B, 0);
  }
  return cost<=K;
}

int main(){
  cin >> N >> K;

  vector<ll> A(N);
  vector<ll> F(N);
  for(ll i=0; i<N; ++i) cin >> A[i];
  for(ll i=0; i<N; ++i) cin >> F[i];

  sort(A.begin(), A.end());
  sort(F.begin(), F.end(), std::greater<int>() );

  //for(ll i=0; i<N; ++i) cout<<A[i];
  //for(ll i=0; i<N; ++i) cout<<F[i];

  
  ll mmax = A[N-1]*F[0] + 1;
  ll mmin = -1;
  ll mtgt = mmax/2;
  ll ans;
  
  while(true) {
    bool ok = check(mtgt, A, F);
    if(ok) {
      if(mtgt-mmin==1) { ans = mtgt; break; }
      mmax = mtgt;
      mtgt = (mmax+mmin)/2;
    }else{
      if(mmax-mtgt==1) { ans = mmax; break; }
      mmin = mtgt;
      mtgt = (mmax+mmin)/2;
    }
  }

  cout << ans << endl;
  
  return 0;
}
