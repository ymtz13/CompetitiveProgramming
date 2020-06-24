#include<iostream>
using namespace std;
#define ll long long

int main(){
  ll N, ans=0;
  cin >> N;
  
  for(ll i=0; i<N; ++i) {
    ll a;
    cin >> a;
    while(a%2==0){ a/=2; ++ans; }
  }

  cout << ans << endl;
  
  return 0;
}
