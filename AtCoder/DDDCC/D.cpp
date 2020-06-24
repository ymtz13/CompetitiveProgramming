#include<iostream>
#include<vector>
using namespace std;
#define ll long long

int main(){
  ll M, ans;
  cin >> M;
  
  vector<ll> X;
  //                     1   2  3   4    5   6   7     8  9
  vector<ll> cost = {0, 70, 77, 4, 91,  98,  5, 112, 119, 2};
  vector<ll> num  = {0, 64, 64, 4, 64,  64,  4,  64,  64, 2};
  for(ll i=0; i<M; ++i) {
    ll d, c;
    cin >> d >> c;
    if(d==0){ ans+=c; continue; }

    while(c>=num[d]){
      ans += (c/num[d])*cost[d];
      c = c/num[d] + c%num[d];
    }
    
    for(ll i=0; i<c; ++i) X.emplace_back(d);
  }

  ll v = X[0];
  for(ll i=1; i<X.size(); ++i){
    ans += 1 + (v+X[i])/10;
    v = (v+X[i])/10 + (v+X[i])%10;
  }

  cout << ans << endl;

  return 0;
}
