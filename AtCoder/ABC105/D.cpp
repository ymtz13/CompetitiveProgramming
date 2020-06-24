#include<iostream>
#include<map>
using namespace std;
#define ll long long

int main(){
  ll N, M;
  cin >> N >> M;

  map<ll, ll> X;
  X[0]=1;

  ll A, S = 0, ans = 0;
  for(ll i=0; i<N; ++i) {
    cin >> A;
    S = (S+A)%M;
    auto itr = X.find(S);
    if(itr!=X.end()) ans += X[S]++;
    else X[S]=1;
  }

  cout << ans << endl;

  return 0;
}
