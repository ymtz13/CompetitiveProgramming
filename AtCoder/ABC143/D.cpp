#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define ll long long

int main(){
  ll N;
  cin >> N;
  vector<ll> L;
  ll buf;
  for(ll i=0; i<N; ++i){ cin >> buf; L.emplace_back(buf); }
  sort(L.begin(), L.end());

  ll ans = 0;
  
  for(ll i=0; i<N; ++i)
  for(ll j=i+1; j<N; ++j){
    auto itr = lower_bound(L.begin(), L.end(), L[i]+L[j]);
    ans += max(0, (int)(itr-L.begin()-j-1));
  }

  cout << ans << endl;

  return 0;
}
