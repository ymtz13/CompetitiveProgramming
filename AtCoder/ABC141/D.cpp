#include<iostream>
#include<set>
using namespace std;
#define ll long long

int main(){
  ll N, M;
  cin >> N >> M;
  multiset<ll> A;
  ll a;
  for(ll i=0; i<N; ++i){
    cin >> a;
    A.insert(a);
  }

  for(ll i=0; i<M; ++i){
    auto max = --A.end();
    A.insert((*max)/2);
    A.erase(max);
  }

  ll ans=0;
  for(auto itr=A.begin(); itr!=A.end(); ++itr) ans+=(*itr);

  cout << ans << endl;
    

  return 0;
}
