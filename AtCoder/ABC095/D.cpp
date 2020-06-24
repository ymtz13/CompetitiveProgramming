#include<iostream>
#include<vector>
using namespace std;
#define ll long long

struct S{
  ll x, v;
  S(ll x, ll v): x(x), v(v) {}
};

int main(){
  ll N, C;
  cin >> N >> C;

  vector<S> Slist;
  for(ll i=0; i<N; ++i) {
    ll x, v;
    cin >> x >> v;
    Slist.emplace_back(x,v);
  }

  ll ans = 0;
  
  vector<ll> max_f(N), max_b(N);
  {
    ll sum_v = 0, m = 0;
    for(ll i=0; i<N; ++i) {
      S& s = Slist[i];
      sum_v += s.v;
      m = max_f[i] = max(m, sum_v - s.x);
    }
    ans = max(ans, m);
  }
  
  {
    ll sum_v = 0, m = 0;
    for(ll i=N-1; i>=0; --i) {
      S& s = Slist[i];
      sum_v += s.v;
      m = max_b[i] = max(m, sum_v - (C - s.x));
    }
    ans = max(ans, m);
  }
  
  for(ll i=0;   i<N-1; ++i) ans = max(ans, max_f[i]+max_b[i+1]-Slist[i].x);
  for(ll i=N-1; i>=1 ; --i) ans = max(ans, max_f[i-1]+max_b[i]-(C-Slist[i].x));

  cout << ans << endl;
  
  return 0;
}
