#include<iostream>
#include<vector>
#include<set>
using namespace std;
#define ll long long

struct F{
  ll A, B;
  F(ll A, ll B): A(A), B(B){}
};

struct Cmp_A { bool operator()(F l, F r) const { return l.A<r.A; } };

int main(){
  ll N, T;
  cin >> N >> T;

  multiset<F, Cmp_A> foods;
  
  for(ll n=0; n<N; ++n){
    ll A, B;
    cin >> A >> B;
    F f(A,B);
    foods.insert(f);
  }


  vector<ll> dp(T+3001, -1);
  dp[0]=0;
  for(auto itr=foods.begin(); itr!=foods.end(); ++itr){
    ll A = itr->A;
    ll B = itr->B;
    //for(ll t=T-1; t>=0 && t+A>=T; --t) {
    //  if(dp[t]!=-1 && dp[t]+B>dp[T]) { dp[T]=dp[t]+B; break; }
    // }

    for(ll t=dp.size()-1; t-A>=0; --t) {
      if(t-A<T && dp[t-A]!=-1 && dp[t-A]+B>dp[t]) dp[t] = dp[t-A]+B;
    }
  }
  
  // for(ll i=0; i<dp.size(); ++i) { cout<<dp[i]<<" "; } cout << endl;
  ll ans = 0;
  for(ll i=dp.size()-1; i>=0; --i) { if(ans < dp[i]) ans = dp[i]; }
  cout << ans << endl;

  return 0;
}
